tple = ('apple', '89', '6', 'banana', 'apple',[678, 'mango'])
print(tple[4])
print(tple[5][0])
print(tple[-1][1])
print(tple[2::-1])

#Inserting an elemennt

x = list(tple)
print(x)
x[0] ="grapes"
print(x[0])
print(tuple(x))

#insert a tuple into another

tple1 = ('one', 'two', 'three')
tple2 = ('four', 'five', 'six')

p = list(tple1)
print(p)
# n = list(tple2)
# print(n)
p.extend(tple2)
print(tuple(p))

print(len(tple1))
# print element with index
index = 0
while index < len(tple1):
    l = tple1[index]
    print(index, l)
    index+=1

#second method
p=[]
index = 0
for i in tple2:
    if index < len(tple2):
        p = (index, i)
        print(list(p))
        index += 1

#enumerate method

x = enumerate(tple1)
print(list(x))

#reverse tuple
print(tple1[::-1])
x = (1,2,3,[3,4,5])
print(x[3][::-1])

#element exist in a tuple
tple1 = ("apple",1,2,3,4)
if "apple" in tple1:
        print("apple in tuple")
else:
        print("apple not in tuple")

# convert tuple to string
x = ('s', 't', 'r', 'i', 'n', 'g')
print("".join(x))

# count the number of occurence
y = (20,50,70,50,60,50)
c = y.count(50)
print(c)