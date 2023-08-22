class math:
    @staticmethod
    def multiply(a,b):
        return a * b
    @staticmethod
    def is_even(number):
        return number % 2 ==0
result = math.multiply(2,4)
print(result)
print(math.is_even(2))
