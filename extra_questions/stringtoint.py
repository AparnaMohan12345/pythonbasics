str1= '123'
results=0
for i in str1:
    digits = ord(i) - ord('0')
    results = results*10+digits
print(results)
print(type(results))

