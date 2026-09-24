class Employees:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
        
    def show_emloyees(self):
        print("Name : ", self.name)
        print("Salary : ", self.salary)
        
class Developer(Employees):
    def __init__(self , name , salary , course):
        super().__init__(name , salary)
        self.course = course
        
    def show_langauge(self):
        print("Language : " , self.course)     
        
                    
obj = Developer("Prateek " , 50000 , "Python")
obj.show_emloyees()
obj.show_langauge()        