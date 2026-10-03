from abc import ABC , abstractmethod

class Ride(ABC):
    def __init__(self , passenger_name , distance , ride_id):
        self.passenger_name = passenger_name
        self.distance = distance
        self.__ride_id = ride_id
    def getter(self):
        return self.__ride_id
    
    def show_ride_details(self):
        print("Passenger name : " , self.passenger_name)
        print("Ride_id : " , self.getter())
        print("Distance : ", self.distance) 
        print("Fare" , self.calculate_fare())
        
    @abstractmethod
    def calculate_fare(self):
        pass
    
class Bike_ride(Ride):
    def calculate_fare(self):
        return self.distance*10 
        
        
class Car_ride(Ride):
    def calculate_fare(self):
         return self.distance*20   
        
class Premimum_ride(Ride):
    def calculate_fare(self):
         return self.distance*40
        
        
        
obj1 = Bike_ride("Prateek", 10, 101)
obj2 = Car_ride("Rahul", 10, 102)
obj3 = Premimum_ride("Aman", 10, 103)


obj1.show_ride_details()
print()

obj2.show_ride_details()

print()

obj3.show_ride_details()        
        
        
                       