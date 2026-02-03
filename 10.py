class Name:
    def __init__(self , name, age):
        self.name = name
        self.age = age
        
    def show_name(self):
        print(f"My name is {self.name}")
        
    def show_age(self):
        print(f"i am {self.age} year old")    
        
obj = Name("Prateek",22)
obj.show_name()
obj.show_age()            
        