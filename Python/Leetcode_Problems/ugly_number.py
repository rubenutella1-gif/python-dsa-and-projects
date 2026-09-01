while True:
    n=int(input("Enter a number to check ugly number or not : "))
    if n<=0:
        print(f"Given number {n} is not ugly")
    elif n==1:
        print(f"Given number {n} is Ugly number ")
    else:
        temp=n
        while temp%2==0:
            temp=temp//2
        while temp%3==0:
            temp=temp//3
        while temp%5==0:
            temp=temp//5
        if temp==1:
            print(f"Given number {n} is Ugly number ")
        else:
            print(f"Given number {n} is not ugly")
    choice = input("Do you want to continue? (yes/no): ").lower()

    if choice == "no":
        break