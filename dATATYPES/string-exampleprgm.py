s1 = "Python"
s2 = "Luminar"
x = int(len(s1))
print("length of s1 is ", x)
mid = x//2
print(type(mid))
print("middle is ", mid)
merge = s1[:mid] + s2 + s1[mid:]
#y = s1[:3] + s2 + s1[3:]
print(merge)

# m = s1[::3]
# print(m)
# n = s2[::3]
# print(n)
# o = m.join(n)
# print(o)
# print(m[0]+n[0]+m[1]+n[1])

first_char = s1[0]+s2[0]
mid_s1 = s1[int(len(s1)/2)]
mid_s2 = s2[(int(len(s2)/2))]
mid = mid_s1 + mid_s2

last_char = s1[-1] + s2[-1]

print(first_char + mid + last_char)