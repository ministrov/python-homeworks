""" Модуль точки входа приложения crm системы """

import storage
from orders import Order, create_order, edit_order, list_orders, remove_order

if __name__ == "__main__":
    orders: list[Order] = []

    order_1: Order = {
        "id": 1,
        "title": "Сайт-визитка",
        "amount": 15000.0,
        "email": "client1@example.com",
        "status": "new",
        "tags": {"web"},
        "created_at": "2026-07-14",
        "due": "2026-08-01",
        "closed_at": None,
    }
    order_2: Order = {
        "id": 2,
        "title": "Мобильное приложение",
        "amount": 80000.0,
        "email": "client2@example.com",
        "status": "in_progress",
        "tags": {"mobile", "ios"},
        "created_at": "2026-07-10",
        "due": "2026-09-01",
        "closed_at": None,
    }

    create_order(orders, order_1)
    create_order(orders, order_2)
    print("После create_order:", list_orders(orders))

    edit_order(orders, 1, {"status": "done", "closed_at": "2026-07-14"})
    print("После edit_order:", list_orders(orders))

    removed = remove_order(orders, 2)
    print("Удалён:", removed)
    print("После remove_order:", list_orders(orders))

    storage.save(orders, "orders.json")
    loaded = storage.load("orders.json")
    print("После save/load:", loaded)
