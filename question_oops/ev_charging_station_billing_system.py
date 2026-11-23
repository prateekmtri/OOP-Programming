from abc import ABC , abstractmethod
class EVCharging(ABC):
    def __init__(self , owner_name , sestion_id , rate_per_kwh ,  unit_consumed ):
        self.owner_name = owner_name
        self.__sestion_id = sestion_id
        self.rate_per_kwh = rate_per_kwh
        self.unit_consumed = unit_consumed
    def get_session_id(self):
        return self.__sestion_id
    
    def set_units_consumed(self , unit_consumed):
        self.unit_consumed = unit_consumed
        
    def show_charging_details(self):
        print(self.owner_name)
        print(self.get_session_id())
        print(self.rate_per_kwh)
        print(self.unit_consumed)
        print(self.calculate_bill())    
        
    @abstractmethod
    def calculate_bill(self):
        pass
    

class StandardCharging(EVCharging):
    def calculate_bill(self):
        total = self.rate_per_kwh * self.unit_consumed
        return total
    

class FastCharging(EVCharging):
    def calculate_bill(self):
        total = self.rate_per_kwh * self.unit_consumed
        surcharge = total * 30/100
        return total + surcharge
    
           
class FleetCharging(EVCharging):
    def calculate_bill(self):
        total = self.rate_per_kwh * self.unit_consumed
        if self.unit_consumed >= 50:
            dicount = total * 15/100
            return total - dicount
        else:
            return total
        
        
obj1 = StandardCharging("Prateek", 701, 12, 20)
obj2 = FastCharging("Shivam", 702, 15, 30)
obj3 = FleetCharging("Manish", 703, 10, 60)

obj1.set_units_consumed(25)

obj1.show_charging_details()
print()
obj2.show_charging_details()
print()
obj3.show_charging_details()        