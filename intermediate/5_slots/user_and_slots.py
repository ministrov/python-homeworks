"""
    Создать класс User с полями: имя, email, password

        Создать класс SlotUser с полями: имя, email, password используя slots

        Создать 2 списка из 100 000 экземпляров каждого класса и вывести сравнение занимаемой памяти
"""


import sys


class User:
    """ Обычный пользователь с (__dict__) """

    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name
        self.email = email
        self.password = password


class SlotUser:
    """ Обычный пользователь без (__dict__) """

    def __init__(self, name: str, email: str, password: str) -> None:
        self.name = name
        self.email = email
        self.password = password


N = 100_000

users = [User(f"user{i}", f"user{i}@mail.com", "pass123") for i in range(N)]
slot_users = [
    SlotUser(f"user{i}", f"user{i}@mail.com", "pass123") for i in range(N)]

# Память одного экземпляра
size_user = sys.getsizeof(users[0])
size_slot_user = sys.getsizeof(slot_users[0])

# У обычного объекта есть ещё и __dict__, который тоже занимает память
size_user_full = size_user + sys.getsizeof(users[0].__dict__)

print(f"Размер одного User (с __dict__):      {size_user_full} байт")
print(f"Размер одного SlotUser (__slots__):    {size_slot_user} байт")
print()

# Суммарная память на 100 000 экземпляров (без учёта общих строк-значений)
total_user = size_user_full * N
total_slot_user = size_slot_user * N

print(
    f"Суммарно {N} объектов User:      {total_user:,} байт (~{total_user / 1024 / 1024:.2f} МБ)")
print(f"Суммарно {N} объектов SlotUser:  {total_slot_user:,} байт (~{total_slot_user / 1024 / 1024:.2f} МБ)")
print()

diff = total_user - total_slot_user
print(f"Экономия за счёт __slots__: {diff:,} байт (~{diff / 1024 / 1024:.2f} МБ), "
      f"это в {total_user / total_slot_user:.2f} раза меньше")
