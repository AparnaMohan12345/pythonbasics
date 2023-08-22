x = int(input("enter the first num"))
y = int(input("enter the second num"))
z = int(input("enter the third num"))
if x > y and x > z:
    print("The greatest is ", x)
elif y > z:
     print("The greatest is ", y)
else:
    print("the greatest is ", z)