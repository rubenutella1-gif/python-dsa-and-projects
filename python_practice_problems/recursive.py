# factorial of a number using recursive
""" def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
while True:
    n=int(input("Enter a number"))
    print("Factorial of a given number is :",fact(n)) """
# fibanacci series using the recursion
""" def fibanacci(n):
    if n<=1:
        return n
    else:
        return fibanacci(n-1)+fibanacci(n-2)
term=int(input("Enter a number : "))
print("Fibanacci series is : ")
for i in range(term):
    print(fibanacci(i),end=" ") """
#without recursion
""" def fib(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
n=int(input("Enter a number :"))
print("Fibanacci series is : ")
fib(n) """
# sum recursive
""" def sum_recursive(n):
    if n==1:
        return 1
    return n + sum_recursive(n-1)
n=int(input("Enter a number : "))
print(sum_recursive(n)) """
# reverse a string using the recursive
def recursive_reverse(s):
    if len(s)==0:
        return ""
    else:
        return s[-1]+recursive_reverse(s[:-1])
s=input("Enter a string : ")
print("Reversed string is : ",recursive_reverse(s))