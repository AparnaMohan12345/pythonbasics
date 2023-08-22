import csv
with open("add.csv",'w', newline='') as file:
    fieldnames=['firstname','lastname']
    w=csv.DictWriter(file,fieldnames=fieldnames)
    w.writeheader()
    w.writerow({"firstname" : 'aparna', 'lastname':'sri'})
with open("add.csv",'r') as file:
    r = csv.reader(file)
    for i in r:
        print(i)
