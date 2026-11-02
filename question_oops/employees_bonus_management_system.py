from abc import ABC , abstractmethod

class Employee(ABC):
    def __init__(self , name , employees_id , basic_salary):
        self.name = name
        self.__employees_id = employees_id
        self.basic_salary = basic_salary
        
    def getter(self):
        return self.__employees_id
    
    def setter(self , basic_salary):
        self.basic_salary = basic_salary
        
    def show_details(self):
        print("Name : ", self.name)
        print("ID : ",self.getter())
        print("Salary : ",self.basic_salary)  
        print("Bonus : ",self.calculate_bonus())  
    
    
    @abstractmethod
    def calculate_bonus(self):
        pass
    
    
class Developer(Employee):
    def calculate_bonus(self):
        bonus = self.basic_salary*15//100
        return bonus
    
class  Manager(Employee):
    def calculate_bonus(self):
        M_Bonus = self.basic_salary*25//100
        return M_Bonus
    
obj1 = Developer("Prateek", 101, 50000)
obj2 = Manager("Rahul", 102, 80000)

obj1.setter(60000)

obj1.show_details()
print()
print()
obj2.show_details()            
    
            