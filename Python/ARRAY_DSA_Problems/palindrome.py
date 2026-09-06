import time

while True:

    n = int(input("Enter a number to check whether the number is palindrome or not: "))

    original = n

    start_time = time.perf_counter()

    if n < 0:
        print(f"Given number {original} is not palindrome")

    elif n < 10:
        print(f"Given number {original} is palindrome")

    elif n % 10 == 0:
        print(f"Given number {original} is not palindrome")

    else:
        reversed_half = 0

        while n > reversed_half:
            digit = n % 10
            reversed_half = reversed_half * 10 + digit
            n = n // 10

        if reversed_half == n or n == reversed_half // 10:
            print(f"Given number {original} is a palindrome")
        else:
            print(f"Given number {original} is not palindrome")

    end_time = time.perf_counter()

    execution_time = end_time - start_time

    print(f"Start Time : {start_time}")
    print(f"End Time   : {end_time}")
    print(f"Execution Time : {execution_time:.10f} seconds")