from abc import ABC , abstractmethod

class HospitalPatient(ABC):
    def __init__(self , patient_name , patient_id , day_admitted , room_charge_per_day):
        self.patient_name = patient_name
        self.__patient_id = patient_id
        self.day_admitted = day_admitted
        self.room_charge_per_day = room_charge_per_day
        
    def getter(self):
        return self.__patient_id
    
    def setter(self , room_charge_per_day):
        self.room_charge_per_day = room_charge_per_day
        
    def show_details(self):
        print(self.patient_name)
        print(self.getter())
        print(self.day_admitted)
        print(self.room_charge_per_day)
        print(self.calculate_bill())    
        
    @abstractmethod
    def calculate_bill(self):
        pass        
    
class GeneralPatient(HospitalPatient):
    def calculate_bill(self):
        total_bill = self.day_admitted * self.room_charge_per_day
        return total_bill
        
        
class EmergencyPatient(HospitalPatient):
    def calculate_bill(self):
        total_bill = self.day_admitted * self.room_charge_per_day + 2000
        return total_bill
    
obj1 = GeneralPatient("Prateek", 101, 3, 2000)
obj2 = EmergencyPatient("Rahul", 102, 4, 3000)

obj1.setter(2500)

obj1.show_details()
print()
obj2.show_details()    
                
        