def prime(n):
    flag=0
    for i in range(2,n):
        if n%i==0:
            flag =1
            return(1)
        else:
            return(0)
x = int(input("Enter the number"))
m = prime(x)
if m ==0:
    print("The num is prime")
else:
    print("The num is not prime")

