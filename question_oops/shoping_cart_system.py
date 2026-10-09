from abc import ABC , abstractmethod

class Product(ABC):
    def __init__(self , Product_name , product_id , quantity , price):
        self.product_name = Product_name
        self.__product_id = product_id
        self.quantity = quantity
        self.price = price
    def getter(self):
        return self.__product_id
    
    def setter(self , price):
        self.price = price
        
    def show_product_details(self):
        print(self.product_name)
        print(self.getter())
        print(self.quantity)
        print(self.price)
        print(self.calculate_bill())
        
    @abstractmethod
    def calculate_bill(self):
        pass
    
class RegularProduct(Product):
    def calculate_bill(self):
        final_bill =  self.quantity * self.price
        return final_bill 
    
class DiscountProduct(Product):
    def calculate_bill(self):
        total_price = self.quantity * self.price
        discount = total_price*10/100
        final_bill = total_price - discount
        return final_bill
    
           
class PremiumProduct(Product):
    def calculate_bill(self):
        total_price = self.quantity * self.price
        discount = total_price*20/100
        final_bill = total_price - discount + 500
        return final_bill
    
    
    
obj1 = RegularProduct("Keyboard", 101, 2, 1000)
obj2 = DiscountProduct("Mouse", 102, 3, 500)
obj3 = PremiumProduct("Monitor", 103, 2, 5000) 

obj1.setter(1200)

obj1.show_product_details()
print()
print()

obj2.show_product_details()
print()
print()
obj3.show_product_details()   
               
        
                 