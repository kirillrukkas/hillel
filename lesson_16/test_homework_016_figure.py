from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)

class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2
    
    def perimeter(self):
        return 4*self.width

class TestsClasses:

    def test_circle(self):
        radius = 5
        circle = Circle(radius)


        # print("Rectangle Area:", rectangle.area())   # Output: 24
        
        assert circle.area() == math.pi*radius**2, "Unexpected area for Circle"
        assert circle.perimeter() == 2*math.pi*radius, "Unexpected perimeter for Circle"
    
    def test_rectangle(self):
        width = 4
        height = 6
        rectangle = Rectangle(width, height)
        
        assert rectangle.area() == width * height, "Unexpected area for Rectangle"
        assert rectangle.perimeter() == 2*(width + height), "Unexpected perimeter for Circle"
    
    def test_square(self):
        a = 5
        square = Square(a)
        
        assert square.area() == a**2, "Unexpected area for Square"
        assert square.perimeter() == 4*a, "Unexpected perimeter for Square"


        



