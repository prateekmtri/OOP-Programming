class Employees:
    def __init__(self , Name , salary):
        self.name = Name
        self.salary = salary

obj1= Employees("Rahul" , 30000)
obj2 = Employees("Aman" , 45000)  
      

print("Name: " , obj1.name , "Salary : ", obj1.salary) 
print("Name: " , obj2.name , "Salary : ", obj2.salary)     