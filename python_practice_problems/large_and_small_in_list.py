# # List and Array Problems
# Find the Largest and Smallest Element in a List
# Write a program to find the max and min without using max() and min()
lst=[1,2,3,4,5,6,7,8,9,23,54,56]
large=lst[0]
small=lst[0]
for i in lst:
    if large<i:
        large=i
    if small>i:
        small=i
print(large) 
print(small)
   