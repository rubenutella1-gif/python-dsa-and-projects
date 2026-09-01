n = int(input("Enter a number to check whether the number is power of 2 : "))
if n <= 0:
    print(f"Given number {n} is not power of 2")
else:
    i = 0
    found = False
    while 2 ** i <= n:
        if n == 2 ** i:
            found = True
            break
        i += 1
    if found:
        print(f"Given number {n} is power of 2")
    else:
        print(f"Given number {n} is not power of 2")