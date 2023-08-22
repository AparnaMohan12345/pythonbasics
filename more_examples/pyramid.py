x= int(input("Enter the level of pyramid: "))
for i in range(x):
    for k in range(x-i):
        print(" ",end=" ")
    for j in range(i + 1):
        print(" * ", end=" ")
    print("\n")



