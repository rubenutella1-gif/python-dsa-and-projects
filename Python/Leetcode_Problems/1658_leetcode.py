nums = [1, 1, 4, 2, 3]
x = 5

total_sum = sum(nums)
target = total_sum - x

left = 0
current_sum = 0
max_length = -1

for right in range(len(nums)):

    current_sum += nums[right]

    while current_sum > target and left <= right:
        current_sum -= nums[left]
        left += 1

    if current_sum == target:
        length = right - left + 1
        max_length = max(max_length, length)

if max_length == -1:
    print(-1)
else:
    no_of_operations = len(nums) - max_length
    print(no_of_operations)