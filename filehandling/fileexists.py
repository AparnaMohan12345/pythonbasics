#file exists or not
import os
if os.path.exists("batch.txt"):
    print("File exists")
else:
    print("File not exists")

#file size

size = os.stat("batch.txt")
print(size.st_size)

#count the line in file

file1 = open("batch.txt")
count=0
t=file1.readlines()
print(t)
for i in t:
    print(i)
    count+=1
print(count)

#search for a string in text file
with open("batch.txt",'r')as file2:
 file3=file2.read()
 s= "Done successfully"
 if s in file3:
     print("Word exists")
 else:
     print("Word doesn't exists")
