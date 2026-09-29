from abc import ABC , abstractmethod

class Order(ABC):
    def __init__(self , customer_name , order_id , price):
        self.customer_name = customer_name
        self.__oerder_id = order_id
        self.price = price
        
    def getter_id(self):
        return self.__oerder_id
    
    def show_price(self):
        print("The price is " , self.price) 
        
    @abstractmethod
    
    def orderStatus(self):
        pass
    
class DeliveredOrder(Order):
    def orderStatus(self):
        print("Order has been delivered")
          
        
class CancelledOrder(Order):
    def orderStatus(self):
        print("Order has been cancelled") 
        
        
obj1 = DeliveredOrder("Prateek", 101, 1500)
obj2 = CancelledOrder("Rahul", 102, 800) 

print(obj1.customer_name)
print(obj1.getter_id())
obj1.show_price()
obj1.orderStatus()   

print()

print(obj2.customer_name)
print(obj2.getter_id())
obj2.show_price()
obj2.orderStatus()       
        
                        