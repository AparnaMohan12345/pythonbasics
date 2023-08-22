numbers = [3,6,7,5,11,8]
sum1 = 0
sum2 = 0
list1=[]
list2=[]
for i in numbers:
    if i%2 == 0:
        list1.append(i)
        sum1 = sum1 + i
    else:
        list2.append(i)
        sum2 = sum2 + i
print("sum of even ", list1, sum1)
print("sum of odd ", list2, sum2)

