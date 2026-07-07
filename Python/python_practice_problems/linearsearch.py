def linearsearch(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    else:
        return -1
arr=[1,23,43,23,421,45]
target=45
result=linearsearch(arr,target)
print(f"Results  found at index {result}"if result!=-1 else "Element not found")