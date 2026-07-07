# Check Prime Number
# Write a function that checks whether a number is prime.
def is_prime(num):
    if(num<2):
        return False
    if(num==2):
        return True
    for i in range(2,num):
        if num%i==0:
            return False
    return True
while True:
    num=int(input("Enter a number To check prime number")) 
    print(is_prime(num))         