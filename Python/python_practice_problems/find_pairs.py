# Find All Pairs in List with Given Sum
lst=[1,2,3,4,5,6,7,8,9,10]
target=8
i=0
while i<len(lst):
    j=i+1
    while j<len(lst):
        if lst[i]+lst[j]==target:
            print("pair found",lst[i],lst[j])
        j+=1
    i+=1        