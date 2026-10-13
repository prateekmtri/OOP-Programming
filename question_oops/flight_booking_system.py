from abc import ABC , abstractmethod
class FlightBooking(ABC):
    def __init__(self, passenger_name , booking_id , ticket_price , number_of_ticket):
        self.passenger_name = passenger_name
        self.__booking_id = booking_id
        self.ticket_prize = ticket_price
        self.number_of_ticket = number_of_ticket
        
    def getter(self):
        return self.__booking_id
    
    def setter(self, ticket_prize):
        self.ticket_prize = ticket_prize
        
    def show_booking_details(self):
        print(self.passenger_name)
        print(self.getter())
        print(self.ticket_prize)
        print(self.number_of_ticket)
        print(self.calclulate_bill())
        
    @abstractmethod
    def calclulate_bill(self):
        pass
    
class EconomyBooking(FlightBooking):
    def calclulate_bill(self):
        final_bill = self.ticket_prize * self.number_of_ticket
        return final_bill
    
class BusinessBooking(FlightBooking):
    def calclulate_bill(self):
        final_bill = self.ticket_prize * self.number_of_ticket + 2000
        return final_bill  
    
class FirstClassBooking(FlightBooking):
    def calclulate_bill(self):
        total_ticket_prize = self.ticket_prize * self.number_of_ticket + 5000
        discount = total_ticket_prize * 10 /100
        final_bill = total_ticket_prize - discount
        return final_bill       
                   

obj1 = EconomyBooking("Prateek", 101, 5000, 2)
obj2 = BusinessBooking("Rahul", 102, 8000, 2)
obj3 = FirstClassBooking("Aman", 103, 15000, 2)   


obj1.setter(6000)

obj1.show_booking_details()
print()
print()
obj2.show_booking_details()
print()
print()
obj3.show_booking_details()                