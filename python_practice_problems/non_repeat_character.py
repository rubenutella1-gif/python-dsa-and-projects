#Find First Non-Repeating Character
#Return the first character in a string that does not repeat.
string1="Hello World".lower()
dict_count={}
for ch in string1:
    if ch!=" ":
        dict_count[ch]=dict_count.get(ch,0)+1
for ch in string1:        
    if ch!=" " and dict_count[ch]==1:
        print("print ",ch)
        break
else:
    print("Nothing")