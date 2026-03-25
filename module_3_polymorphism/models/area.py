import math

class Shape:
    def area(self):
        return 'Undefined area'

class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    circle = Circle(10)
    rectangle = Rectangle(5, 10)
    triangle = Triangle(8, 5)

    for shape in [circle, rectangle, triangle]:
        print(shape.area())