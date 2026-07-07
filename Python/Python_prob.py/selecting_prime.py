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
print(is_prime(n))
position=int(input("Enter the position : "))
if 1<=position<=len(primes):
    print("Prime number at position ",position,"is",primes[position-1])
else:
    print("Invalud input")