str1 = input("input a string")
letters=0
digits=0
for i in str1:
    if(i>='a' and i<='z') or (i>='A' and i<='Z'):
        letters +=1
    if i>='0' and i<='9':
        digits +=1
print("Total number of letters: ", letters)
print("Total number of digits: ", digits)