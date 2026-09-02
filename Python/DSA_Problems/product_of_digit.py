n=int(input("Enter a number : "))
product=1
temp=n
while temp!=0:
    digit=temp%10
    product=product*digit
    temp=temp//10
print("Sum of digit is : ",product)