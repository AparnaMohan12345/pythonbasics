import csv
s= input("Do you want to write into the file? (y/n)")
with open("add.csv",'w',newline='')as file:
    writer= csv.writer(file)
    writer.writerow(["roll", "name", 'class'])

while s=='y' or s=='Y':
    r=int(input("Enter the roll no "))
    n=input("Enter the name")
    c=input("Enter the class")
    rec=[r,n,c]
    with open("add.csv", 'a', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(rec)
    s = input("Do you want to write into the file? (y/n)")

with open("add.csv",'r')as file:
    reader= csv.reader(file)
    for i in reader:
     print(i)
