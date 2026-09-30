from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self , name , person_id, cource):
        self.name  = name
        self.__person_id = person_id
        self.cource = cource
    
    def get_perosn(self):
        return self.__person_id
    
    def show_cource(self):
        print("Your cource is " , self.cource)
        
        
    @abstractmethod
    def role(self):
        pass
    
class Student(Person):
    def role(self):
        print("I am student")   
        
class Professor(Person):
    def role(self):
        print("i am professor")  
        

ob1 = Student("Prateek", 101, "Computer Science")
ob2 = Professor("Rahul", 102, "Data Structures")  

print(ob1.name)
print(ob1.get_perosn())
ob1.show_cource()
ob1.role()                    

print()

print(ob2.name)
print(ob2.get_perosn())
ob2.show_cource()
ob2.role()