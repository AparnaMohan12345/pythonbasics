def findfib(num):
   if num<=1:
       return num
   else:
       fib3 = findfib(num - 1) + findfib(num - 2)
       return fib3

num = int(input("Enter the number to find the fibanocci series "))

fib =findfib(num)
print(fib)
