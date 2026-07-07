#check if palindrome or not ignore spaces between charechters
inp1=input().lower()
clean=inp1.replace(" ","")
rev=clean[::-1]
if rev==clean:
    print("Palindrome")
else:
    print("Not palindrome")