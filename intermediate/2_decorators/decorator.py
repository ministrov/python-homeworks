""" Модуль домашнего задания по теме Декораторы

    Задание: def limit_args

    Декоратор для ограничения числовых аргументов функции. Параметры:

    max_value: максимальное допустимое значение для числовых аргументов
    mode: "error" или "clip"
                - "error" — при превышении max_value выбрасывать ValueError

                - "clip" — при превышении maxvalue заменять значение на maxvalue

    @limit_args(max_value=10, mode="clip")
    def multiply(a, b):
        return a * b

    multiply(2, 3) = 6
    multiply(100, 3) = 30
"""

from functools import wraps
from typing import Any, Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def limit_args(max_value: int, mode: str) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Декоратор для ограничения числовых аргументов функции.

    :param max_value: максимальное допустимое значение для числовых аргументов
    :param mode: "error" — выбрасывать ValueError при превышении max_value
                 "clip"  — заменять значение на max_value при превышении
    """
    if mode not in ("error", "clip"):
        raise ValueError('mode должен быть "error" или "clip"')

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            def process(value: Any) -> Any:
                if isinstance(value, (int, float)) and not isinstance(value, bool):
                    if value > max_value:
                        if mode == "error":
                            raise ValueError(
                                f"Значение {value} превышает допустимый максимум {max_value}"
                            )
                        else:  # mode == "clip"
                            return max_value
                return value

            new_args = tuple(process(a) for a in args)
            new_kwargs = {k: process(v) for k, v in kwargs.items()}

            return func(*new_args, **new_kwargs)

        return wrapper

    return decorator


# ---------- Проверка ----------
if __name__ == "__main__":
    @limit_args(max_value=10, mode="clip")
    def multiply(a: int, b: int) -> int:
        return a * b

    print(multiply(2, 3))     # 6
    print(multiply(100, 3))   # 30  (100 -> 10)

    @limit_args(max_value=10, mode="error")
    def add(a: int, b: int) -> int:
        return a + b

    print(add(2, 3))          # 5
    try:
        add(20, 1)
    except ValueError as e:
        print(e)               # Значение 20 превышает допустимый максимум 10
