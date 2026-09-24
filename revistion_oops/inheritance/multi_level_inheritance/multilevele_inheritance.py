class Person:
    def __init__(self ,name):
        self.name = name
        
    def show_name(self):
        print("Name : ", self.name)
        
class Employees(Person):
    def __init__(self, name , salary):
        super().__init__(name) 
        self.salary = salary
        
    def show_salary(self):
        print("salary : ", self.salary) 
        
class Developer(Employees):
    def __init__(self ,name , salary , langauage):
        super().__init__(name , salary)
        self.langauege = langauage
    
    def show_langauge(self):
        print("Lnaguage : ", self.langauege)  
        
obj = Developer("Prateek" , 100000 , "Python")
obj.show_name()
obj.show_salary()
obj.show_langauge()                     
                    