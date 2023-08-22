str1 = input("Enter the string ").lower()
str2 = str1[::-1]
print(str2)
if str1 == str2:
    print("String is palindrome")
else:
    print("String is not palindrome")