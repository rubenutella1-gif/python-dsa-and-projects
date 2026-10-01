s=input("enter a string: ")
stack=[]
current=""
for i in s:
    if i=="(":
        stack.append(current)
        current=""
    elif i==")":
        current=current[::-1]
        previous=stack.pop()
        current=previous+current
    else:
        current+=i
print(current)