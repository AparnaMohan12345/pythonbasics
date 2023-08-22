str1 = input("Enter the string")
list1=[]
for i in str1:
    if i in list1:
        continue
    else:
        list1.append(i)
print(list1)