from abc import ABC , abstractmethod
class CloudStorage(ABC):
    def __init__(self ,user_name , account_id , price_per_gb , storage_gb):
        self.name = user_name
        self.__id = account_id
        self.price_gb = price_per_gb
        self.storage_gb = storage_gb
        
    def get_account_id(self):
        return self.__id
    
    def set_storage_gb(self , storage_gb):
        self.storage_gb = storage_gb 
        
    def show_subscription_details(self):
        print(self.name)
        print(self.get_account_id())
        print(self.price_gb)
        print(self.storage_gb)
        print(self.calculate_bill())      
        
    @abstractmethod
    def calculate_bill(self):
        pass
class PersonalPlan(CloudStorage):
    def calculate_bill(self):
        total = self.price_gb * self.storage_gb
        return total
    
class ProPlan(CloudStorage):
    def calculate_bill(self):
        total = self.price_gb * self.storage_gb
        if self.storage_gb >= 100:
            discount = total * 15/100
            return total - discount
        else:
            return total          
    
class EnterprisePlan(CloudStorage):
    def calculate_bill(self):
        total = self.price_gb * self.storage_gb
        discount = total*25/100
        dedicated_support = 500
        final = (total - discount) + dedicated_support
        return final 
    
    
obj1 = PersonalPlan("Prateek", 501, 20, 50)
obj2 = ProPlan("Shivam", 502, 15, 120)
obj3 = EnterprisePlan("Manish", 503, 10, 500)

obj1.set_storage_gb(60)

obj1.show_subscription_details()
print()
obj2.show_subscription_details()
print()
obj3.show_subscription_details()      
    
    
    
             
        