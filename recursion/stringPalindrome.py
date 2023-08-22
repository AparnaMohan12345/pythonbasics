# def reverseof(string,string2):
#     list1=list(string)
#     for i in list1:
#         string2=str(list1[-1])
#         reverseof(string[i:-i],string2)
#     return(string2)
# string = input("enter a string")
# string2=""
# reverse=reverseof(string,string2)
# if reverse == string:
#  print("The reverse of string ",string," is ",reverse)
# else:
#     print("The string is not palindrome")

s=input("Enter the string")
def is_palindrome(s):
    if len(s)<=1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
print(is_palindrome(s))