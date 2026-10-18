
from abc import ABC, abstractmethod


class VehicleInsurance(ABC):
    def __init__(self, owner_name, policy_id, vehicle_value, years):
        self.owner_name = owner_name
        self.__policy_id = policy_id
        self.vehicle_value = vehicle_value
        self.years = years

    def get_policy_id(self):
        return self.__policy_id

    def set_vehicle_value(self, vehicle_value):
        self.vehicle_value = vehicle_value

    def show_policy_details(self):
        print("Owner Name:", self.owner_name)
        print("Policy ID:", self.get_policy_id())
        print("Vehicle Value:", self.vehicle_value)
        print("Insurance Years:", self.years)
        print("Final Premium:", self.calculate_premium())

    @abstractmethod
    def calculate_premium(self):
        pass


class CarInsurance(VehicleInsurance):
    def calculate_premium(self):
        premium = self.vehicle_value * 5 / 100
        final_premium = premium * self.years
        return final_premium


class BikeInsurance(VehicleInsurance):
    def calculate_premium(self):
        premium = self.vehicle_value * 3 / 100
        total_premium = premium * self.years
        final_premium = total_premium + 500
        return final_premium


class CommercialVehicleInsurance(VehicleInsurance):
    def calculate_premium(self):
        premium = self.vehicle_value * 8 / 100
        total_premium = premium * self.years

        if self.years > 3:
            discount = total_premium * 10 / 100
            final_premium = total_premium - discount
        else:
            final_premium = total_premium

        return final_premium


obj1 = CarInsurance("Prateek", 101, 500000, 2)
obj2 = BikeInsurance("Rahul", 102, 100000, 3)
obj3 = CommercialVehicleInsurance("Aman", 103, 1000000, 4)

obj1.set_vehicle_value(600000)

obj1.show_policy_details()
print()

obj2.show_policy_details()
print()

obj3.show_policy_details()
