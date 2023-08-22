a=int(input("Enter the First number "))
b=int(input("Enter the Second number "))

opt = input("Select the operator( +, -, *,/)")
if opt == "+":
    print("Sum is", (a+b))
elif opt == "-":
    print("Subtract is", (a - b))
elif opt == "*":
    print("Product  is", (a * b))
elif opt == "/":
    print("Remainder is", (a / b))
else:
    print("invalid operator or error")


