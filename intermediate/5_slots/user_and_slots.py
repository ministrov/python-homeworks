"""
    Создать класс User с полями: имя, email, password

        Создать класс SlotUser с полями: имя, email, password используя slots

        Создать 2 списка из 100 000 экземпляров каждого класса и вывести сравнение занимаемой памяти
"""


class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


anton = User("Anton", 34)
print(anton.name)
