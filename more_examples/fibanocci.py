x = int(input("Enter the range for fibanocci series"))
fib = 0
n1 = 0
n2 = 1
for i in range(1,x):
    print(n1)
    fib = n1 +n2
    n1 = n2
    n2 = fib

