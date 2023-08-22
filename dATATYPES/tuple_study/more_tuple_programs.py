print("find the size of tuple")
tple1 = (1,2,3,4,5)
print(str(tple1.__sizeof__())+ " bytes")

print("find the min and max")
a = 0
min =0
max =0
for i in tple1:
    if a < i:
        min = a
    else:
        max = i

print(max)

