def BinarySearch(arr,target):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if target==arr[mid]:
            return(f"Element found at index number {mid}")
        elif target<arr[mid]:
            end=mid-1
        elif target>arr[mid]:
            start=mid+1
    return "-1"
arr = [2, 5, 7, 10, 15, 18, 20, 25]
result=BinarySearch(arr,target=18)
print(result)