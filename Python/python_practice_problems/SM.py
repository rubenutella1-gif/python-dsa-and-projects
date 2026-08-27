from datetime import datetime

Name = input("Enter your name: ")

items = {
    "Rice": 50,
    "Sugar": 45,
    "Dal": 55,
    "Tea": 30,
    "Milk": 25,
    "Red": 35
}

totalprice = 0
ilist = []
qlist = []
plist = []

option = int(input("If you want to see the list of items press 1: "))

if option == 1:
    print("\nAvailable Items:")
    for item, price in items.items():
        print(f"{item:<10} Rs {price}")

while True:

    inp1 = int(input("\nIf you want to buy press 1 and for exit press 2: "))

    if inp1 == 2:
        break

    elif inp1 == 1:

        item = input("Enter item: ").title()
        quantity = int(input("Enter quantity: "))

        if item in items:

            price = quantity * items[item]

            totalprice += price

            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)

            print(f"{item} added to your bill.")
            print(f"Price: Rs {price}")

        else:
            print("Sorry, the item is not available!")

    else:
        print("You entered a wrong number!")

gst = (totalprice * 5) / 100
FinalAmount = totalprice + gst

if totalprice > 0:

    print("\n" + "=" * 60)
    print(f"{'Rubenu Super Market':^60}")
    print(f"{'Nandigama':^60}")
    print("=" * 60)

    print(f"Name: {Name}")
    print(f"Date: {datetime.now()}")

    print("-" * 60)

    print(f"{'SNO':<5}{'ITEMS':<15}{'QUANTITY':<15}{'PRICE':<10}")
    print("-" * 60)

    for i in range(len(ilist)):
        print(f"{i + 1:<5}{ilist[i]:<15}{qlist[i]:<15}{plist[i]:<10}")

    print("-" * 60)

    print(f"{'Total Price:':<35}Rs {totalprice:.2f}")
    print(f"{'GST (5%):':<35}Rs {gst:.2f}")
    print(f"{'Final Amount:':<35}Rs {FinalAmount:.2f}")

    print("=" * 60)

else:
    print("\nNo items purchased.")