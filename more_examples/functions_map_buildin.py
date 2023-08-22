"""
map function
map(functions,iterable)
lambda arguments:expression
"""
from functools import reduce


def myfun(a,b):
    return(a+b)

a=['one','two']
b =['three','four']
x= list(map(myfun,a,b))
print(x)

num1 = [1,2,3]
num2 =[4,5,6]
result = map(lambda x,y:x+y, num1,num2)
print(list(result))

"""
Filter
filter(function,iterables)
"""
num = range(-5,5)
less = list(filter(lambda x:x<0,num))
print(less)

num2=[-3,-6,-5,2,5,6,-2]
less1 = list(filter(lambda x:x<0,num2))
print(less1)

"""
Reduce
1.import reduce
"""

list1 =[1,3,4,6]
prod = reduce((lambda x,y:x*y),[1,3,4,6])
print(prod)

n= range(1,10)

sum = reduce((lambda x,y: x+y),n)
print(sum)
