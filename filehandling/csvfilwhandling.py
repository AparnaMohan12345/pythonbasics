import csv
with open("names.csv",'r') as file:
    reader=csv.reader(file)
    for i in reader:
     print(i)