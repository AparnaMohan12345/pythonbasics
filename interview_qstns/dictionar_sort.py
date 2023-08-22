dict1 = {5:2, 6:4, 7:3, 8:1, 9:0}
val= list(dict1.items())
print(val)
newval=[]
newvalf=[]
ascend=[]
descend=[]
for i in val:
    irev=i[::-1]
    newval.append(irev)
print(newval)
newval.sort()
print(newval)
newvalf=newval[::-1]
print(newvalf)
for i in newval:
     irevf=i[::-1]
     ascend.append(irevf)
for i in newvalf:
    irevff=i[::-1]
    descend.append(irevff)
print('asecnding order ',ascend)
print('Descending order ',descend)