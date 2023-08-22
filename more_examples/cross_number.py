n = int(input("Enter a number "))
for i in range(1,n+1):
    x=i
    for j in range(i-1):
        print(" ",end=' ')
    for k in range(i):
       if(x==i):
         print(i,end=' ')
         i=i+1
       else:
           print(" ",end=' ')
    print()

# for i in range(1, n + 1):
#     x = i
#     for j in range(i - 1):
#         print(" ", end=' ')
#     for k in range(i):
#         if (x == i):
#             print(i, end=' ')
#
#             i = i + 1
#     print()