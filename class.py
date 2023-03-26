from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def area(self):
        result = self.width * self.height
        print(f"My area is {result} meter")


obj = Rectangle(10, 5)
obj.area()
