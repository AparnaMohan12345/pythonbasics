x = int(input("Enter the number "))
rev =0
while x!=0:
    rem = x%10
    rev = rem + (rev*10)
    x //=10

print("the reve  rse of number ", rev)