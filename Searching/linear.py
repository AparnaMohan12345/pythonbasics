def linear_search(a,b):
    for i in a:
        if(a[i]==b):
            return i
    return -1
list1=[1,3,5,7,8]
key= 7
n=linear_search(list1,key)
if(n == -1):
    print("Element not found")
else:
    print("element found on index position ",n)
