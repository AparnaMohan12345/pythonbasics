x = int(input("Enter the year"))
if x%400 == 0:
    print("year is leap year")
elif x%4 ==0 and x%100!=0:
    print("year is leap year")
else:
    print("not a leap year")

