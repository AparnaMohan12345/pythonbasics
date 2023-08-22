str1 = input("Enter the string")
vowels= ['a','e','i','o','u','A','E','I','O','U']
for i in range(len(str1)):
    if str1[i] in vowels:
        str1.replace(str1[i],'-')
        break

print(str1)
