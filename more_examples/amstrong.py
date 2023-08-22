x = int(input("Enter a num"))
sum = 0
temp = x
while x != 0:
    dig = x%10
    sum = sum +(dig*dig*dig)
    x = x//10
if temp == sum:
    print("the num is Armstrong")
else:
    print("The num is not Armstrong")
