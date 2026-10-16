
from abc import ABC, abstractmethod


class HotelGuest(ABC):
    def __init__(self, guest_name, guest_id, nights, price_per_night):
        self.guest_name = guest_name
        self.__guest_id = guest_id
        self.nights = nights
        self.price_per_night = price_per_night

    def get_guest_id(self):
        return self.__guest_id

    def set_price_per_night(self, price_per_night):
        self.price_per_night = price_per_night

    def show_bill_details(self):
        print("Guest Name:", self.guest_name)
        print("Guest ID:", self.get_guest_id())
        print("Nights:", self.nights)
        print("Price Per Night:", self.price_per_night)
        print("Final Bill:", self.calculate_bill())

    @abstractmethod
    def calculate_bill(self):
        pass


class StandardGuest(HotelGuest):
    def calculate_bill(self):
        return self.nights * self.price_per_night


class VIPGuest(HotelGuest):
    def calculate_bill(self):
        room_cost = self.nights * self.price_per_night
        total_cost = room_cost + 1500
        discount = total_cost * 10 / 100
        final_bill = total_cost - discount
        return final_bill


class CorporateGuest(HotelGuest):
    def calculate_bill(self):
        room_cost = self.nights * self.price_per_night

        if self.nights > 5:
            final_bill = room_cost - (room_cost * 15 / 100)
        else:
            final_bill = room_cost

        return final_bill


obj1 = StandardGuest("Prateek", 101, 3, 2000)
obj2 = VIPGuest("Rahul", 102, 4, 3000)
obj3 = CorporateGuest("Aman", 103, 7, 2500)

obj1.set_price_per_night(2500)

obj1.show_bill_details()
print()

obj2.show_bill_details()
print()

obj3.show_bill_details()
