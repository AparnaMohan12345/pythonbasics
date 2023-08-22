"""
List is
Mutable
Ordered
Indexed
Allow duplicates
"""

list_items = ["apple", "Orange", "Mango"]
print(list_items)
print(list_items[0])
print(list_items[::-1])
print(list_items[0][-1])
print(list_items[2][-3])
print(list_items[2][::-1])
print(list_items[1][4::-1])
print(list_items[1][-2::-1])

#mutate the list

list_items[1] = "pineapple"
print(list_items)

#nested list

list_it = ["apple", "Orange", "Mango", ["python", "java", "C++"]]
print(list_it[3][0])
print(list_it[3][0][::-1])
print(list_it[3][::-1])

#insert an item in an index

list_it[3].insert(1,"golang")
print(list_it)
list_it.insert(2,"golang")
print(list_it)


#append only add an item at the end of the list

list_it.append("angular")
print(list_it)

#extending a list
list2 = ["car", "bike", "bus", "lorry"]
list_it.extend(list2)
print(list_it)


#remove an element
list_it[4].remove("golang")
print(list_it)

list_it[4].pop(1)
print(list_it)

list_it[4].pop(-1)
print(list_it)

del list_it[7:]
print(list_it)


# can use del and clear to remove full list

list_it[4].insert(1,list2)
print(list_it)
del list_it[4][1][1]
print(list_it)


#copy the list

x = list_it.copy()
print(x)

#count the list

y = list_it[4].count('python')
print(y)



#reverse the list

list_it.reverse()
print(list_it)

#sort
list3 = ["verb","noun","plural"]
list3.sort()
print(list3)

