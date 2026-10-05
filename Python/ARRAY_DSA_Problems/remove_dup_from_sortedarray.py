l1=[1,1,2,3,4,4,5,6,7,7,8,9,9]
j=1
for i in range(1,len(l1)):
    if l1[i]!=l1[j-1]:
        l1[j]=l1[i]
        j+=1
print(l1[:j])