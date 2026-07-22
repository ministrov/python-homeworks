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
    def __init__(self, account_holder: str, account_number: str | int, current_balance: int = 0):
        if current_balance < 0:
            raise ValueError("Баланс не может быть отрицательным")

        self.account_holder = account_holder
        self.account_number = account_number
        self.current_balance = current_balance

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Нельзя пополнять на отрицательную сумму")
        self.current_balance += amount

    def withdraw(self, amount: int):
        if amount <= 0:
            raise ValueError("Нельзя снимать на отрицательную сумму")
        if self.current_balance - amount < 0:
            raise ValueError("Недостаточно средств на счёте")
        self.current_balance -= amount

    def transfer_to(self, other_account: BankAccount, amount: int):
        self.withdraw(amount)
        other_account.deposit(amount)

    def info(self) -> str:
        return (f"Счёт №{self.account_number} "
                f"(владелец: {self.account_holder}), "
                f"баланс: {self.current_balance}")
