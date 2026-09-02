n=int(input("Enter a number : "))
temp=n
reverse_num=0
while temp!=0:
    digit=temp%10
    reverse_num=reverse_num*10+digit
    temp=temp//10
print(reverse_num)