"""
. Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
(Just try )

Hints:
Consider use yield

"""
class divisible:
    def __init__(self):
        pass
    def divby(self,n):
        for i in range(0,n):
            if i%7 ==0:
                print(i)
n = int(input("Enter the range"))
d1 = divisible()
d1.divby(n)