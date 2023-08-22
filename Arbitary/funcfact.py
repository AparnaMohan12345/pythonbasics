def fact(a):
    num = 1
    while a>0:
     num=num*a
     a=a-1
    return(num)


x = fact(5)
print(x)