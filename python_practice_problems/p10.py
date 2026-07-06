try:
    a=int(input("Enter a value :"))
    b=int(input("Enter b value :"))
    total=0
    for i in range(a,b+1):
        total+=i*i*i
    print(total)
except:
    print("Invalid input ")