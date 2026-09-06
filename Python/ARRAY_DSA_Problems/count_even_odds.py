while True:
    n=int(input("Enter a number : "))
    even=0
    odd=0
    temp=n
    if n == 0:
        even = 1
    else:
        while temp != 0:
            digit = temp % 10
            if digit % 2 == 0:
                even += 1
            else:
                odd += 1
            temp = temp // 10
    print(f"even count in number {even}")
    print(f"odd count in number {odd}")
    choice=input("Do you want to continue Enter your choice (y/n)").lower()
    if choice=="n":
        break