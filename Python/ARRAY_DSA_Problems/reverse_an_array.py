user_input=input("Enter a string without spaces: ")
result=[]
for i in range(len(user_input)-1,-1,-1):
    result.append(user_input[i])
reversed_string="".join(result)
print(reversed_string)