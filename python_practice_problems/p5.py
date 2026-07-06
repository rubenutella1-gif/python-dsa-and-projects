try:
    n=int(input())
    arr=list(map(int,input().split()))
    sorted_arr=sorted(set(arr))
    if len(sorted_arr)<2:
        print("-1")
    else:
        print(f"Second Largest element is : {sorted_arr[-2]}")
except:
    print("Enter valid input")