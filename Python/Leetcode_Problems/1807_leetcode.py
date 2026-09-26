s=input("Enter a string: ")
dict1={'name':'Rubenu','age':'24'}
result=""
i=0
while i<len(s):
    
    if s[i]!="(":
        result+=s[i]
        i+=1
    else:
        j=i+1
        while s[j]!=")":
            j+=1
        key=s[i+1:j]
        if key in dict1:
            result+=dict1[key]
        else:
            result+="?"
        i=j+1
print(result)