from abc import ABC,abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length:float,width:float):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area is {self.length*self.width}")


r = Rectangle(2,3)
r.area()
