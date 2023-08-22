x = int(input("Enter first num"))
y = int(input("Enter second num"))
gcd = 1
if x<y:
    smaller =x
else:
    smaller = y


for i in range(1, smaller):
     if x%i == 0 and y%i == 0:
         gcd = i
print(gcd)


