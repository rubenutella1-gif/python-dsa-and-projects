l1=list(input("Enter list of element :").split())
l2=[]
n=len(l1)-1
for i in range(len(l1)):
    if n==0:
        l2.append(l1[i])
    elif i==0:
       if l1[i]>l1[i+1]:
            l2.append(l1[i])
    elif i==n:
        if l1[i]>l1[i-1]:
            l2.append(l1[i])
    else:
        if l1[i]>l1[i-1] and l1[i]>l1[i+1]:
            l2.append(l1[i])
print(l2)