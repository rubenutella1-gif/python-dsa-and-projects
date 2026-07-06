try:
    n=int(input().strip())
    if n==0:
        print("0 fee")
    elif n==1:
        print("2000")
    elif n==3:
        print("5000")
    elif n==6:
        print("9000")
    elif n==9:
        print("12000")
    elif n==12:
        print("15000")
    else:
        print("Error")
except:
    print("Error")