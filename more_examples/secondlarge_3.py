x = int(input("Enter the First num "))
y = int(input("Enter the second num "))
z = int(input("Enter the Third num "))
if x > y and x > z:
    if y>z:
     print(y, " is the second largest")
    else:
        print(z, " is the second largest")
elif y>z and y>x:
    if z>x:
        print(z, " is the second largest")
    else:
        print(x, " is the second largest")
elif x>y:
    print(x, " is the second largest")
else:
    print(y, " is the second largest")


