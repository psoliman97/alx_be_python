import math

class Shape:
    def __init__(self):
        pass
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height, length):
        self.width = width
        self.length = length
    def area(self):
        return self.length , self.length * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius** 2)