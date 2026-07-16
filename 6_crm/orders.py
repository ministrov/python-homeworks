""" Модуль заказов """

from typing import Literal, TypedDict


OrderStatus = Literal["new", "in_progress", "done", "cancelled"]


class Order(TypedDict):
    id: int
    title: str
    amount: float
    email: str
    status: OrderStatus
    tags: set[str]
    created_at: str
    due: str | None
    closed_at: str | None


def create_order(orders: list[Order], order: Order) -> None:
    """ Добавить новый заказ в список заказов """
    orders.append(order)


def list_orders(orders: list[Order]) -> list[Order] | None:
    """ Вернуть список заказов """
    return orders


def edit_order(
    orders: list[Order], order_id: int, updates: dict[str, object]
) -> Order | None:
    """ Изменить поля заказа по id """
    for order in orders:
        if order["id"] == order_id:
            for key, value in updates.items():
                order[key] = value
            return order
    return None


def remove_order(orders: list[Order], order_id: int) -> Order | None:
    """ Удалить заказ по id """
    for order in orders:
        if order["id"] == order_id:
            orders.remove(order)
            return order
    return None
