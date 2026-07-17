""" Модуль проверки полей заказа """


def validate_email(email: str) -> None:
    """ Проверить формат email """
    if "@" not in email:
        raise ValueError(f"Некорректный email: {email}")

    parts = email.split("@")
    if len(parts) != 2:
        raise ValueError(f"Некорректный email: {email}")

    name_part = parts[0]
    domain_part = parts[1]
    if not name_part or "." not in domain_part:
        raise ValueError(f"Некорректный email: {email}")


def validate_amount(amount: float) -> None:
    """ Проверить, что сумма заказа положительна """
    if amount <= 0:
        raise ValueError(f"Сумма заказа должна быть положительной: {amount}")


def parse_tags(raw: str) -> set[str]:
    """ Разобрать строку тегов через запятую в множество """
    tags: set[str] = set()
    parts = raw.split(",")
    for part in parts:
        tag = part.strip()
        if tag:
            tags.add(tag)
    return tags
