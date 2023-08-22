str1 = input("enter the first string")
str2 = input("enter the second string")
st1= str1.split()
st2= str2.split()

for i in st1:
 if i in st2:
     print(i)