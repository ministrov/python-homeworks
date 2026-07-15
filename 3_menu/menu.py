""" Домашнее задание по теме управление потоком

    Задача: Спросить у пользователя категорию: «напиток», «суп», «десерт».
        В зависимости от выбора — предложить варианты (например:
            • напиток → «чай», «кофе», «сок»
            • суп → «борщ», «щи», «суп-пюре»
            • десерт → «торт», «мороженое», «фрукты»).

    Пользователь вводит конкретное блюдо.
    Программа с помощью match case выводит цену выбранного блюда.
"""

category = input("Введите категорию: ")
meal = category
meal_price = 0

if meal == "напиток":
    dish = input("Выберите напиток (чай, кофе, сок): ")
    match dish:
        case "чай":
            meal_price = 120
            print(f"Цена выбранного блюда: {meal_price}")
        case "кофе":
            meal_price = 145
            print(f"Цена выбранного блюда: {meal_price}")
        case "сок":
            meal_price = 234
            print(f"Цена выбранного блюда: {meal_price}")
        case _:
            print("Такого напитка нет")

elif meal == "суп":
    dish = input("Выберите суп (борщ, щи, суп-пюре): ")
    match dish:
        case "борщ":
            meal_price = 220
            print(f"Цена выбранного блюда: {meal_price}")
        case "щи":
            meal_price = 245
            print(f"Цена выбранного блюда: {meal_price}")
        case "суп-пюре":
            meal_price = 250
            print(f"Цена выбранного блюда: {meal_price}")
        case _:
            print("Такого супа нет")

elif meal == "десерт":
    dish = input("Выберите десерт (торт, мороженое, фрукты): ")
    match dish:
        case "торт":
            meal_price = 250
            print(f"Цена выбранного блюда: {meal_price}")
        case "мороженое":
            meal_price = 300
            print(f"Цена выбранного блюда: {meal_price}")
        case "фрукты":
            meal_price = 350
            print(f"Цена выбранного блюда: {meal_price}")
        case _:
            print("Такого десерта нет")
