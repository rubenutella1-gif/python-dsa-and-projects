# Count Frequency of Characters in a String
# Return a dictionary with character counts.
string="Hello I am learning python"
string1=string.lower()
count_char={}
for char in string1:
    if char!=" ":
        count_char[char]=count_char.get(char,0)+1
print(count_char)