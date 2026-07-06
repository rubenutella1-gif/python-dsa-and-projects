def is_fibanacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b  
n=int(input("Enter a number:"))
is_fibanacci(n)

