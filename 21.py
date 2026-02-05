class Vehicle:
    def __init__(self, brand , fuel):
        self.brand = brand
        self.__fuel = fuel
        
    def show_info(self):
        print(f"Brand : {self.brand}")
        print(f"fuel : {self.__fuel}")
    
    def use_fuel(self , km):
        if self.__fuel >= km:
            self.__fuel = self.__fuel-km
            print("Reduce fuel")
        else:
            print("Not enough fuel")
            
            
           
                
        
class Bike(Vehicle):
    def ride(self , km):
        self.use_fuel(km)

            
class Car(Vehicle):
    def drive(self , km):
        self.use_fuel(km*2) 
            
            
b = Bike("Honda", 50)
c = Car("Tata", 50)

b.show_info()
b.ride(20)
b.show_info()

c.show_info()
c.drive(20)
c.show_info()                          
        