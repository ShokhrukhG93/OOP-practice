# Import ABC and abstractmethod from the abc module
import math
from abc import ABC, abstractmethod

# Define an abstract base class Shape
class Shape(ABC):
    # Abstract method area, which must be implemented by any subclass
    @abstractmethod
    def area(self) -> None:
        pass

# Define a concrete class Circle inheriting from Shape
class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    # Implementation of the are abstract method
    def area(self):
        return math.pi * self.r ** 2

# Define a concrete class Rectangle inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implementation of the are abstract method
    def area(self):
        return self.width * self.height

# Using the abstract interface
# Create an instance of Circle and call area
circle = Circle(5)
print(f'Area of the circle: {circle.area()}')

# Create an instance of Rectangle and call area
rectangle = Rectangle(4, 6)
print(f'Area of the rectangle: {rectangle.area()}')
