import json
import os

from customer import Customer
from loan import Loan


DATA_FILE = "customers.json"

customers = []


def save_data():

    data = []

    for customer in customers:
        data.append(customer.to_dict())

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("\nData saved successfully.")

def load_data():

    global customers

    if not os.path.exists(DATA_FILE):

        customers = []
        return

    try:

        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        customers = []

        for customer_data in data:

            customer = Customer.from_dict(customer_data)

            customers.append(customer)

        print("\nData loaded successfully.")

    except json.JSONDecodeError:

        print("\nData file is empty or corrupted.")

        customers = []

def find_customer(customer_id):

    for customer in customers:

        if customer.customer_id == customer_id:
            return customer

    return None


def find_loan(customer, loan_id):

    for loan in customer.loans:

        if loan.loan_id == loan_id:
            return loan

    return None

def register_customer():

    print("\n----- Register Customer -----")

    customer_id = input("Enter Customer ID: ")

    # Check duplicate customer ID
    if find_customer(customer_id):

        print("\nCustomer ID already exists.")
        return

    name = input("Enter Name: ")

    try:

        age = int(input("Enter Age: "))

    except ValueError:

        print("\nAge must be a number.")
        return

    if age <= 0:

        print("\nAge must be greater than 0.")
        return

    mobile = input("Enter Mobile: ")

    address = input("Enter Address: ")

    customer = Customer(
        customer_id,
        name,
        age,
        mobile,
        address
    )

    customers.append(customer)

    save_data()

    print("\nCustomer registered successfully.")


def create_loan():

    print("\n----- Create Loan -----")

    customer_id = input("Enter Customer ID: ")

    customer = find_customer(customer_id)

    if customer is None:

        print("\nCustomer not found.")
        return

    loan_id = input("Enter Loan ID: ")

    # Check duplicate loan
    if find_loan(customer, loan_id):

        print("\nLoan ID already exists.")
        return

    try:

        loan_amount = float(
            input("Enter Loan Amount: ")
        )

        interest_rate = float(
            input("Enter Interest Rate (%): ")
        )

        tenure = int(
            input("Enter Tenure (years): ")
        )

    except ValueError:

        print("\nInvalid input.")
        return

    if loan_amount <= 0:

        print("\nLoan amount must be greater than 0.")
        return

    if interest_rate < 0:

        print("\nInterest rate cannot be negative.")
        return

    if tenure <= 0:

        print("\nTenure must be greater than 0.")
        return

    loan = Loan(
        loan_id,
        loan_amount,
        interest_rate,
        tenure
    )

    loan.calculate_emi()

    customer.add_loan(loan)

    save_data()

    print("\nLoan created successfully.")

    print(f"Loan ID : {loan.loan_id}")
    print(f"EMI     : ₹{loan.emi:.2f}")

def view_customers():

    if not customers:

        print("\nNo customers registered.")
        return

    print("\n----- All Customers -----")

    for customer in customers:

        customer.display()

        print(f"Loans : {len(customer.loans)}")


def view_customer_loans():

    print("\n----- View Customer Loans -----")

    customer_id = input("Enter Customer ID: ")

    customer = find_customer(customer_id)

    if customer is None:

        print("\nCustomer not found.")
        return

    customer.display()

    customer.show_loans()


def search_customer():

    print("\n----- Search Customer -----")

    customer_id = input("Enter Customer ID: ")

    customer = find_customer(customer_id)

    if customer is None:

        print("\nCustomer not found.")
        return

    customer.display()

    print(f"\nTotal Loans : {len(customer.loans)}")


def search_loan():

    print("\n----- Search Loan -----")

    customer_id = input("Enter Customer ID: ")

    customer = find_customer(customer_id)

    if customer is None:

        print("\nCustomer not found.")
        return

    loan_id = input("Enter Loan ID: ")

    loan = find_loan(customer, loan_id)

    if loan is None:

        print("\nLoan not found.")
        return

    loan.display()


def pay_emi():

    print("\n----- Pay EMI -----")

    customer_id = input("Enter Customer ID: ")

    customer = find_customer(customer_id)

    if customer is None:

        print("\nCustomer not found.")
        return

    loan_id = input("Enter Loan ID: ")

    loan = find_loan(customer, loan_id)

    if loan is None:

        print("\nLoan not found.")
        return

    loan.pay_emi()

    save_data()


def repayment_history():

    print("\n----- Repayment History -----")

    customer_id = input("Enter Customer ID: ")

    customer = find_customer(customer_id)

    if customer is None:

        print("\nCustomer not found.")
        return

    loan_id = input("Enter Loan ID: ")

    loan = find_loan(customer, loan_id)

    if loan is None:

        print("\nLoan not found.")
        return

    loan.show_repayment_history()

def loan_summary():

    print("\n----- Loan Summary -----")

    customer_id = input("Enter Customer ID: ")

    customer = find_customer(customer_id)

    if customer is None:

        print("\nCustomer not found.")
        return

    loan_id = input("Enter Loan ID: ")

    loan = find_loan(customer, loan_id)

    if loan is None:

        print("\nLoan not found.")
        return

    loan.loan_summary()


def menu():

    load_data()

    while True:

        print("\n")
        print("==========================================")
        print("          CREDITrack LOAN SYSTEM")
        print("==========================================")

        print("1. Register Customer")
        print("2. Create Loan")
        print("3. View All Customers")
        print("4. View Customer Loans")
        print("5. Search Customer")
        print("6. Search Loan")
        print("7. Pay EMI")
        print("8. Repayment History")
        print("9. Loan Summary")
        print("10. Save Data")
        print("11. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            register_customer()

        elif choice == "2":

            create_loan()

        elif choice == "3":

            view_customers()

        elif choice == "4":

            view_customer_loans()

        elif choice == "5":

            search_customer()

        elif choice == "6":

            search_loan()

        elif choice == "7":

            pay_emi()

        elif choice == "8":

            repayment_history()

        elif choice == "9":

            loan_summary()

        elif choice == "10":

            save_data()

        elif choice == "11":

            save_data()

            print("\nThank you for using CREDITrack.")

            break

        else:

            print("\nInvalid choice. Please try again.")

menu()