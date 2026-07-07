# Greatest Common Divisor (GCD)
# Write a function to find the GCD of two numbers.
def find_gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
while True:
    num1=int(input("Enter First Number : "))    
    num2=int(input("Enter Second Number : "))
    print(find_gcd(num1,num2))    