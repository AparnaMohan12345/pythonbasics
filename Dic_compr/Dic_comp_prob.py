old={"milk":1.02, "coffee":2.5, "bread":2.4}
dollar = 0.76
new = {key:value*dollar for (key,value)in old.items()}
print(new)


first={"jack":38, "Jin":48, "Sera":39}
second={k:v for(k,v) in first.items() if v%2 ==0}
print(second)

key ={'a','b','c','d','e'}
value={1,2,3,4,5}
pair = {k:v for (k,v) in zip(key,value)}
print(pair)

l=['a','b','c','d','e','f']
l1=l[::2]
l2=l[1::2]
print(dict(zip(l1,l2)))