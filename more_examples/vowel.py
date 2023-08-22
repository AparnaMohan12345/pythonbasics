char1 = input("Enter the char")
vowels =['a', 'e', 'i','o','u','A', 'E', 'I', 'O', 'U']
#if char1 == 'a' or char1 =='e' or char1 =='i' or char1 =='o' or char1 =='u' or char1 =='A' or char1 =='E' or char1 =='I' or char1 =='O' or char1 =='U':

if char1 in vowels:
     print("Char is a vowel")
else:
     print("char is a consonent")