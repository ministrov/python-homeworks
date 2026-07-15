""" Домашнее задание по теме операторы

    Задача: Калькулятор скидки. Спросить у пользователя цену товара.
    Спросить процент скидки. Посчитать и вывести цену со скидкой.
"""
price = int(input("Введите цену товара: "))
discount_percent = int(input("Введите процент скидки: "))

final_price = price - (price * discount_percent / 100)

print(f"Исходная цена: {price} руб")
print(f"Скидка: {discount_percent}%")
print(f"Финальная цена: {final_price:.2f} руб")