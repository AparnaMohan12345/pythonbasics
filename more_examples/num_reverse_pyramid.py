n = int(input("Enter the rows "))
for i in range(0,n):
    for j in range(n-i):
        print("",end='')
    for k in range(n-i,0,-1):
        print(k, end='')
    print()