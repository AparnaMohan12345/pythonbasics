x = int(input("enter a num"))
flag = 0
for i in range(2,x):
    if x%i == 0:
        flag =1
if flag == 0:
    print("the num is prime")
else:
    print("the num is not prime")