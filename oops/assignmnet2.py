"""
1. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

"""

class string:
    def __init__(self,string1):
        self.string1 = string1
    def getstring(self):
        self.string1 = input("enter a string: ")
    def printstring(self):
        print("string is :",self.string1.upper())
    def testmethod(self):
        print("test the class methods")
str1 = string("aparna")
str1.getstring()
str1.printstring()
str1.testmethod()