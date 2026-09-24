class Person:
    def __init__(self , name):
        self.name = name
        
    def show_name(self):
        print("Name : " , self.name)    
        
class Student(Person):
    def __init__(self,name , course):
        super().__init__(name)
        self.course = course
        
    def show_Course(self):
        print("Course : ", self.course)     
        
obj = Student("Prateek" , "B teach")
obj.show_name()
obj.show_Course()

 

              