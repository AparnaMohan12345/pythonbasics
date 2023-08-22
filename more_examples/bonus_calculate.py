x = int(input("enter the year of experience"))

if x > 5:
    y = int(input("current salary"))
    inc = y + (y*(5/100))
    print("salary incremented to ", inc)
else:
    print("Not eligible for salary increment")