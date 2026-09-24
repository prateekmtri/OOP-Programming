# Paramerterized Constructor

class Student:
    def __init__(self , name , age , branch):
        self.name = name
        self.age = age
        self.branch = branch

obj1 = Student("Prateek" , 22 , "CSE")
print("Name : ", obj1.name )
print("Age : ", obj1.age )
print("Branch : ", obj1.branch )    
        