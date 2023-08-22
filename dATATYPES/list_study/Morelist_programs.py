# find common numbers from two list
list1 = [1,6,8,7,3]
list2 = [8,6,4,3,1]
list3=[]

for i in list1:
   for j in list2:
       if i == j:
           list3.append(i)
print(list3)

#method2
new_list =[]
for i in list1:
   for j in list2:
       if i == j and i not in new_list:
           new_list.append(i)
print(new_list)

new_list =[]
for i in list1:
   if i not in list2 and i not in new_list:
       new_list.append(i)
for j in list2:
   if j not in list1 and j not in new_list:
       new_list.append(j)
print(new_list)


#print even numbers
list_even = [1,6,8,7,3]
new_list =[]
for i in list_even:
    if i%2 == 0:
        new_list.append(i)

print(new_list)

#remove repeated elements

m = ['lets', 'google', 'the', 'pineapple', 'photo', 'google', 'photo']


new_list=[]
for i in m:
   if i not in new_list:
       new_list.append(i)
print(new_list)

#print suffix

m = ['www.zframes.com', 'www.wikipedia.org', 'www.asp.net', 'www.abcd.in']
for i in m:
    a = i.split('.')
    print(a[-1])