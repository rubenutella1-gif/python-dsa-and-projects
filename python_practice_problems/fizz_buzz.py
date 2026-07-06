# Logic and Condition-Based Problems
# FizzBuzz
# Print numbers from 1 to 100. For multiples of 3, print “Fizz”; for 5, print “Buzz”; for both, print “FizzBuzz”.
n=100
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print(i,"FizzBuzz")
    elif i%3==0:
        print(i,"Fizz")
    elif i%5==0:
        print(i,"Buzz")
    else:
        print(i)
    