""" Модуль парсинга аргументов / команд """

import argparse

from orders import OrderStatus

_STATUSES: tuple[OrderStatus, ...] = ("new", "in_progress", "done", "cancelled")


def build_parser() -> argparse.ArgumentParser:
    """ Собрать парсер аргументов командной строки crm-утилиты """
    parser = argparse.ArgumentParser(
        prog="crm", description="CRM утилита для управления заказами"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="Вывести таблицу заказов")
    list_parser.add_argument(
        "--overdue", action="store_true", help="Только просроченные заказы"
    )
    list_parser.add_argument("--tag", help="Фильтр по тегу")
    list_parser.add_argument(
        "--limit", type=int, help="Ограничить количество выводимых заказов"
    )

    add_parser = subparsers.add_parser("add", help="Добавить новый заказ")
    add_parser.add_argument("--title", required=True, help="Название заказа")
    add_parser.add_argument(
        "--amount", required=True, type=float, help="Сумма заказа"
    )
    add_parser.add_argument("--email", required=True, help="Email клиента")
    add_parser.add_argument("--due", help="Срок выполнения (YYYY-MM-DD)")
    add_parser.add_argument("--tags", help="Теги через запятую, например a,b,c")

    remove_parser = subparsers.add_parser("remove", help="Удалить заказ по id")
    remove_parser.add_argument("--id", required=True, help="Id заказа")

    edit_parser = subparsers.add_parser(
        "edit", help="Изменить только переданные поля заказа"
    )
    edit_parser.add_argument("--id", required=True, help="Id заказа")
    edit_parser.add_argument("--title", help="Новое название заказа")
    edit_parser.add_argument("--amount", type=float, help="Новая сумма заказа")
    edit_parser.add_argument("--email", help="Новый email клиента")
    edit_parser.add_argument("--due", help="Новый срок выполнения (YYYY-MM-DD)")

    tags_parser = subparsers.add_parser("tags", help="Управление тегами заказа")
    tags_parser.add_argument("--id", required=True, help="Id заказа")
    tags_parser.add_argument("--add", help="Теги для добавления через запятую")
    tags_parser.add_argument("--remove", help="Теги для удаления через запятую")

    status_parser = subparsers.add_parser("status", help="Изменить статус заказа")
    status_parser.add_argument("--id", required=True, help="Id заказа")
    status_parser.add_argument("status", choices=_STATUSES, help="Новый статус")

    return parser
