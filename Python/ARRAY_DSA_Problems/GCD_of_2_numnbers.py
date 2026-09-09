a=int(input("Enter a numnber :"))
b=int(input("Enter a numnber :"))
while b!=0:
    a,b=b,a%b
print("GCD is ",a)