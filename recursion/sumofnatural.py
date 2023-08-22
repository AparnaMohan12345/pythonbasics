def sumof(b):
 if b>0:
    sum_of_num = b +sumof(b-1)

    return(sum_of_num)
 else:
     return b


a = int(input("Enter the number to find the sum of upto that number"))
sum = sumof(a)
print("sum of ", a, " natural numbers is ",sum)