x = int(input("enter the mark"))
if x > 80:
    print("Having Grade A")
elif x >= 60 and x < 80:
    print("Having grade B")
elif x >= 50 and x < 60:
    print("Having grade C")
elif x >= 45 and x < 50:
    print("Having grade D")
elif x >= 25 and x < 45:
    print("Having grade E")
elif x < 25:
    print("Having grade F")
else:
    print("invalid input")