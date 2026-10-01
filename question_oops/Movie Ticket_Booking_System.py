from abc import ABC , abstractmethod
class Booking(ABC):
    def __init__(self , customer_name , booking_id , ticket_price):
        self.customer_name = customer_name
        self.__booking_id = booking_id
        self.ticket_price = ticket_price
        
    def get_booking(self):
        return self.__booking_id
    
    def show_price(self):
        print("Ticket prize is " ,self.ticket_price)
        
    @abstractmethod
    def booking_type(self):
        pass
    
class RegularBooking(Booking):
    def booking_type(self):
        print("Regular Movie Booking")
    
class VIPBooking(Booking):
    def booking_type(self):
     print("VIP Movie Booking")
     

obj1 = RegularBooking("Prateek", 101, 250)
obj2 = VIPBooking("Rahul", 102, 800)   

print(obj1.customer_name)
print(obj1.get_booking())
obj1.show_price()
obj1.booking_type() 

print() 
print()


print(obj2.customer_name)
print(obj2.get_booking())
obj2.show_price()
obj2.booking_type()