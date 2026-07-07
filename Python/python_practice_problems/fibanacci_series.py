# # #Fibonacci Series
# # Generate the Fibonacci series up to n terms using iteration and recursion.
# def fibancci(n):
#     a,b=0,1
#     series=[]
#     for i in range(n):
#         series.append(a)
#         a,b=b,a+b
#     return series
# while True:
#     n=int(input("Enter a Number"))    
#     print("Fibanacci Series is:")
#     print(fibancci(n))
def recursive_fibanacci_sries(n):
    if n<=1:
        return 1
    return recursive_fibanacci_sries(n-1)+recursive_fibanacci_sries(n-2)
def recursive(num):
    series=[]
    for i in range(num):
        series.append(recursive_fibanacci_sries(i))
    return series
while True:
        num=int(input("Enter a number for fibanacci series : "))  
        print("Fibanacci Series is:")
        print(recursive(num))
   