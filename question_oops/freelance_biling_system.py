from abc import ABC , abstractmethod

class ProjectBilling(ABC):
    def __init__(self , clinet_name , project_id , hourely_rate , hour_worked):
        self.clint_name = clinet_name
        self.__project_id = project_id
        self.hourely_rate = hourely_rate
        self.hour_worked = hour_worked
        
    def getter(self):
        return self.__project_id
        
    def setter(self , hour_worked):
        self.hour_worked = hour_worked
        
    @abstractmethod
    def calculate_total(self):
        pass
    
    def show_project_details(self):
        print(self.clint_name)
        print(self.getter())
        print(self.hourely_rate)
        print(self.hour_worked)
        print(self.calculate_total())
        
class StandardProject(ProjectBilling):
    def calculate_total(self):
        total = self.hourely_rate * self.hour_worked
        return total
                

class UrgentProject(ProjectBilling):
    def calculate_total(self):
        total = self.hourely_rate*self.hour_worked
        rush_fee = total*20/100
        final_fee = total + rush_fee
        return final_fee
    
    
class LongTermProject(ProjectBilling):
    def calculate_total(self):
        total = self.hourely_rate * self.hour_worked
        if self.hour_worked >= 40:
              discount = total* 10/100
              return total - discount
        else: 
            return total      
    
    
obj1 = StandardProject("Shivam", 201, 500, 10)
obj2 = UrgentProject("Prateek", 202, 800, 5)
obj3 = LongTermProject("Manish", 203, 600, 50)

obj1.setter(15)

obj1.show_project_details()
print()
obj2.show_project_details()
print()
obj3.show_project_details()               
    
                                