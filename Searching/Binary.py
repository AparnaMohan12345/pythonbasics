def binary(a,b):
    n=len(a)
    low = 0
    high = n-1
    while low<=high:
        mid=(low+(high-low))//2
        if a[mid]==b:
            return mid
        elif a[mid]<b:
            low=mid+1
        else:
            high = mid-1
    return -1

array = [3, 4, 5, 6, 7, 8, 9,10]
x = 6
result = binary(array,x)
if result ==-1:
    print("Element not found")
else:
    print("Element found on the position ",result)