class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length *self.width
    def perimeter(self):
        return 2*(self.length*self.width)
    @classmethod
    def create_square(cls,side):    
        return cls(side,side)

r1 = rectangle(7,6)
print(r1.area())
print(r1.perimeter())

s1 = rectangle.create_square(4)
print(s1.area())
print(s1.perimeter())