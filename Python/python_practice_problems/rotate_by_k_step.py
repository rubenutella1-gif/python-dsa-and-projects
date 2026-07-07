# Rotate List
# Rotate a list to the right by k steps.
lst=[1,2,3,4,5,6]
k=2
k=k%len(lst)
rotated_list=lst[-k:]+lst[:-k]
print("Rotated list is: ",rotated_list)