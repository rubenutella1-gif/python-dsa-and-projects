#1. Print numbers from 1 to 10
'''n=1
while n<=10:
    print(n,end=" ")
    n+=1'''
#2. Sum of first n natural numbers
""" n=1
sum=0
while n<=50:
    sum+=n
    n+=1
print(f"Sum of n Natural Numbers are {sum}") """
# 3. Factorial of a number
""" user_input=int(input("Enter a number"))
fact=1
i=1
while i<=user_input:
    fact*=i
    i+=1
print(fact) """
#while loop
'''1. Print numbers from 1 to 10 using a while loop
(Expected Output: 1 2 3 ... 10)


2. Find the sum of all even numbers between 1 and 100
Hint: Use a counter to check even and add to sum.


3. Reverse a number
Input: 12345 → Output: 54321


4. Print a countdown from a given number to 1
Input: 5 → Output: 5 4 3 2 1


5. Keep taking input from the user until they type "exit"
Hint: while loop with input condition.'''
#1
'''n=1
while n<=10:
    print(n,end=" ")
    n+=1'''
#2
'''n=100
i=2
while i<=n:
    print(i,end=" ")
    i+=2'''
#3
'''n=input("Enter your input")
n_string=str(n)
rst=""
i=0
while i<len(n_string):
    rst=n_string[i]+rst
    i+=1
print(rst)'''
#4
'''user_input=int(input("Enter a number to count"))
i=1
while i<=user_input:
    print(user_input)
    user_input-=1'''
#5
'''
while True:
    user_input=input("Enter : ")
    if user_input.lower()=="exit":
        print("exited")
        break
    else:
        print("Enter valid input")'''
#6
# '''Sum of Digits Until Single Digit

# Input a number.

# Use while loop to keep summing the digits until you get a single digit.

# Inside loop, use for loop to extract each digit and use if to check condition.


# Example: 987 → 9+8+7=24 → 2+4=6'''
""" while True:
    n=int(input("Enter a number : "))
    while n>=10:
        total=0
        for digit in str(n):
            total+=int(digit)
        n=total
    print(f"Sum of each digit is {total}") """
#4. Print even numbers between 1 to 20
""" n=int(input("Enter a number"))
i=2
while i<=n:
    if i%2==0:
        print(i,end=" ")
    i+=1 """
#5. Reverse a number
""" num=int(input("Enter a number : "))
num_string=str(num)
i=0
rst=""
while i<len(num_string):
    rst=num_string[i]+rst
    i+=1
print("Reversed number is",rst) """
#6. Check if a number is a palindrome
""" num=int(input("Enter a number : "))
num_string=str(num)
i=0
rst=""
while i<len(num_string):
    rst=num_string[i]+rst
    i+=1
if int(rst)==num :
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome") """
# 7. Count the number of digits in a number
""" n=int(input("Enter A Number"))
n_string=str(n)
i=0
count=0
while i<len(n_string):
    count+=1
    i+=1
print(count) """
# 8. Check if a number is an Armstrong number
""" n=int(input("Enter a number : "))
n_string=str(n)
power=len(n_string)
i=0
armstrong=0
while i<len(n_string):
    digit=int(n_string[i])
    armstrong+=digit**power
    i+=1
if armstrong==n:
    print("Given number is armstrong ",n)
else:
    print("not a armstrong number ") """
# 9. Print digits of a number separately
""" n=int(input("Enter a number :"))
n_string=str(n)
i=0
lst=[]
while i<len(n_string):
    lst.append(int(n_string[i]))
    i+=1
print(lst) """
# 10. Find the sum of digits of a number
# n=int(input("Enter a number : "))
# string_n=str(n)
# i=0
# sum=0
# while i < len(string_n):
#     sum+=int(string_n[i])
#     i+=1
# print(sum)
# n=int(input("Enter a number : "))
# for i in range(1,n+1):
#     for j in range(i):
#        print("*",end=" ")
#     print()
# for i in range(n,0,-1):
#     for j in range(i-1):
#         print("*",end=" ")
#     print()
n=int(input("Enter  n value : "))
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
""" n=int(input("Enter a number : "))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
for i in range(2,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()  """
""" row=int(input("Enter rows : "))
for i in range(1,row+1):
    spaces=" "*(row-i)
    stars="*"*i
    print(spaces+stars)
for j in range(row-1,0,-1):
    spaces=" "*(row-j)
    stars="*"*j
    print(spaces+stars) """