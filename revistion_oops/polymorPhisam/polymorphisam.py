class Vehicle:
    def start(self):
        print("Vehicle is starting")
        
class Car(Vehicle):
    def start(self):
        print("Car is starting with a key") 
        
obj = Vehicle()        
obj2 = Car()

obj.start()
obj2.start()        
              