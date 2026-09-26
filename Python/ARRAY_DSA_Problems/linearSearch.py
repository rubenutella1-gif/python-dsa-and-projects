l1=list(map(int,input("Enter list of elements seperated by space: ").split()))
key=27
status=False
for i in l1:
    if i==key:
        status=True
        break
if status:
    print("Key found ")
else:
    print("key not found ")