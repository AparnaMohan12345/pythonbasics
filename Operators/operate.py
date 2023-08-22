print('........arithmetic operator..........')
x = 30
y = 20
print('sum: ', x+y)
print('Subtract:', x-y)
print('Division:', x/y)
print('Exponent', x**y)
print('To make the floating number rounded', x//y)

print('..........assignment Operator...........')
x = 6
x = x+2
x += 4
print('Assigning', x)
y = 3
y //= 3
print(y)
x **= 2
print(x)

print('................comparison operator............')
x = 2
y = 4
print('comparing x=y is', x == y)
print('not equal x and y is', x != y)
print('less than', x < y)
print('greater than', x > y)
print('less than or equal', x <= y)
print('greater than or equal', x >= y)

print('..........Logical operators..........')
x = 10
y = 15

a = x != y and x > y
print(a)

b = x != y or x == y
print(b)

c = not(x != y and x > y)
print(c)
