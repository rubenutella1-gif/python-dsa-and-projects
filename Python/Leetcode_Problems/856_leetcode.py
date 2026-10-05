s=input("Enter valid paranthesis: ")
stack=[0]
for i in s:
    if i=="(":
        stack.append(0)
    else:
        score=stack.pop()
        if score==0:
            score=1
        else:
            score=score*2
        stack[-1]+=score    
print(stack[0])