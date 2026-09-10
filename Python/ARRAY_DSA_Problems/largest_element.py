l1=list(map(int,input("Enter list of elements : ").split()))
largest=l1[0]
for i in range(1,len(l1)):
    if l1[i]>largest:
        largest=l1[i]
print(largest)