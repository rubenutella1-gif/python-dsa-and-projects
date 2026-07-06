from datetime import datetime

Name=input("Enter your name:")
Lists='''
    "Rice"   :"Rs 50",
    "Sugar"  :"Rs 45",
    "Dal"    :"Rs 55",
    "Tea"    :"Rs 30",
    "Milk"   :"Rs 25",
    "Red"    :"Rs 35"
    '''
# print(Lists)
#List of items in the super market
items={
    "Rice"   : 50,
    "Sugar"  : 45,
    "Dal"    : 55,
    "Tea"    :30,
    "Milk"   : 25,
    "Red"    :35
    }
#Variables declarations
price=0
pricelist=[]
plist=[]
ilist=[]
qlist=[]
totalprice=0
finalprice=0
option=int(input("If you want to See list of items press 1 "))
if option==1:
    print(items)
else:
    pass
for i in range(len(items)):
    inp1=int(input("If you want to buy press 1 and for exit press 2  "))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter item :")
        quantity=int(input("Enter quantity :"))
        if item in items.keys():
            price=quantity*int((items[item]))
            pricelist.append((price,quantity,items,item))
            totalprice+=price
            plist.append(price)
            qlist.append(quantity)
            ilist.append(item)
            gst=(totalprice*5)/100
            FinalAmount=gst+totalprice
        else:
            print(" Sorry You entered items are not available !")
    else:
        print("You entered wrong number !")
    inp=input("Can I bill the items yes or no  ")
    if inp=="yes":
        pass
        if FinalAmount != 0:
            print("="*60)
            print(f"{'Rubenu Super Market':^60}")
            print(f"{'Nandigama':^60}")
            print("="*60)

            print(f"Name: {Name}")
            print(f"Date: {datetime.now()}")
            print("-"*60)

            # Header
            print(f"{'SNO':<5}{'ITEMS':<15}{'QUANTITY':<15}{'PRICE':<10}")
            print("-"*60)

            # Items
            for i in range(len(ilist)):
                print(f"{i:<5}{ilist[i]:<15}{qlist[i]:<15}{plist[i]:<10}")

            print("-"*60)
            print(f"{'Total Price:':<35}{totalprice}")
            print(f"{'GST (5%):':<35}{gst}")
            print(f"{'Final Amount:':<35}{FinalAmount}")
            print("="*60)