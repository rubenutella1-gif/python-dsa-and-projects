l1=list(map(int,input("Enter list of elements : ").split()))
smallest=l1[0]
for i in l1:
    if i<smallest:
        smallest=i
print(smallest)