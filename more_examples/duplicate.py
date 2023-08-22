str3 = "lets google the pineapple"
str1 = str3.split(' ')
print(str1)
str2=[]
for i in str1:
 k = " "
 #print(i)
 for j in i:

     if j in k:

      continue
     else:
         k=k+j
 print(k)
 str2.append(k)
 print(str2)
print(" ".join(str3))

