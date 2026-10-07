from abc import ABC , abstractmethod
class HotelBooking(ABC):
    def __init__(self , guest_name , room_number , day , price_per_Day):
        self.guest_name = guest_name
        self.__room_number = room_number
        self.day = day
        self.price_per_day = price_per_Day
        
    def get_function(self):
        return self.__room_number
    
    def set_function(self , price_per_Day):
        self.price_per_day = price_per_Day
        
        
    def show_booking_details(self):
        print(self.guest_name)
        print(self.get_function())
        print(self.day)
        print(self.calculate_bill())    
    
    @abstractmethod
    def calculate_bill(self):
        pass
    
class standard(HotelBooking):
    def calculate_bill(self):
        return self.day*self.price_per_day
        
    
class Deluxe(HotelBooking):
    def calculate_bill(self):
        return self.day*self.price_per_day+ 1000
        
        
class Suite(HotelBooking):
    def calculate_bill(self):
        return self.day*self.price_per_day+ 2000 
        
        
  
obj1 = standard("Prateek", 101, 3, 2000)
obj2= Deluxe("Rahul", 102, 3, 2500)
obj3 = Suite("Aman", 103, 3, 4000) 

obj1.set_function(2500) 


obj1.show_booking_details()
print()
print()
obj2.show_booking_details()
print()
print()
obj3.show_booking_details()             
        
                    