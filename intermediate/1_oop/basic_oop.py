""" Модуль для выполнения дз по теме Базовый ООП 

    Задача: 
    
    1. Нужно реализовать класс BankAccount, описывающий банковский счёт простого вида. У счёта должны быть:
            владелец счёта (строка, имя);
            номер счёта (строка или число);
            текущий баланс (число, не может быть отрицательным);
            При создании счёта баланс может задаваться, а если не задан — считается 0.

    2. Класс BankAccount должен уметь:
            Создавать новый счёт в конструкторе init
            deposit(amount) — пополнение счёта на сумму amount.
            withdraw(amount) — снятие денег со счёта. Нельзя уйти в минус.
            transferto(otheraccount, amount) — перевод денег на другой счёт BankAccount.
            info() — возвращать строку с краткой информацией о счёте
            @classmethod def getaccountscreated(cls) — возвращает количество созданных счетов.
"""


class BankAccount:
    balance: int = 0

    def __init__(self, account_owener: str, account_number: str | int, current_balance: int = balance):
        self.account_owener = account_owener
        self.account_number = account_number
        self.current_balance = current_balance

        if self.current_balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
