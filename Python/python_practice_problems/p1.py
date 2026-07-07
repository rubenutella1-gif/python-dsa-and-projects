n=int(input(("Enter no of values").strip()))
arr=list(map(int,input().split()))
mp={}
rank=1
for num in sorted(arr):
    if num not in mp:
        mp[num]=rank
        rank+=1
print([mp[num] for num in arr])