#sum all the items in a list
list1 =[1,2,3,4]
print(list1)
sum = 0
for i in list1:
    sum = sum + i

print("Sum of list ", sum)

#find the product
prod = 1
for i in list1:
    prod = prod * i

print("prod of list ", prod)

#write a program t convert list to string
s = ['p', 'y', 't', 'h', 'o', 'n']
m = ''
for i in s:
    m = m + i
print(m)

# separate negative numbers and positive numbers

numbers = [1, 5, 6, -5, -2, -1, -7]
x = []
y = []
z = []
for i in numbers:
    if i>0:
        x.append(i)
    elif i ==0:
        z.append(i)
    else:
        y.append(i)
print(x)
print(y)

# program to find largest
#1 method
mylist =[5,9,8,7,3,2]
mylist.sort()
print(mylist[-1])

#2 method
max = mylist[0]
for i in mylist:
    if max<=i:
       max = i

print(max)
