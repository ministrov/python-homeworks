""" Модуль проверки полей заказа """

import re


_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate_email(email: str) -> None:
    """ Проверить формат email """
    if not _EMAIL_RE.match(email):
        raise ValueError(f"Некорректный email: {email}")


def validate_amount(amount: float) -> None:
    """ Проверить, что сумма заказа положительна """
    if amount <= 0:
        raise ValueError(f"Сумма заказа должна быть положительной: {amount}")


def parse_tags(raw: str) -> set[str]:
    """ Разобрать строку тегов через запятую в множество """
    return {tag.strip() for tag in raw.split(",") if tag.strip()}
