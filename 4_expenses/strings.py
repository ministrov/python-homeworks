""" Принять строку формата "<руб> руб <коп> коп" (пример: 100 руб 10 коп) и вывести нормализованную сумму в рублях с двумя знаками  после запятой: 100.10 ₽. Поддержать варианты без копеек ("159 руб" → "159.00 ₽").

        Программа читает одну строку из input()
        Регистр и лишние пробелы игнорируются
        Допустимые слова для единиц
        На выходе — сумма в виде X.YY ₽ (два знака после запятой)
        Если формат некорректный — вывести:
        Некорректный формат суммы

"""

user_input = input("Введите строку формата (<руб> руб <коп> коп): ")
formatted = user_input.strip().lower().split()

if 'руб' in formatted:
    index_rub = formatted.index("руб")
    try:
        rubles = int(formatted[index_rub - 1])
    except:
        print("Некорректный формат суммы")
        exit()
else:
    print("Некорректный формат суммы")
    exit()

if 'коп' in formatted:
    index_cop = formatted.index("коп")
    try:
        cop = int(formatted[index_cop - 1])
    except:
        print("Некорректный формат суммы")
        exit()
else:
    cop = 0

total = rubles + cop / 100
print(f"{total:.2f} ₽")
