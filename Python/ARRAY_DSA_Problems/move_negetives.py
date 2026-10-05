l1=[-1,2,4,-3,4,5,-45,-4,53,45,3]
j=0
for i in range(len(l1)):
    if l1[i]>0:
        l1[j],l1[i]=l1[i],l1[j]
        j+=1
print(l1)