class Employees:
    def __init__(self ,name , department , salary):
        self.name = name
        self._department = department
        self.__salary = salary
        
    def show_details(self):
        print("Salary : ", self.__salary)
        
obj = Employees("Prateek" , "IT" , 5000)
print("Name : " , obj.name)  
print("Department : " , obj._department) 
obj.show_details()      
        