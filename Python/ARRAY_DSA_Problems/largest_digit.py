while True:
    n=int(input("Enter a number : "))
    largest_digit=0
    temp=n
    while temp!=0:
        digit=temp%10
        if digit>largest_digit:
            largest_digit=digit
        temp=temp//10
    print(f"Largest digit is {largest_digit}")
    choice=input("Enter your choice (y/n)").lower()
    if choice=="n":
        break