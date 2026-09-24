class Person:
    def __init__(self , name):
        self.name = name
        
    def show_name(self):
        print("Name : " , self.name)
        
class Student(Person):
    def __init__(self, name , course):
        super().__init__(name)
        self.course = course
        
    def show_Course(self):
        print("Course : " , self.course) 
        
class Employees(Person):
    def __init__(self, name , salary):
        super().__init__(name)
        self.salary = salary
        
    def show_salary(self):
        print("Saalry : ", self.salary) 
        
obj = Student("Prateek" , "Pyhton") 
obj2 = Employees("Rahul" , 50000)

obj.show_name()
obj.show_Course() 

obj2.show_name()
obj2.show_salary()                                