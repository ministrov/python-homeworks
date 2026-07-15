""" Модуль заказов """

from typing import Literal, TypedDict, cast


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


def list_orders(orders: list[Order]) -> list[Order]:
    """ Вернуть список заказов """
    return orders


_EDITABLE_FIELDS = {
    "title", "amount", "email", "status", "tags", "due", "closed_at",
}


def _find_order(orders: list[Order], order_id: int) -> Order:
    """ Найти заказ по id, иначе бросить KeyError """
    for order in orders:
        if order["id"] == order_id:
            return order
    raise KeyError(f"Заказ с id={order_id} не найден")


def edit_order(
    orders: list[Order], order_id: int, updates: dict[str, object]
) -> Order:
    """ Изменить поля заказа по id """
    order = _find_order(orders, order_id)

    for key, value in updates.items():
        if key not in _EDITABLE_FIELDS:
            raise KeyError(f"Заказу нельзя менять поле: {key}")
        cast(dict[str, object], order)[key] = value

    return order


def remove_order(orders: list[Order], order_id: int) -> Order:
    """ Удалить заказ по id """
    order = _find_order(orders, order_id)
    orders.remove(order)
    return order
