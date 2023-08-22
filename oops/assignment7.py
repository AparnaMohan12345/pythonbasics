"""
. Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.


"""
class circle:
    def __init__(self,radius):
        self.radius =radius
    def area(self):
        print("The area of circle: ", 3.14 * self.radius* self.radius)
c1 = circle(4)
c1.area()
