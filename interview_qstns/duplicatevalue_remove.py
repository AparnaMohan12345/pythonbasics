list1=[{"v":"5000"},{"v":"5001"},{"v":"5001"},{"v":"5002"},{"v":"5002"}]
uniquelist=[]
duplicatelist=[]
newlist=[]
for i in list1:
    for j in i.values():
        if j not in uniquelist:
            uniquelist.append(j)
        else:
            duplicatelist.append(j)
print(uniquelist)
print(duplicatelist)
for i in uniquelist:
    if i not in duplicatelist:
        newlist.append(i)

print(newlist)



