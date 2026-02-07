from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        print(f"Square area: {self.side * self.side}")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(f"Rectangle area: {self.length * self.breadth}")


s = Square(4)
r = Rectangle(5, 3)

s.area()
r.area()
