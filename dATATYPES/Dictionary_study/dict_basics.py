"""
ordered
indexed
duplicates not allowed
Mutable
"""
dict1 ={'name':'apz', 'age':25, 'place':'abc'}
print(dict1)
print(dict1['age'])
print(dict1.get('name'))
dict1["name"]="priya"
print(dict1)
dict1.update({'qualification':'bca', 'job':'teaching'})
print(dict1)
print(dict1.keys())
print(dict1.values())
#print(dict1.items())
print(dict(zip(dict1.keys(),dict1.values())))
dict1.pop("name")
print(dict1)
dict1.popitem()
print(dict1)
dict1.clear()
print(dict1)
dict1 ={'name':'apz', 'age':25, 'place':'abc'}
x =(1,2,3)
y = 0
dict3 = dict.fromkeys(x,y)
print(dict3)
dict1.setdefault('age',26)
print(dict1)
dict1.setdefault('work','it')
print(dict1)
#rename key in dictionary
dict1 ={'name':'apz', 'age':25, 'place':'abc'}
dict1["school area"]=dict1.pop("place")
print(dict1)
