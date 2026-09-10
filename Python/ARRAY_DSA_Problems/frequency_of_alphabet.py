user_input=input("Enter input : ").upper()
count_char={}
for char in user_input:
    if char!=" ":
        count_char[char]=count_char.get(char,0)+1
print(count_char)