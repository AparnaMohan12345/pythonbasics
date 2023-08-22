str1='python'
str3=''

for i in str1:
    str3=i+str3
    print(str3)

#another method

def reverse(str2):
    str2 = [str2[i] for i in range(len(str2)-1,-1,-1)]
    print(str2)
    return ''.join(str2)
print(reverse(str1))
