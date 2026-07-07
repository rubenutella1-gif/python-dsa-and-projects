""" a = [10, 20]
b = a

a = [40, 50]
b.append(30)

print(b)
print(a) """
""" Finding max value without sorting array
arr = [3, 7, 2, 9, 5]
max_val=arr[0]
for i in range(1,len(arr)):
    if arr[i]>max_val:
        max_val=arr[i]
print(max_val) """
""" Reversing the array without using the built in functions
arr = [1, 2, 3, 4]
arr1=[]
for i in range(len(arr)-1,-1,-1):
    arr1.append(arr[i])
print(arr1) """
""" Moving all zeros to end of the array
arr = [0, 1, 0, 3, 12]
j=0
for i in range(0,len(arr)):
    if arr[i]!=0:
        arr[j]=arr[i]
        j+=1
for i in range(j,len(arr)):
    arr[i]=0
print(arr) """
# Find the the second largest element in the given array Without using the sort
""" arr = [10, 20, 11, 5, 8]
first=float("-inf")
second=float("-inf")
for num in arr:
    if num>first:
        second=first
        first=num
    elif num>second and num!=first:
        second=num
print(second) """
""" arr = [1, 2, 4, 5]
total=0
remaining=0
n=5
for num in arr:
    total+=num
remaining=((n*(n+1))/2)-total
print(remaining) """
""" a=10
b=20
a,b=b,a
print("Case 1")
print(a,b) """
""" a=10
b=20
temp=0
temp=a
a=b
b=temp
print("Case 2")
print(a,b) """
""" import random
n=random.randint(1,10)
print(n) """
sum=23
array=[10,12,13,3,13]
sub_sum=0
i=0

for i in array:
    for j in range(i+1,len(array)):
        sub_sum=array[i]+array[j] 
    i+=1
    if sub_sum==sum:
        
        print(array[i],array[j])