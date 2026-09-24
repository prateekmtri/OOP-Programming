from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog barks")
        
class Cat(Animal):
    def sound(self):
        print("cat meow") 
        
        
obj = Dog()
obj2 = Cat()

obj.sound()
obj2.sound()               
            