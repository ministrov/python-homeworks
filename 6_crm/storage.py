""" Модуль хранилища JSON данных"""

import json
from pathlib import Path
from orders import Order


def load(path: str) -> list[Order]:
    """ Загрузить список заказов из JSON файла """
    if not Path(path).exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        try:
            raw = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Файл поврежден {e}")
            return []
    for order in raw:
        order["tags"] = set(order["tags"])

    return raw


def save(orders: list[Order], path: str) -> None:
    """ Сохранить список заказов в JSON файл """
    serializable: list[dict[str, object]] = []
    for order in orders:
        order_copy = dict(order)
        order_copy["tags"] = list(order["tags"])
        serializable.append(order_copy)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(serializable, f, ensure_ascii=False, indent=2)
