def is_prime(n):
    l1=[]
    for j in range(2,n):
        for i in range(2,j):
            if j%i==0:
                break
        else:
            l1.append(j)
    return l1
n = int(input("Enter a number to print numbers: "))  
primes=is_prime(n)
print(primes)
print("""Prime numbers in the list
      according to the prime number positions (1-n) not from indexing """)
l2=[]
for i in range(2,len(primes)+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        l2.append(primes[i-1])
print(l2)

"""def is_prime(n):
    l1 = []

    for j in range(2, n):
        for i in range(2, j):
            if j % i == 0:
                break
        else:
            l1.append(j)

    return l1


n = int(input("Enter a number: "))

primes = is_prime(n)

print("Prime numbers:")
print(primes)

prime_positions = is_prime(len(primes) + 1)

l2 = []

for pos in prime_positions:
    l2.append(primes[pos - 1])

print("\nPrime numbers at prime positions:")
print(l2)"""