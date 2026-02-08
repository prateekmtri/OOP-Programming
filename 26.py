from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass



class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"Dog {self.name} says Bark")



class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"Cat {self.name} says Meow")



d = Dog("Tommy")
c = Cat("Kitty")

d.sound()
c.sound()
