try:
    income=int(input("Enter income of the user : "))
    expense1=input("Enter expense type : ")
    price1=int(input("Enter price of the expense : "))
    expense2=input("Enter expense type : ")
    price2=int(input("Enter price of the expense : "))
    print("Total income is :",income)
    if price2!=0 and price1!=0:
        print(f"Total expenses are : {price1+price2}")
    elif price1!=0:
        print(f"Total expense are : {price1}")
    elif price2!=0:
        print(f"Total expense are : {price1}")
    else:
        print("No expenses")
except:
    print("Invalid input :")
finally:
    savings=income-(price1+price2)
    print(f"Total savings are : {savings}")
    print("Analysis : ")
    print(f"{expense1} : {price1}")
    print(f"{expense2}: {price1}")