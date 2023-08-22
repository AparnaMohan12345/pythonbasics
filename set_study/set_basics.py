"""
immutable
unchangeable
can remove and add
unordered
un indexed
"""
set1 ={'safna',12,'python',12, (1,2,3), set["abc",46,'cdf']}
print(set1)
x =list(set1)
print(x)

A = {1,2,3,4,}
B = {12,1,2,3,5}
print(A.union(B))
print(A.difference(B))
print(A.intersection(B))
A = (A.difference_update(B))
print(A)