n=int(input("Enter a number : "))
temp=n
degree=len(str(n))
power_sum=0
while temp!=0:
    digit=temp%10
    power_sum=power_sum+digit**degree
    temp=temp//10
if power_sum==n:
    print(f"Given number {n} is Armstrong number ")
else:
    print(f"Given number {n} is not Armtrong number ")