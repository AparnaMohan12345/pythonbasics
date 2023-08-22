def even(n):
    list1=[]
    #list2=[i for i range(4,n+1) if i%2==0]
    for i in range(4,n+1):
        if i%2==0:
            list1.append(i)
    return(list1)
a=30
print(even(a))
