while True:

    n = int(input("Enter a Positive number : "))

    if n == 0:
        Smallest_digit = 0
    else:
        Smallest_digit = 10
        temp = n

        while temp != 0:
            digit = temp % 10

            if digit < Smallest_digit:
                Smallest_digit = digit

            temp = temp // 10

    print(f"Smallest digit is {Smallest_digit}")

    choice = input("Enter your choice (y/n): ").lower()

    if choice == "n":
        break