# x = int(input("Enter a number"))
# rev = int(str(x)[::-1])
# if x == rev:
#     print("The num is palindrome")
# else:
#     print("The num is not palindrome")

#second method
y = int(input("Enter a number"))
temp = y
rev=0
while y!=0:
    rem = y%10
    rev = (rev*10)+rem
    y //=10
if temp == rev:
    print("The num is palindrome")
else:
    print("The num is not palindrome")