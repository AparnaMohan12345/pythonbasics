n = int(input("Enter the row "))
mid =n/2
for i in range(1,n+1):
    for j in range(n-i):
        print(" ", end =' ')
    for k in range(1,n+1):
        if (k == 1 or k==i):
            print("*  ", end=' ')
        elif(i==mid):
            print("*  ", end=' ')

        else:
            print(" ", end='   ')
    print()