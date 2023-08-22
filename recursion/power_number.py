# def powerof(num,power,count,n):
#     while count<power:
#         n=n*num
#         count+=1
#     return n
def powerof(num,power,count,n):
    if count<power:
        n=n*num
        count+=1
        return powerof(num,power,count,n)
    else:
        return n
num=int(input("Enter the number to find the power"))
power = int(input("Enter the power to calculate"))
count=0
n=1
result= powerof(num,power,count,n)
print("The ",power," power of the number ",num," is ",result)