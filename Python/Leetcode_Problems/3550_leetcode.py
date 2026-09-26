nums = [1, 3, 2]

for i in range(len(nums)):

    sum_of_digit = 0
    temp = nums[i]

    while temp > 0:

        digit = temp % 10
        sum_of_digit += digit
        temp = temp // 10

    if sum_of_digit == i:
        print(i)
        break

else:
    print(-1)