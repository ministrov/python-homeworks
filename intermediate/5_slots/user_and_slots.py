"""
    Создать класс User с полями: имя, email, password

        Создать класс SlotUser с полями: имя, email, password используя slots

        Создать 2 списка из 100 000 экземпляров каждого класса и вывести сравнение занимаемой памяти
"""


import ast
# import dis
# import sys


source = open(__file__).read()
print(ast.dump(ast.parse(source), indent=2))


class User:
    """ Обычный пользователь """

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


anton = User("Anton", 34)
print(anton.name)

# dis.dis(User.__init__)
# print(sys.getrefcount(anton))
print(anton.__dict__)
print(User.__dict__)
