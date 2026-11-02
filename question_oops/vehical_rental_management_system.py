from abc import ABC , abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_name , vehicle_id , rent_per_day , days):
        self.vehicle_name = vehicle_name
        self.__vehicle_id = vehicle_id
        self.rent_per_day = rent_per_day
        self.days = days
        
    def getter(self):
        return self.__vehicle_id
    
    def setter(self , rent_per_day):
        self.rent_per_day = rent_per_day
        
    def show_details(self):
        print(self.vehicle_name)
        print(self.getter())
        print(self.rent_per_day)
        print(self.days)
        print(self.calculate_rent())    
        
    
    @abstractmethod
    def calculate_rent(self):
        pass
    
class Car(Vehicle):
    def calculate_rent(self):
        total_rent = self.rent_per_day*self.days
        return total_rent 
    
class Bike(Vehicle):
    def calculate_rent(self):
        total_rent = self.rent_per_day*self.days+ 200
        return total_rent   
    
    
obj1 = Car("BMW", 101, 3000, 4)
obj2 = Bike("Royal Enfield", 102, 1000, 3)

obj1.setter(3500)

obj1.show_details()
print()
print()
obj2.show_details()        
            