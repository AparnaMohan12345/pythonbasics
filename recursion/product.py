def productof(num,prod):
   if num==0:
     return prod
   else:
     n = num % 10
     prod = prod * n
     num = num // 10
     return productof(num,prod)
num = int(input("Enter the number"))
prod=1
product= productof(num,prod)
print("the product of digits in ", num , " is ",product)