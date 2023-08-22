import csv

with open("add.csv",'r')as file:
 with open("temp.csv", 'a',newline='') as file1:
    reader=csv.reader(file)
    writer = csv.writer(file1)
    for i in reader:
     writer.writerow(i)
with open("temp.csv", 'r',newline='') as file3:
    read=csv.reader(file3)
    for i in read:
        print(i)

# f=open("add.csv",'r')
# f1= open("temp.csv",'w')
# d=csv.reader(f)
# d1=csv.writer(f1)
# for i in d:
#     d1.writerow(i)
# f.close()
# f1.close()