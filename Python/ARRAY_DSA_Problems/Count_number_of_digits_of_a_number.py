n=int(input("Enter a number : "))
temp=n
count=0
while temp!=0:
    temp=temp//10
    count+=1
print(count)