l1 = list(map(int, input("Enter list of elements: ").split()))

largest = float('-inf')
second_largest = float('-inf')

for num in l1:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second largest element:", second_largest)