"""
The circle class models a circle with a radius and color

attributes : radius , color

methods :

Circle
getRadius()
getCircumference()
getArea()
"""


class circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def getarea(self):
        print("Area of circle: ", 3.14 * (self.radius * self.radius))

    def getcircumference(self):
        print("Perimeter of circle: ", (2 * 3.14) * self.radius)

    def getradius(self):
        self.radius = int(input("Enter the radius:"))


c1 = circle(10, 'red')
c1.getradius()
c1.getarea()
c1.getcircumference()
