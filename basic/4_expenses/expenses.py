""" Выполнение дз по теме списков и кортежей

    Задача: Создать список из трат за неделю (7 чисел)
            Посчитать сумму, среднее, минимум и максимум.
            Сохранить в кортеже (минимум, максимум, сумма) и вывести его.
"""

flat_rent = 750
mobile_expense = 120
food = 450
clothes = 700
fitness = 340
console_game = 345
going_out = 560

expenses: list[int] = [flat_rent, mobile_expense,
                       food, clothes, fitness, console_game, going_out]

sum_of_expenses = sum(expenses)
average_of_expenses = sum_of_expenses / len(expenses)
min_of_expenses = min(expenses)
max_of_expenses = max(expenses)

result = (min_of_expenses, max_of_expenses, sum_of_expenses)

print(sum_of_expenses)
print(max_of_expenses)
print(min_of_expenses)
print(f"Average of expenses: {average_of_expenses:.2f}")
print(result)
