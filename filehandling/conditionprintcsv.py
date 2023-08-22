import csv
with open("student.csv",'w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(['roll','name','marks'])
    writer.writerow([1, 'name1', 20])
    writer.writerow([2, 'name2', 50])
    writer.writerow([3, 'name3', 90])
    writer.writerow([4, 'name4', 100])
f=open("student.csv",'r')
read=csv.reader(f)
next(read)
for i in read:
    if int(i[2])>=80:
        print(i)




