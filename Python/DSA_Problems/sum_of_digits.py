n=int(input("Enter a number : "))
total=0
temp=n
while temp!=0:
    digit=temp%10
    total+=digit
    temp=temp//10
print("Sum of digit is : ",total)