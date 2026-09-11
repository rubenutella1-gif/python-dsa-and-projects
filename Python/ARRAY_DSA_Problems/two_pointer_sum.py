l1=[2,3,5,7,9,11]
target=9
left=0
right=len(l1)-1
while left<right:
    current_sum=l1[left]+l1[right]
    if current_sum==target:
        print((left+1),right+1)
        break
    elif current_sum>target:
        right=right-1
    elif current_sum<target:
        left=left+1