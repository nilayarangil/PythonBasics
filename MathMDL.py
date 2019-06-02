import math

# This class only does basic math operations on a list of numbers
class MathMDL:
    def __init__(self):
        self.numbers = []
     # Method adds the list of numbers passed   
    def Add(self):
        c1 = 0
        for n in self.numbers:
            c1 = c1 + float(n) 
        return c1
    # Method multiplies all the numbers in the list 
    def Multiply(self):
        c1 = 1
        for n in self.numbers:
            c1 = c1 * float(n)
        return c1
    # Method substracts the first two numbers in the list passed
    def Subtract(self):
        if len(self.numbers) > 2 or len(self.numbers) <= 1:
            print("Error calculating difference. Please pass only two numbers.") 
        elif len(self.numbers) == 2:
            return float(self.numbers[0])-float(self.numbers[1])        
    # Method divides the first two numbers in the list
    def Divide(self):
        if len(self.numbers) > 2 or len(self.numbers) <= 1:
            print("Error dividing. Please pass only two numbers.") 
        elif len(self.numbers) == 2:
             return float(self.numbers[0])/float(self.numbers[1])

# This class defines a cricle and attributes and methods of a circle
class Circle:
    def __init__(self):
        self.radius = 0
    def GetArea(self):
        return math.pi * self.radius * self.radius
        
# Define class for rectangle and have square class inherit from it.
class Rectangle:
    def __init__(self):
        self.length = 0
        self.width = 0
    def GetArea(self):
        return self.length * self.width
    def GetPerimeter(self):
        return (self.length + self.width) * 2
 
class Square(Rectangle):
    def __init__(self):
        Rectangle.__init__(self)
    def GetSquareArea(self):
        return self.length * self.length
    def GetSquarePerimeter(self):
        return self.length *4

       
# Define class for Cylinder. it should have one method GetVolume
class Cylinder(Circle):
    def __init__(self):
        Circle.__init__(self)
        self.height = 0      
        
    def GetCylinderVolume(self):
        return math.pi * self.radius * self.radius * self.height
    def GetCylinderSurfaceArea(self):
        return (math.pi * self.radius * self.radius * 2)+((math.pi * (self.radius *2)) * self.height) 
    
# Define triangle. It should have method GetArea,Perimeter
class Triangle():
    def __init__(self):
        self.side1 = 0
        self.side2 = 0
        self.side3 = 0
        self.base = 0
        self.height = 0 
    
    def GetPerimeter(self):
        return self.side1 + self.side2 + self.side3
    def GetArea(self):
        return self.base * self.height / 2 
# Define Temperture class. attributes should be celcius,farenheat. Methods mustbe ConvertToCelcius
# and ConvertToFarenheats
        
        