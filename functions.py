"""
Function
1.set of codes
2. Will call repeatedly
3. parameters in function
4. Arguments in the function call
5. Return statement can also add
"""

def sum(a):
    res = 0
    i = 1
    while i <= a:
        res = res + i
        i = i + 1
    return res

x = int(input("Enter a num "))
result = sum(x)
print(result)







