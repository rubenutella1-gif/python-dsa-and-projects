# 🔠 String Manipulation Problems
# Check Palindrome
# Check whether a given string is a palindrome.
def is_palinderom_or_not(n):
    if n.lower()==n.lower()[::-1]:
        print(n,"is palindrome")
    else:
        print(n,"is not a polindrome")
n=input("Enter your inout : ")   
is_palinderom_or_not(n)    