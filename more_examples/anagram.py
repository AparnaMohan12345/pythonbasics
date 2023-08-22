x1 = input("Enter the first string ")
y1 = input("Enter the second string ")
count =0
x = x1.lower()
y = y1.lower()
if len(x) == len(y):
   print("lengths are equal")
else:
    print("lengths are not equal")
for i in x:
 for j in y:
  if i == j:
    count +=1
if count == len(x):
    print("Strings are anagram")
else:
    print("Strings are not anagram")

#second method

str1 = input("Enter the first string ")
str2 = input("Enter the second string ")
str3 = str1.lower()
str4 = str2.lower()

if len(str3)== len(str4):
    sort1 =sorted(str3)
    sort2 =sorted(str4)
if sort1 == sort2:
    print("strings are anagram")
else:
    print("strings are not anagram")