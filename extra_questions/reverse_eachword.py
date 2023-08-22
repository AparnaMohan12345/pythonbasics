str1 = ("lets google the pineappple")
str2= str1.split(' ')
print(str2)
str3=[]
for i in str2:
    rev=i[::-1]
    str3.append(rev)
str4 = ' '.join(str3)
print(str4)