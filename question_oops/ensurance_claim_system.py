from abc import ABC , abstractmethod

class InsuranceClaim(ABC):
    def __init__(self, customer_name , claim_id , reapair_cost , damage_level):
        self.customer_name = customer_name
        self.__claim_id = claim_id
        self.repair_cost = reapair_cost
        self.damage_level = damage_level
        
    def getter(self):
        return self.__claim_id
    
    def setter(self , repair_cost):
        self.repair_cost = repair_cost
        
    def show_claim_details(self):
        print(self.customer_name)
        print(self.getter())
        print(self.repair_cost)
        print(self.damage_level) 
        print(self.claculate_payout())        
        
    @abstractmethod
    def claculate_payout(self):
        pass
    
class BasicClaim(InsuranceClaim):
    def claculate_payout(self):
        final_payout = self.repair_cost * 80/100
        return final_payout  
    
class PremiumClaim(InsuranceClaim):
    def claculate_payout(self):
        pay = self.repair_cost * 100/100
        didcut = 1000
        final_payout = pay - didcut
        return final_payout
    
    
class AccidentClaim(InsuranceClaim):
    def claculate_payout(self):
        pay = self.repair_cost * 90/100
        if self.damage_level == "high":
            final_payout = pay + 2000
        else:
            final_payout = pay     
        return final_payout   
    
    
    
obj1 = BasicClaim("Prateek", 101, 10000, "low")
obj2 = PremiumClaim("Rahul", 102, 20000, "medium")
obj3 = AccidentClaim("Aman", 103, 30000, "high")

obj1.setter(12000)   

obj1.show_claim_details()
print()
print()
obj2.show_claim_details()
print()
print()
obj3.show_claim_details()              