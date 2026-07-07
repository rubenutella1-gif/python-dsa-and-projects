try:
    n=int(input("Enter valu of n :"))
    arr=list(map(int,input().split()))
    if len(arr)!=n:
        raise ValueError("Entered array is not equals to the size of the array")
    max_ending_here=arr[0]
    max_so_far=arr[0]
    for i in range(1,n):
        max_ending_here=max(arr[i],arr[i]+max_ending_here)
        max_so_far=max(max_ending_here,max_so_far)
    print(f"Maximum sum of sub array is {max_so_far}")
except:
    print("Invalid input ")