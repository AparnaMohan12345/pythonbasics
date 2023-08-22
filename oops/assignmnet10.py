"""
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.


"""
class person:
    def getgender(self):
        print("Not defined")
class male(person):
    def getgender(self):
        print("Gender: Male")
class female(person):
    def getgender(self):
        print("Gender: Female")
m= male()
f = female()
m.getgender()
f.getgender()
