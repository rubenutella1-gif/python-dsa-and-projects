l1=list(map(int,input("Enter list of elements : ").split()))
sum_of_array=0
no_of_elements=len(l1)
for num in l1:
    sum_of_array+=num
average_of_elements=sum_of_array/no_of_elements
print(sum_of_array)
print(average_of_elements)