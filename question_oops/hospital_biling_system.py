from abc import ABC , abstractmethod

class Hospital_patience(ABC):
    def __init__(self , patient_name , patient_id , day_admited , daily_charge):
        self.patient_name = patient_name
        self.__patient_id = patient_id
        self.day_admitted = day_admited
        self.daily_charges = daily_charge
        
    def getter(self):
        return self.__patient_id
    
    def setter(self , daily_charges):
        self.daily_charges = daily_charges
        
    def show_bill_details(self):
        print(self.patient_name)
        print(self.getter())
        print(self.day_admitted)
        print(self.daily_charges)
        print(self.calulate_bill())        
        
    @abstractmethod
    def calulate_bill(self):
        pass
    
class General_patient(Hospital_patience):
    def calulate_bill(self):
        final_bill = self.day_admitted * self.daily_charges
        return final_bill       
    
class ICUPatient(Hospital_patience):
    def calulate_bill(self):
        final_bill = self.day_admitted * self.daily_charges + 5000
        return final_bill    
    

class EmergencyPatien(Hospital_patience):
    def calulate_bill(self):
        total_price = self.day_admitted * self.daily_charges + 2000
        discount = total_price* 5/100
        final_bill = total_price - discount
        return final_bill    
    
obj1 = General_patient("Prateek", 101, 3, 2000)
obj2 = ICUPatient("Rahul", 102, 2, 5000)
obj3 = EmergencyPatien("Aman", 103, 4, 1500)   


obj1.setter(2500)

obj1.show_bill_details()
print()
print()
obj2.show_bill_details()
print()
print()
obj3.show_bill_details() 