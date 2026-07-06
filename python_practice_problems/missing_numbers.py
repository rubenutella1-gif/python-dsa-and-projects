# Find Missing Number in a Range
# Given a list of numbers from 1 to n with one number missing, find the missing number.
lst=[1,2,3,4,6,7,8]
n=8
sum=0
expected_sum=n*(n+1)//2
for i in lst:
    sum+=i
    missing=  expected_sum-sum  
print(missing)    