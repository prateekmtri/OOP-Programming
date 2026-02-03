class Student:
    def __init__(self, name , age):
        self.name = name
        self.age = age
        
    def show_name(self):
        print(f"My name is {self.name}")
        
        
    def show_age(self):
        print(f"My age is {self.age}")
        
        if self.age >18:
            print("I am adult")
        else:
            print("I am minor") 
               
        
obj = Student("Prateek" , 22)
obj.show_name()
obj.show_age()
        
        