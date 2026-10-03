from abc import ABC , abstractmethod


class Payment(ABC):
    def __init__(self ,customer_name , amount , transictiion_id):
        self.customername = customer_name
        self.amount = amount
        self.__transcition_id = transictiion_id
        
    def getter(self):
        return self.__transcition_id
    
    def show_details(self):
        print(self.customername)
        print(self.getter())
        print(self.amount)
        print(self.payment_status())

        
    @abstractmethod
    def payment_status(self):
        pass
    
class Credit_card(Payment):
    def payment_status(self):
        print("Payment successful through Credit Card")            
        
class UPI(Payment):
    def payment_status(self):
        return "Payment successful through UPI"        
        
        
class Cash_on_delivery(Payment):
    def payment_status(self):
        return "Payment will be collect through delvivery"
        


obj1 = Credit_card("Prateek", 1500, 101)
obj2= UPI("Rahul", 800, 102)
obj3 = Cash_on_delivery("Aman", 1200, 103)

obj1.show_details()

print()

obj2.show_details()



print()


obj3.show_details()


                