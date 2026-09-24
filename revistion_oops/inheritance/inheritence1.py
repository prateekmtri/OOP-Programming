class Person:
    def __init__(self , name):
        self.name = name
        
    def show_name(self):
        print("Name : " , self.name)    
        
class Student(Person):
    pass
        
obj = Student("Prateek")
obj.show_name()

 

              