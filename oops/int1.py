class teacher:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.__salary = salary
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary: ", self.__salary)
class student(teacher):
    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)
       # print("Salary: ", self.__salary) #will not print
t1 = student("Aparna", 26,25000)
t1.show()
