print("Enter numbers from 65 to 91")
x=int(input("Enter the first num "))
y = int(input("Enter the second num "))

for i in range(x, y):
    k = i
    for j in range(x,i+1):
        print(chr(k),end='')
        k=k+1
    print()



n = int(input("Enter the levels "))
k1=1
for i in range(1,n+1):

    for j in range(n-i):
        print(" ",end=' ')
    for k in range(1,i+1):
        ch = chr(64+k1)
        print(ch,end='   ')
        k1=k1+1
    print()
