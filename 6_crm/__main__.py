""" Модуль точки входа приложения crm системы """

import sys
from typing import cast

import storage
from cli import build_parser
from orders import (
    Order,
    OrderStatus,
    add_tags,
    create_order,
    edit_order,
    filter_by_tag,
    filter_overdue,
    list_orders,
    new_order,
    remove_order,
    remove_tags,
    set_status,
)
from utils.validators import parse_tags, validate_amount, validate_email

STORAGE_PATH = "orders.json"


def _stringify_orders(orders: list[Order]) -> str:
    """ Собрать заказы в текстовую таблицу """
    headers = ["ID", "TITLE", "AMOUNT", "STATUS", "DUE"]
    rows: list[list[str]] = [
        [
            order["id"],
            order["title"],
            f"{order['amount']:.2f}",
            order["status"],
            order["due"] or "-",
        ]
        for order in orders
    ]

    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, col in enumerate(row):
            col_widths[i] = max(col_widths[i], len(col))

    def format_row(row: list[str]) -> str:
        return " | ".join(f"{col:<{col_widths[i]}}" for i, col in enumerate(row))

    lines = [format_row(headers), "-+-".join("-" * w for w in col_widths)]
    lines.extend(format_row(row) for row in rows)
    return "\n".join(lines)


def run(argv: list[str] | None = None) -> None:
    """ Разобрать аргументы и выполнить соответствующую команду """
    args = build_parser().parse_args(argv)
    orders = storage.load(STORAGE_PATH)

    if args.command == "list":
        result = list_orders(orders)
        if args.overdue:
            result = filter_overdue(result)
        if args.tag:
            result = filter_by_tag(result, args.tag)
        if args.limit is not None:
            result = result[: args.limit]
        print(_stringify_orders(result) if result else "Заказов нет")
        return

    if args.command == "add":
        validate_email(args.email)
        validate_amount(args.amount)
        tags = parse_tags(args.tags) if args.tags else set()
        order = new_order(args.title, args.amount, args.email, args.due, tags)
        create_order(orders, order)
        storage.save(orders, STORAGE_PATH)
        print(f"Заказ создан: {order['id']}")
        return

    if args.command == "remove":
        removed = remove_order(orders, args.id)
        storage.save(orders, STORAGE_PATH)
        print(f"Заказ удалён: {removed['id']}")
        return

    if args.command == "edit":
        updates: dict[str, object] = {}
        if args.title is not None:
            updates["title"] = args.title
        if args.amount is not None:
            validate_amount(args.amount)
            updates["amount"] = args.amount
        if args.email is not None:
            validate_email(args.email)
            updates["email"] = args.email
        if args.due is not None:
            updates["due"] = args.due
        if not updates:
            print("Не переданы поля для редактирования")
            sys.exit(1)
        edit_order(orders, args.id, updates)
        storage.save(orders, STORAGE_PATH)
        print(f"Заказ изменён: {args.id}")
        return

    if args.command == "tags":
        if not args.add and not args.remove:
            print("Нужно передать --add и/или --remove")
            sys.exit(1)
        if args.add:
            add_tags(orders, args.id, parse_tags(args.add))
        if args.remove:
            remove_tags(orders, args.id, parse_tags(args.remove))
        storage.save(orders, STORAGE_PATH)
        print(f"Теги заказа обновлены: {args.id}")
        return

    if args.command == "status":
        status = cast(OrderStatus, args.status)
        set_status(orders, args.id, status)
        storage.save(orders, STORAGE_PATH)
        print(f"Статус заказа изменён: {args.id} -> {status}")
        return


if __name__ == "__main__":
    try:
        run()
    except (KeyError, ValueError) as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
