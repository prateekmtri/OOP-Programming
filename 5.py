class Age:
    "My age is 45"
    def __init__(self, age):
        self.age = age
        
object = Age(45)
print(object.age)
print(object.__doc__)
        