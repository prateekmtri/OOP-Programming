from abc import ABC , abstractmethod

class Vehicle(ABC):
    def __init__(self , brand , vehical_number , rent):
        self.brand  = brand
        self.__vehical_number = vehical_number
        self.rent = rent
        
    def get_vehical(self):
        return self.__vehical_number
    
    def show_rent(self):
        print("your rent is  " , self.rent) 
        
    @abstractmethod
    def vehicle_type(self):
        pass
    
class Car(Vehicle):
    def vehicle_type(self):
        print("This is a car " , self.brand)
        
class Bike(Vehicle):
    def vehicle_type(self):
        print("This is a bike " , self.brand) 
        
ob1 = Car("Toyota", 101, 2000)
obj2 = Bike("Honda", 102, 1000) 

print("Brand : " , ob1.brand)
print("Vehical Number : " , ob1.get_vehical())
print("Rent : " , ob1.rent) 
ob1.vehicle_type()


print("Brand : " , obj2.brand)
print("Vehical Number : " , obj2.get_vehical())
print("Rent : " , obj2.rent)
obj2.vehicle_type()