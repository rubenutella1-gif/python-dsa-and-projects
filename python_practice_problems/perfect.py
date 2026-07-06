# Check Perfect Number
# A perfect number is one whose sum of factors (excluding itself) equals the number. Check if a given number is perfect.
def is_perfect(num):
    if(num==0):
        return False
    result_sum=0
    for i in range(1,num):
        if num%i==0:
            result_sum+=i
    return result_sum==num   
def perfect_upto_n(n):
    perfect_numbers=[]
    for i in range(1,n+1):
        if is_perfect(i):
            perfect_numbers.append(i)
    return perfect_numbers
while True:
    n=int(input("Enter a number to print perfect numbers upto n = ")) 
    result=perfect_upto_n(n)  
    print(result)