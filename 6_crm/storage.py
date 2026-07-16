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
            print(raw)
        except json.JSONDecodeError as e:
            print(f"Файл поврежден {e}")
            return []
    for order in raw:
        order["tags"] = set(order["tags"])

    return raw


def save(orders: list[Order], path: str):
    """ Сохранить список заказов в JSON файл """
    pass
