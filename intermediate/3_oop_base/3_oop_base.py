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

from datetime import date


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


class LuxuryRoom(Room):
    def __init__(self, room_number: str | int, price_per_night: int | float, price_multiplier: float):
        super().__init__(room_number, price_per_night)
        self.price_multiplier = price_multiplier

    def get_price(self) -> int | float:
        return self.price_per_night * self.price_multiplier

    def show_info(self) -> str:
        base = super().show_info()
        return (
            f"{base} "
            f"Увеличение цены на: {self.price_multiplier}"
        )


class Booking:
    def __init__(self, room: Room, guest_name: str, date_of_check_in: date, date_of_check_out: date, is_cancelled: bool = False):
        if date_of_check_out <= date_of_check_in:
            raise ValueError("Дата выезда не может быть раньше даты заезда!!!")
        self.room = room
        self.guest_name = guest_name
        self.date_of_check_in = date_of_check_in
        self.date_of_check_out = date_of_check_out
        self.is_cancelled = is_cancelled

    def cancel(self):
        self.is_cancelled = True


class Hotel:
    def __init__(self, hotel_name: str):
        self.hotel_name = hotel_name
        self.rooms: list[Room] = []
        self.bookings: list[Booking] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def show_booked_rooms(self):
        actives = [
            active for active in self.bookings if not active.is_cancelled]

        for active in actives:
            print(
                f"номер гостя: {active.guest_name} "
                f"дата въезда: {active.date_of_check_in} "
                f"дата выезда: {active.date_of_check_out}"
            )

    def list_available_rooms(self, date_from: date, date_to: date) -> list[Room]:
        return [
            room for room in self.rooms
            if self._is_room_available(room, date_from, date_to)
        ]

    def _is_room_available(self, room: Room, date_from: date, date_to: date) -> bool:
        for booking in self.bookings:
            if booking.is_cancelled:
                continue
            if booking.room is not room:
                continue
            if booking.date_of_check_in < date_to and booking.date_of_check_out > date_from:
                return False
        return True

    def book_room(self, room: Room, guest_name: str, date_from: date, date_to: date) -> Booking:
        if not self._is_room_available(room, date_from, date_to):
            raise ValueError("Номер не доступен")
        booking = Booking(room, guest_name, date_from, date_to)
        self.bookings.append(booking)
        return booking


if __name__ == "__main__":
    room = Room("12", 12.40)
    luxury_room = LuxuryRoom("23", 23, 1.5)

    print(room.show_info())
    print(luxury_room.show_info())
