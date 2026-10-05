l1=[12,0,34,34,0,34,0,4,42,0]
j=0
for i in range(len(l1)):
    if l1[i]!=0:
        l1[j],l1[i]=l1[i],l1[j]
        j+=1
print(l1)