n = int(input("Enter the row "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end =' ')
    for k in range(1,n+1):
        if (k == 1 or k==i):
            print("*  ", end=' ')
        else:
            print(" ", end='   ')
    print()

for i in range(1,n):
    for j in range(i):
        print(" ", end =' ')
    for k in range(1,n):
        if (k == 1 or k==n-i):
            print("*  ", end=' ')
        else:
            print(" ", end='   ')
    print()



