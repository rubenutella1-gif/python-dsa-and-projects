# Find Factorial
# Write a function to calculate the factorial of a number using both recursion and iteration.
def fact(num):
    if(num==1 or num==0):
        return 1
    result=1
    for i in range(1, num+1):
        result*=i
    return result
num=int(input("Enter a number"))
result1=fact(num)
print(f"Factorial of {num} is {result1}")    
        
