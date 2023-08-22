str1 = input("Enter a string")
char = input("Enter the character to count")
count =0
for i in range(len(str1)):
    if(str1[i] == char):
        count+=1
print(count)