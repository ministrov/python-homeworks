""" Модуль парсинга аргументов / команд """


def parse_list(args: list[str]) -> tuple[bool, str | None, int | None]:
    """ Разобрать аргументы команды list """
    overdue = False
    tag = None
    limit = None

    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--overdue":
            overdue = True
            i += 1
        elif arg == "--tag":
            tag = args[i + 1]
            i += 2
        elif arg == "--limit":
            limit = int(args[i + 1])
            i += 2
        else:
            raise ValueError(f"Неизвестный аргумент: {arg}")

    return overdue, tag, limit


def parse_add(
    args: list[str],
) -> tuple[str, float, str, str | None, str | None]:
    """ Разобрать аргументы команды add """
    title = None
    amount = None
    email = None
    due = None
    tags = None

    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--title":
            title = args[i + 1]
            i += 2
        elif arg == "--amount":
            amount = float(args[i + 1])
            i += 2
        elif arg == "--email":
            email = args[i + 1]
            i += 2
        elif arg == "--due":
            due = args[i + 1]
            i += 2
        elif arg == "--tags":
            tags = args[i + 1]
            i += 2
        else:
            raise ValueError(f"Неизвестный аргумент: {arg}")

    if title is None or amount is None or email is None:
        raise ValueError("Нужно передать --title, --amount и --email")

    return title, amount, email, due, tags


def parse_remove(args: list[str]) -> str:
    """ Разобрать аргументы команды remove """
    order_id = None

    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--id":
            order_id = args[i + 1]
            i += 2
        else:
            raise ValueError(f"Неизвестный аргумент: {arg}")

    if order_id is None:
        raise ValueError("Нужно передать --id")

    return order_id


def parse_edit(
    args: list[str],
) -> tuple[str, str | None, float | None, str | None, str | None]:
    """ Разобрать аргументы команды edit """
    order_id = None
    title = None
    amount = None
    email = None
    due = None

    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--id":
            order_id = args[i + 1]
            i += 2
        elif arg == "--title":
            title = args[i + 1]
            i += 2
        elif arg == "--amount":
            amount = float(args[i + 1])
            i += 2
        elif arg == "--email":
            email = args[i + 1]
            i += 2
        elif arg == "--due":
            due = args[i + 1]
            i += 2
        else:
            raise ValueError(f"Неизвестный аргумент: {arg}")

    if order_id is None:
        raise ValueError("Нужно передать --id")

    return order_id, title, amount, email, due


def parse_tags_command(
    args: list[str],
) -> tuple[str, str | None, str | None]:
    """ Разобрать аргументы команды tags """
    order_id = None
    add = None
    remove = None

    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--id":
            order_id = args[i + 1]
            i += 2
        elif arg == "--add":
            add = args[i + 1]
            i += 2
        elif arg == "--remove":
            remove = args[i + 1]
            i += 2
        else:
            raise ValueError(f"Неизвестный аргумент: {arg}")

    if order_id is None:
        raise ValueError("Нужно передать --id")

    return order_id, add, remove


def parse_status(args: list[str]) -> tuple[str, str]:
    """ Разобрать аргументы команды status """
    order_id = None
    status = None

    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--id":
            order_id = args[i + 1]
            i += 2
        elif not arg.startswith("--"):
            status = arg
            i += 1
        else:
            raise ValueError(f"Неизвестный аргумент: {arg}")

    if order_id is None or status is None:
        raise ValueError("Использование: status --id <id> <новый статус>")

    return order_id, status
