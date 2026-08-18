from loan import Loan


class Customer:

    def __init__(self, customer_id, name, age, mobile, address):

        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.mobile = mobile
        self.address = address

        self.loans = []

    # Display customer details
    def display(self):

        print("\n----- Customer Details -----")
        print(f"Customer ID : {self.customer_id}")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Mobile      : {self.mobile}")
        print(f"Address     : {self.address}")

    # Add loan
    def add_loan(self, loan):

        self.loans.append(loan)

    # Display all loans
    def show_loans(self):

        if not self.loans:
            print("\nNo loans found.")
            return

        print("\n----- Customer Loans -----")

        for loan in self.loans:
            loan.display()

    # Convert Customer object to dictionary
    def to_dict(self):

        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "age": self.age,
            "mobile": self.mobile,
            "address": self.address,
            "loans": [
                loan.to_dict()
                for loan in self.loans
            ]
        }

    # Convert dictionary back to Customer object
    @classmethod
    def from_dict(cls, data):

        customer = cls(
            data["customer_id"],
            data["name"],
            data["age"],
            data["mobile"],
            data["address"]
        )

        for loan_data in data.get("loans", []):

            loan = Loan.from_dict(loan_data)

            customer.add_loan(loan)

        return customer