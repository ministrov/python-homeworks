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
