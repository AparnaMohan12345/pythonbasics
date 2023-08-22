import csv


with open("data.csv",'w',newline='')as file:
    writer=csv.writer(file)
    writer.writerow(['admno','name','class'])
    writer.writerow([1, 'name1', 'class1'])
    writer.writerow([2, 'name2', 'class2'])
    writer.writerow([3, 'name3', 'class1'])
    writer.writerow([4, 'name4', 'class1'])
    writer.writerow([5, 'name5', 'class1'])

s= input("Admission number to search ")
found = False
with open("data.csv",'r')as file:
    reader = csv.reader(file)
    count =0
    for i in reader:
        if i[0] == s:
            print('admno = ',i[0])
            print('name = ', i[1])
            print('class = ', i[2])
            found = True
            break

if found == False:
    print("Not found")
