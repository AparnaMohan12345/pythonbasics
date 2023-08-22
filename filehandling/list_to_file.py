import csv
import os
list = ['hi','aparna','Mohan']
with open("add.csv",'a',newline='') as file:
    w=csv.writer(file)
    for i in list:
      #  print(i)
      # file.write(i)
        w.writerow([i])
r = open('add.csv','r',newline='')
read=csv.reader(r)
for i in read:
    print(i)


