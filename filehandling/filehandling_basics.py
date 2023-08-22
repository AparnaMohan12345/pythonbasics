"""
File can be
read
write
append
insert
delete
Modes: w,r,x,remove,a,w+,r+,a+
"""
#create file
with open("batch.txt",'w')as file:
    file.write("Hi Aparna")
    file.close()
with open('batch.txt', 'a') as file:
   l1 = "Welcome to TutorialsPoint\n"
   l2 = "Write multiple lines \n"
   l3 = "Done successfully\n"
   l4 = "Thank You!"
   file.writelines([l1, l2, l3, l4])


#read file
# with open("batch.txt",'r')as file:
#     print(file.read())


#delete file
# import os
# file = "batch.txt"
# os.remove(file)


#reading file as list
# with open("batch.txt",'r')as file:
#     # print(file.readlines())
#     x = file.readlines()
#     # x.pop(0)
#     print(x)

#multiple lines to delete
import fileinput
file ='batch.txt'
lines_del=[1,2]
def delete_line(file,lines_del):
      with fileinput.input(file,inplace=True)as file:
         for i in file:
           if file.lineno() not in lines_del:
            print(i.rstrip())
delete_line(file,lines_del)
