l1=list(map(int,input("Enter list of elements seperated by space: ").split()))
key=27
status=False
for i in range(len(l1)):
    if l1[i]==key:
        status=True
        index_number=i
if status:
    print(f"Key found at index {index_number}")
else:
    print("key not found ")