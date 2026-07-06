# #Reverse a String
# Reverse the input string without using built-in functions.
string=input("Enter a string: ")
rst=""
for i in string:
    rst=i+rst
print(rst)