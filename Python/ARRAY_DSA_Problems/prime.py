while True:
    n=int(input("Enter a number : "))
    if n<2:
        print(f"Entered number {n} is not prime number ")
    elif n==2:
        print(f"Entered number {n} is prime number ")
    elif n%2==0:
        print(f"Entered number {n} is not prime number ")
    else:
        result=True
        for i in range(3,int(n**0.5)+1,2):
            if n%i==0:
                result=False
                break
        if result:
            print(f"Entered number {n} is  prime number ")
        else:
            print(f"Entered number {n} is not prime number ")