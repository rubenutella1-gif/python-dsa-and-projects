l1 = list(map(int, input("Enter list of elements: ").split()))

smallest = float('inf')
second_smallest = float('inf')

for num in l1:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Second smallest element:", second_smallest)