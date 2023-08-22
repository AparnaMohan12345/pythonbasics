for i in range(1,51):
    if(i%3==0):
        print(i)

#make it into a list
list1 = [ i for i in range(1,51)
    if(i%3==0)]
print(list1)

#list comprehension

fruits=['apple', 'orange', 'banana', 'kiwi', 'grapes']
new_list=[]
for i in fruits:
    if 'a' in i:
        new_list.append(i)
print(new_list)

list_items =[1,8,3,4,5,6,7]
even = [i for i in list_items if i % 2 == 0]
print(even)
odd = [i for i in list_items if i % 2 != 0]

print(odd)


