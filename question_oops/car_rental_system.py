from abc import ABC , abstractmethod

class CarRental(ABC):
    
    def __init__(self , customer_name , car_number , days , price_per_day):
        self.customer_name = customer_name
        self.__car_number = car_number
        self.days = days
        self.price_per_day = price_per_day
        
        
    def geter_car(self):
        return self.__car_number
    
    def setter(self , price_per_day):
        self.price_per_day = price_per_day
        
    def show_rental_details(self):
        print(self.customer_name)
        print(self.__car_number)
        print(self.price_per_day)
        print(self.days)
        print(self.calculate_rent())
        
    @abstractmethod
    def calculate_rent(self):
            pass
        
class EconomyCar(CarRental):
    def calculate_rent(self):
        return self.days * self.price_per_day
    
    
class SUV(CarRental):
    def calculate_rent(self):
        return self.days * self.price_per_day + 1500
    
    
class LuxuryCar(CarRental):
    def calculate_rent(self):
        return self.days * self.price_per_day + 3000   
    
    
obj1 = EconomyCar("Prateek", 101, 4, 1500)
obj2 = SUV("Rahul", 102, 3, 2500)
obj3 = LuxuryCar("Aman", 103, 2, 5000)   


 
obj1.setter(2000)

obj1.show_rental_details()
print()
print()
obj2.show_rental_details()
print()
print()
obj3.show_rental_details()