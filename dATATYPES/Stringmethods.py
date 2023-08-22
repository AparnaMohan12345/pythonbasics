str1 = "Hello world"
print(str1.find("l"))   #find the index of a character
print(str1.__str__())
mn = ["apz", "jaz", "class"]
print("#".join(mn))   #join the items in a list or other datatypes
print(str1.count("l"))  #count the occurence of a character or word
print(str1.lower())
print(str1.upper())
print(str1.capitalize())
print(str1.split())
print("#".join(str1))
print(str1.casefold())
print(str1.isalnum())
print(str1.isalpha())

print("................Slicing.............")
name = "Aparna Mohan"
print(name[0:6])
print(name[::-1])
print(name[:-6:-1])
print(name[:6:-1])
print(name[-7::-1])
print(name[5::-1])
print(name[::2])