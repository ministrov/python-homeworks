""" Модуль вывода заказов в виде таблицы """

from orders import Order


def print_orders(orders: list[Order]) -> None:
    """ Напечатать заказы в виде таблицы """
    if not orders:
        print("Заказов нет")
        return

    print(f"{'ID':<38}{'TITLE':<25}{'AMOUNT':<12}{'STATUS':<14}{'DUE':<12}")
    for order in orders:
        due = order["due"]
        if due is None:
            due = "-"
        print(
            f"{order['id']:<38}{order['title']:<25}"
            f"{order['amount']:<12.2f}{order['status']:<14}{due:<12}"
        )
