while True:
    a=int(input("Enter a value : "))
    b=int(input("Enter b value : "))
    x,y=a,b
    while y!=0:
        x , y=y , x % y
    GCD=x
    LCM=a*b//x
    print(f"GCD of {a,b} : {GCD}")
    print(f"LCM of {a,b} : {LCM}")