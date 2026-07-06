try:
    units=int(input("Enter no of units :"))
    if units<=100:
        charge=units*5
    elif units<=300:
        charge=(100*5)+(units-100)*7
    else:
        charge= (100*5)+(200*7)+(units-300)*10
    if charge>2000:
        print(f"Actual amount is {charge}")
        charge=charge-charge*0.05
        print(f"After discount Charge is :{charge}")
    else:
        print(charge)
except ValueError:
    print("Invalid input :")