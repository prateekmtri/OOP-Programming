from abc import ABC , abstractmethod
class WarehouseStorage(ABC):
    def __init__(self , client_name , storage_id , rate_per_day , day_stored):
        self.client_name = client_name
        self.__storage_id = storage_id
        self.rate_per_day = rate_per_day
        self.day_stored = day_stored
    
    def get_storage_id(self):
        return self.__storage_id
    
    def set_day_stored(self , day_stored):
        self.day_stored = day_stored
    
    def show_storage_details(self):
        print("Client Name  : ", self.client_name)
        print("Storage Id :  ", self.get_storage_id())
        print("Rate Per day : ", self.rate_per_day)
        print("Day Stored : ", self.day_stored)
        print("Final Total : " , self.calculate_storage_fee())    
        
    
    @abstractmethod
    def calculate_storage_fee(self):
        pass
    
class GeneralStorage(WarehouseStorage):
    def calculate_storage_fee(self):
        total = self.rate_per_day * self.day_stored
        return total
    
class ColdStorage(WarehouseStorage):
    def calculate_storage_fee(self):
        total = self.rate_per_day * self.day_stored
        surcharge = total * 25/100
        return total + surcharge
    
class LongTermStorage(WarehouseStorage):
    def calculate_storage_fee(self):
        total = self.rate_per_day * self.day_stored
        if self.day_stored >= 30:
            discount = total*15/100
            return total - discount
        else:
            return total
        
        
obj1 = GeneralStorage("Prateek", 801, 200, 10)
obj2 = ColdStorage("Shivam", 802, 400, 10)
obj3 = LongTermStorage("Manish", 803, 300, 40)

obj1.set_day_stored(15)

obj1.show_storage_details()
print()
obj2.show_storage_details()
print()
obj3.show_storage_details()        