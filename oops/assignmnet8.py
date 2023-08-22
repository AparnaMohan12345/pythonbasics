"""
. Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method

"""
class rectangle:
    def __init__(self,len,brdth):
        self.len=len
        self.brd =brdth
    def area(self):
        print("Area of rectangle: ",self.len *self.brd)
r1 = rectangle(4,2)
r1.area()