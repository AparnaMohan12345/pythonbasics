def sumof(num,sum2):
   if num==0:
     return sum2
   else:
     n = num % 10
     sum2 = sum2 + n
     num = num // 10
     return sumof(num,sum2)
num = int(input("Enter the number"))
sum2=0
sum1= sumof(num,sum2)
print("the sum of digits of ", num , " is ",sum1)

# def sumof(num, sum2):
#    if num == 0:
#      return sum2
#    else:
#         n = num % 10
#         sum2 = sum2 + n
#         num = num // 10
#         return sumof(num, sum2)
#
#
# num = int(input("Enter the number: "))
# sum2 = 0
# sum1 = sumof(num, sum2)
# print("The sum of the digits of", num, "is", sum1)