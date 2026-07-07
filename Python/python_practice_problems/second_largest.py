# Second Largest Number
# Find the second largest number in a list without sorting.
lst=[1,2,34,25,23,6446,43,5334,564]
first=second=float('-inf')
for i in lst:
    if i>first:
        second=first
        first=i
    elif i>second and i!=first:
        second=i
print(first)
print(second)