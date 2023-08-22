"""
Multiply nums in a list using function
"""
import functools
def mult(a,b):
    return a *b

list1=[1,2,3,4,5,6]
result=functools.reduce(mult,list1)
print(result)