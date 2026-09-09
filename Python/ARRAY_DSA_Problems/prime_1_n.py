while True:
    n = int(input("Enter a number: "))

    primes = []

    for i in range(2, n + 1):

        if i == 2:
            primes.append(i)
            continue

        if i % 2 == 0:
            continue

        is_prime = True

        for j in range(3, int(i ** 0.5) + 1, 2):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

    if n < 2:
        print(f"There are no prime numbers till {n}")
    else:
        print(f"All primes till {n} are {primes}")