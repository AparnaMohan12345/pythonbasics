"""
 Write a Program to create a class and, using the class instance, print all the writable attributes of that object.
"""
class staff:
    def __init__(self, num):
        self.num = num

    def show(self):
        print(self.num)
        print(self.class1)


class teacher(staff):
    def __init__(self, class1):
        self.class1 = class1
        super().__init__(4)


obj1 = teacher(3)
print(obj1.__dict__)
