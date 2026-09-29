from abc import ABC , abstractmethod

class FoodOrder(ABC):
    def __init__(self , Customer_name , order_id , amount):
        self.customer_id = Customer_name
        self.__order_id = order_id
        self.amount = amount
        
    def get_id(self):
        return self.__order_id
    
    def show_Amount(self):
        print("Your order amount " , self.amount) 
        
    @abstractmethod
    def delivery_type(self):
        pass
    
class Online_order(FoodOrder):
    def delivery_type(self):
        print("Order will be delivered to your address")
    
    
class TakeWay(FoodOrder):
    def delivery_type(self):
        print("Order will be picked up from the restaurant")
        

obj1 = Online_order("Prateek", 101, 500) 
obj2 = TakeWay("Rahul", 102, 300)   

print(obj1.customer_id)  
print(obj1.get_id())
obj1.show_Amount()
obj1.delivery_type() 


print(obj2.customer_id)  
print(obj2.get_id())
obj2.show_Amount()
obj2.delivery_type() 



                   