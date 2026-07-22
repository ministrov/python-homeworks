""" Модуль заказов """

import uuid
from datetime import date, datetime
from typing import Literal, TypedDict


OrderStatus = Literal["new", "in_progress", "done", "cancelled"]

_EDITABLE_FIELDS = {"title", "amount", "email", "due"}
_CLOSED_STATUSES = ("done", "cancelled")


class Order(TypedDict):
    id: str
    title: str
    amount: float
    email: str
    status: OrderStatus
    tags: set[str]
    created_at: str
    due: str | None
    closed_at: str | None


def new_order(
    title: str,
    amount: float,
    email: str,
    due: str | None = None,
    tags: set[str] | None = None,
) -> Order:
    """ Создать новый заказ со сгенерированным id """
    if tags is None:
        tags = set()

    order: Order = {
        "id": str(uuid.uuid4()),
        "title": title,
        "amount": amount,
        "email": email,
        "status": "new",
        "tags": tags,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "due": due,
        "closed_at": None,
    }
    return order


def create_order(orders: list[Order], order: Order) -> None:
    """ Добавить новый заказ в список заказов """
    orders.append(order)


def list_orders(orders: list[Order]) -> list[Order]:
    """ Вернуть список заказов """
    return orders


def find_order(orders: list[Order], order_id: str) -> Order:
    """ Найти заказ по id """
    for order in orders:
        if order["id"] == order_id:
            return order
    raise KeyError(f"Заказ с id={order_id} не найден")


def edit_order(
    orders: list[Order], order_id: str, updates: dict[str, object]
) -> Order:
    """ Изменить переданные поля заказа по id """
    order = find_order(orders, order_id)
    for key, value in updates.items():
        if key not in _EDITABLE_FIELDS:
            raise KeyError(f"Поле '{key}' нельзя редактировать")
        order[key] = value
    return order


def remove_order(orders: list[Order], order_id: str) -> Order:
    """ Удалить заказ по id """
    order = find_order(orders, order_id)
    orders.remove(order)
    return order


def add_tags(orders: list[Order], order_id: str, tags: set[str]) -> Order:
    """ Добавить теги заказу """
    order = find_order(orders, order_id)
    for tag in tags:
        order["tags"].add(tag)
    return order


def remove_tags(orders: list[Order], order_id: str, tags: set[str]) -> Order:
    """ Убрать теги у заказа """
    order = find_order(orders, order_id)
    for tag in tags:
        if tag in order["tags"]:
            order["tags"].remove(tag)
    return order


def set_status(orders: list[Order], order_id: str, status: OrderStatus) -> Order:
    """ Изменить статус заказа """
    order = find_order(orders, order_id)
    order["status"] = status
    if status in _CLOSED_STATUSES:
        order["closed_at"] = datetime.now().isoformat(timespec="seconds")
    else:
        order["closed_at"] = None
    return order


def is_overdue(order: Order, today: date | None = None) -> bool:
    """ Проверить, просрочен ли заказ """
    if today is None:
        today = date.today()

    if order["due"] is None:
        return False

    if order["status"] in _CLOSED_STATUSES:
        return False

    due_date = date.fromisoformat(order["due"])
    if due_date < today:
        return True
    return False


def filter_by_tag(orders: list[Order], tag: str) -> list[Order]:
    """ Отфильтровать заказы по тегу """
    result: list[Order] = []
    for order in orders:
        if tag in order["tags"]:
            result.append(order)
    return result


def filter_overdue(orders: list[Order]) -> list[Order]:
    """ Отфильтровать просроченные заказы """
    result: list[Order] = []
    for order in orders:
        if is_overdue(order):
            result.append(order)
    return result
