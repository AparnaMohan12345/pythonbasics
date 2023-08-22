str1 ="this is a python program send many orders"
words = list(str1.split(" "))
for i in words:
    if (len(i))%2 == 0:
        print(i)
