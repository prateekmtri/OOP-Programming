class Vehicle:
    def __init__(self , brand):
        self.brand = brand
        
    def show_name(self):
        print("Name : " , self.brand)    
        
class Car(Vehicle):
    pass
        
obj = Car("Toyota")
obj.show_name()
