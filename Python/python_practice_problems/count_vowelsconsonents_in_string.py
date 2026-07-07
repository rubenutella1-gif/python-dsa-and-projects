# #Count Vowels and Consonants
# Write a function to count the number of vowels and consonants in a string.
string=input("Enter string : ")
vowels=['a','e','i','o','u','A','E','I','O','U']
vowel_count=0
consonant_count=0
for i in string:
    if i!=" ":
     if i in vowels:
        vowel_count+=1
     else:
        consonant_count+=1 
print("vowel count is",vowel_count)   
print("consonant count is",consonant_count)     