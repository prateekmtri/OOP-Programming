from abc import ABC , abstractmethod

class ShoppingCart(ABC):
    def __init__(self , customer_name , customer_id , product_price , quantity):
        self.customer_name = customer_name
        self.__customer_id = customer_id
        self.product_price = product_price
        self.quantity = quantity
        
    def getter(self):
        return self.__customer_id  
    
    def setter(self , quantity):
        self.quantity = quantity
        
    def  show_cart_details(self):
        print(self.customer_name)
        print(self.getter())
        print(self.product_price)
        print(self.quantity)
        print(self.calculate_total())
            
        
    @abstractmethod
    def calculate_total(self):
        pass
    
class RegularCustomer(ShoppingCart):
    def calculate_total(self):
        total = self.product_price * self.quantity
        return total
     

    
class PremiumCustomer(ShoppingCart):
    def calculate_total(self):
        total = self.product_price * self.quantity
        if total > 5000:
            final_total = total - (total * 10 / 100)
        else:
            final_total = total
            
        return final_total
    
class WholesaleCustomer(ShoppingCart):
    def calculate_total(self):
        total = self.product_price * self.quantity
        if self.quantity >= 10:
            final = total - (total*15/100)
        else:
            final = total
        return final           
                
             
    
obj1 = RegularCustomer("Prateek", 101, 1000, 4)
obj2 = PremiumCustomer("Rahul", 102, 1500, 4)
obj3 = WholesaleCustomer("Aman", 103, 800, 12)

obj1.setter(6)

obj1.show_cart_details()
print()
obj2.show_cart_details()
print()
obj3.show_cart_details()    
    
        
          
        