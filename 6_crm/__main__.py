""" Модуль точки входа приложения crm системы """

import sys

import cli
import storage
from orders import (
    Order,
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
from utils.table import print_orders
from utils.validators import (
    parse_tags,
    validate_amount,
    validate_email,
    validate_status,
)

STORAGE_PATH = "orders.json"


def run_list(orders: list[Order], args: list[str]) -> None:
    """ Выполнить команду list """
    overdue, tag, limit = cli.parse_list(args)

    result = list_orders(orders)
    if overdue:
        result = filter_overdue(result)
    if tag is not None:
        result = filter_by_tag(result, tag)
    if limit is not None:
        result = result[:limit]

    print_orders(result)


def run_add(orders: list[Order], args: list[str]) -> None:
    """ Выполнить команду add """
    title, amount, email, due, tags_string = cli.parse_add(args)
    validate_email(email)
    validate_amount(amount)

    tags: set[str] = set()
    if tags_string is not None:
        tags = parse_tags(tags_string)

    order = new_order(title, amount, email, due, tags)
    create_order(orders, order)
    storage.save(orders, STORAGE_PATH)
    print(f"Заказ создан: {order['id']}")


def run_remove(orders: list[Order], args: list[str]) -> None:
    """ Выполнить команду remove """
    order_id = cli.parse_remove(args)
    removed = remove_order(orders, order_id)
    storage.save(orders, STORAGE_PATH)
    print(f"Заказ удалён: {removed['id']}")


def run_edit(orders: list[Order], args: list[str]) -> None:
    """ Выполнить команду edit """
    order_id, title, amount, email, due = cli.parse_edit(args)

    updates: dict[str, object] = {}
    if title is not None:
        updates["title"] = title
    if amount is not None:
        validate_amount(amount)
        updates["amount"] = amount
    if email is not None:
        validate_email(email)
        updates["email"] = email
    if due is not None:
        updates["due"] = due

    if not updates:
        print("Не переданы поля для редактирования")
        sys.exit(1)

    edit_order(orders, order_id, updates)
    storage.save(orders, STORAGE_PATH)
    print(f"Заказ изменён: {order_id}")


def run_tags(orders: list[Order], args: list[str]) -> None:
    """ Выполнить команду tags """
    order_id, add, remove = cli.parse_tags_command(args)

    if add is None and remove is None:
        print("Нужно передать --add и/или --remove")
        sys.exit(1)

    if add is not None:
        add_tags(orders, order_id, parse_tags(add))
    if remove is not None:
        remove_tags(orders, order_id, parse_tags(remove))

    storage.save(orders, STORAGE_PATH)
    print(f"Теги заказа обновлены: {order_id}")


def run_status(orders: list[Order], args: list[str]) -> None:
    """ Выполнить команду status """
    order_id, status = cli.parse_status(args)
    validate_status(status)
    set_status(orders, order_id, status)  # type: ignore[arg-type]
    storage.save(orders, STORAGE_PATH)
    print(f"Статус заказа изменён: {order_id} -> {status}")


def main() -> None:
    """ Разобрать команду и выполнить её """
    if len(sys.argv) < 2:
        print("Использование: python __main__.py <команда> [аргументы]")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]
    orders = storage.load(STORAGE_PATH)

    if command == "list":
        run_list(orders, args)
    elif command == "add":
        run_add(orders, args)
    elif command == "remove":
        run_remove(orders, args)
    elif command == "edit":
        run_edit(orders, args)
    elif command == "tags":
        run_tags(orders, args)
    elif command == "status":
        run_status(orders, args)
    else:
        print(f"Неизвестная команда: {command}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except (KeyError, ValueError) as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
