arr=[11,22,33,44,55]
x=55
for i in range(len(arr)):
    print(f"Element at index number {i} is {arr[i]}")
arr.insert(1,1)
arr.append(40)
print(arr)
arr.remove(1)
print(arr)
arr.pop(3)
print(arr)
if x in arr:
    print(f"{x} is found at position {arr.index(x)}")
else:
    print(f"{x} is not found")
arr[0]=1
print(f"Updated array is {arr}")