import csv
with open('industry.csv','r')as file:
    csv_file=csv.DictReader(file)
    for row in csv_file:
        print(row)
