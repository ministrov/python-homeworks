""" Модуль для выполнения дз по теме ООП (базовый уровень)

    Задача: Реализовать техническое задание ниже.

    ТЕХ. ЗАДАНИЕ:
        У нас есть отель, в котором есть номера разных типов (от Room):
        Обычный номер
        Люкс (имеет мультипликатор цены)
        Гость может:
        бронировать номер на определённые даты - через класс Booking - бронирование. Его можно отменить.
        Отель (класс Hotel) должен:
        уметь показывать список доступных номеров на заданные даты;
        добавить номер
        забронировать и отменить бронирование
        показать забронированные номера
"""


class Room:
    """ Комната в отеле """

    def __init__(self, room_number: str | int, price_per_night: int | float):
        if price_per_night < 0:
            raise ValueError("Цена за ночь не может быть отрицательной")
        self.room_number = room_number
        self.price_per_night = price_per_night

    def get_price(self) -> int | float:
        return self.price_per_night

    def show_info(self) -> str:
        return (
            f"Номер комнаты: № {self.room_number} "
            f"Цена за ночь: {self.price_per_night}"
        )
