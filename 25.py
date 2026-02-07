from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    

class Square(Shape):
    def   area(self , side):
        self.side = side*side
        print("Your side is : {self.side}")
        
        
class Rectangle(Shape):
    def area(self, length , breath):
        self.total = length*breath
        print("Rectangle area : {self.total}")
        
        
        
s = Square()
R = Rectangle()

        
                         