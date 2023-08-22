list1 = [1,6,8,7,3]
list2 = [8,6,4,3,1]
new_list = []
for i in list1:
    for j in list2:
        if i == j and i not in new_list:
            new_list.append(i)

print(new_list)
n_list=[]
for i in list1:
    for j in list2:
        if i not in new_list and i not in n_list:
            n_list.append(i)
        if j not in new_list and j not in n_list:
            n_list.append(j)
print(n_list)