import math
class shape:
    def area(self):
        pass

class Circle(shape):
    def __init__(self,r):
        self.r=r
    
    def area(self):
        return math.pi*self.r*self.r
    
class Rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    def area(self):
        return self.l*self.b

class Triangle(shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        return 0.5 * self.base * self.height
    
Circle=Circle(5)
Rectangle=Rectangle(2,4)
Triangle=Triangle(5,10)

print("Area of circle",Circle.area())
print("Area of Rectangle",Rectangle.area())
print("Area of triangle",Triangle.area())