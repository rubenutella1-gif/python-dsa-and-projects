# 1 take user input ,if the user name in raj he is allowed to class
# 2 if the password lenght is 8 characters then it is allowed or else not allowed
""" user_input=input("Enter your name :")
if user_input=="Raj":
    print("He is allowed to class")
else:
    print("He is not allowed to class") """
""" user_input=input("Enter your password :")
if len(user_input)==8:
    print("You are allowed")
else:
    print("Ypu have to enter 8 characters of password") """
#1 check if the given charecter is vowel or not
""" user_input=input("Please enter a string")
vowel="aeiouAEIOU"
if user_input in vowel:
    print(f"The given input is vowel")
else:
    print("Not a vowel") """
#second method
""" user_input=input("Please enter a string")
vowel=['a','e','i','o','u','A','E','I','O','U']
if user_input not in vowel:
    print("Not a vowel")
else:
    print(f"The given input is vowel") """
#3rd method
""" user_input=input("Please enter a string")
if user_input !='a'or'e'or'i'or'o'or'u'or'A'or'E'or'I'or'O'or'U':
    print("Not a vowel")
else:
    print(f"The given input is vowel") """
#4th method
""" user_input=input("Please enter a string")
if user_input =='a'or'e'or'i'or'o'or'u'or'A'or'E'or'I'or'O'or'U':
    print(f"The given input is vowel")
else:
     print("Not a vowel") """
#write a program to check howmany vowels and consonants in the string and place it in strings
""" user_input=input("Please enter a string : ")
user=user_input.lower()
vowel="aeiou"
vowels=""
consonants=""
for i in user_input:
    if i in vowel:
        vowels+=i+" "
    else:
        consonants+=i+" "
print(f"vowels are:{vowels} and\n consonants are:{consonants}") """
# using lists to check the vowel
""" a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
c=int(input("Enter a number : "))
if a>b and a>c:
    print(f"{a} is largest")
elif b>a and b>c:
    print(f"{b} is largest")
elif c>a and c>b:
    print(f"{c} is largest")
else:
    print("Enter a valid number") """
#Ask the user to enter the number and check the number is divisible by both 5 and 7
""" while True:
    user_input=int(input("Enter a number "))
    if user_input%5==0 and user_input%7==0:
        print(f"The given number {user_input} is divisible by both 5 and 7 ")
    elif user_input % 5==0:
        print(f"{user_input} is divisible by 5 only")
    elif user_input % 7==0:
        print(f"{user_input} is divisible by 7 only")
    else:
        print("The number is not divisible either 5 or 7") """
# BY using the list check the vowel or consonants and push it into lists
""" user_input=input("Enter a string ").lower()
vowel="aeiou"
vowels=[]
consonants=[]
for i in user_input:
    if i in vowel:
        vowels.append(i)
    else:
        consonants.append(i)
print("vowels are :",vowels)
print("consonants are :",consonants) """
#Check uppercase lower case or digit 
#Write a program that takes single character 
#input from the user and determines if it is an uppercase ,lowercase or digit
""" while True:
    user_input=input("Enter a singlr character : ")
    if len(user_input)!=1:
        print("Enter single character ")
    elif user_input.isupper():
        print("The character is uppercase ")
    elif user_input.islower():
        print("The character is lowercase ")
    elif user_input.isdigit():
        print("The character is Digit ")
    else:
        print("Don't enter special character ") """
#Check if the year is leap year or not
while True:
    year=int(input("Enter the Year : "))
    if year%4==0 and (year%100!=0 or year%400==0):
        print(f"{year} is leap year ")
    else:
        print(f"{year} is not leap year ")