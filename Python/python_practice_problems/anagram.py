# Anagram Checker
# Check if two strings are anagrams of each other.
def is_anagram(s1,s2):
    str1=s1.replace(" ","").lower()
    str2=s2.replace(" ","").lower()
    string1=sorted(str1)
    string2=sorted(str2)
    return string1==string2

s1=input("enter a string ")
s2=input("enter a string ")
if is_anagram(s1,s2):
    print("given strings anagram")
else:
    print("Not anagram")