"""
Write a program to create a child class Teacher that will inherit the properties of Parent class Staff
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
obj1.show()
