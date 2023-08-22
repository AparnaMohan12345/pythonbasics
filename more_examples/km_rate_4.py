km = int(input("Enter the Kilometers"))
if km <= 10:
    amt = km*11
elif km >= 10 and km<= 90:
    amt = 110 + ((km - 10)* 10)
elif km > 100:
    amt = 1010 + ((km - 100)*9)
print("total amount to pay ", amt)