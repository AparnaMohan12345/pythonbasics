x = int(input("Enter the row "))

for i in range(1,x+1):
    for k in range(x - i):
     print(" ",end =' ')
    for j in range(i):
        print("* ", end =' ')
    print("\n")
for i in range(1,x +1):
    for k in range(x - i):
        print(" ", end =" ")
    for j in range(1,i+1):
        print(j, "", end =' ')
    print()

print()
for i in range(x+1):
    for k in range(i):
     print(" ",end ='')
    for j in range(x-i):
        print(" *", end =' ')
    print("\n")

for i in range(1,x +1):
    for k in range(x - i):
        print(" ", end =" ")
    for j in range(1,i+1):
        print(j, ' ', end ='')
    print()


n = int(input("enter the row "))

for i in range(0,n):
    for j in range(i):
        print(" ", end =" ")
    for l in range(n-i):
        print("*  ", end=" ")
    print()

for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end =" ")
    for l in range(i):
        print("*  ", end=" ")
    print()

