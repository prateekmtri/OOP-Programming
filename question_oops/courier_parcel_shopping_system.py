from abc import ABC , abstractmethod

class ParcelShipping(ABC):
    def __init__(self , sender_name , tracking_id , rate_per_kg , weight_kg):
        self.sender_name = sender_name
        self.__tracking_id = tracking_id
        self.rate_per_kg = rate_per_kg
        self.weight_kg = weight_kg
        
    def get_tracking_id(self):
        return self.__tracking_id
    
    def set_weight_kg(self , weight_kg):
        self.weight_kg = weight_kg
    
    def show_shipping_details(self):
        print(self.sender_name)
        print(self.get_tracking_id())
        print(self.rate_per_kg)
        print(self.weight_kg)
        print(self.calculate_shipping_cost())
        
    @abstractmethod
    def calculate_shipping_cost(self):
        pass
    
class StandardShipping(ParcelShipping):
    def calculate_shipping_cost(self):
        total = self.weight_kg * self.rate_per_kg
        return total
    
    
class ExpressShipping(ParcelShipping):
    def calculate_shipping_cost(self):
        total = self.weight_kg * self.rate_per_kg
        surcharge = total * 25/100
        return total + surcharge
    

class BulkShipping(ParcelShipping):
    def calculate_shipping_cost(self):
        total = self.weight_kg * self.rate_per_kg
        discount = total * 20/100
        if self.weight_kg >= 20:
            return total - discount
        return total
        
obj1 = StandardShipping("Prateek", 601, 50, 4)
obj2 = ExpressShipping("Shivam", 602, 80, 5)
obj3 = BulkShipping("Manish", 603, 40, 25)

obj1.set_weight_kg(6)

obj1.show_shipping_details()
print()
obj2.show_shipping_details()
print()
obj3.show_shipping_details()        
        
           
            