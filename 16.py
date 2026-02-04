class Student:
    def __init__(self, name, marks, fees):
        self.name = name
        self._marks = marks
        self.__fees = fees

    def show_inside(self):
        print("Inside class:")
        print(self.name)
        print(self._marks)
        print(self.__fees)

    def show_fees(self):      
        print(self.__fees)


obj = Student("Prateek", 80, 5000)

obj.show_inside()
print(obj.name)
print(obj._marks)

obj.show_fees() 
