str1 = '18345789'
num=[]
even=[]
odd=[]
for i in str1:
    num.append(int(i))

print(num)
for i in num:
    if i%2 ==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
x= sorted(even)
y= sorted(odd,reverse=True)
print(x)
print(y)
x.extend(y)
print(x)
res=''
for i in x:
    res=res+str(i)
print(res)
res =[str(i) for i in x ]
rev=''.join(res)
print(rev)