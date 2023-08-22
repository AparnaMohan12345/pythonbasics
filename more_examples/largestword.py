str1 = input("Enter a string")
l = str1.split()
max = 0
b=''
for i in l:
 if len(i)>max:
    b=i
    max = len(i)
print("largest word is ",b)