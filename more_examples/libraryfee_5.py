x = int(input("Enter the number of days"))
if x <= 5:
    amt = x*5
elif x > 5 and x <= 10:
    amt = x*3
elif x > 10 and x <= 15:
    amt = x*4

print(amt)

