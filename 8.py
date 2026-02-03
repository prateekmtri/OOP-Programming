class Age:
    "This is my age class"
    def __init__(self , age):
        self.age = age
        
    def show_age(self):
        print(f"My age is {self.age}")
        
        
obj = Age(45)
obj.show_age()        
        