try:
    m=int(input("Enter m value :"))
    n=int(input("Enter n value :"))
    total=0
    for i in range(m,n+1):
        total+=i
    print(total)
except:
    print("Invalid input :")