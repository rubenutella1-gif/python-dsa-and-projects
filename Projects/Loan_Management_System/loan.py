from account import Account
from datetime import datetime


class Loan(Account):

    def __init__(self, loan_id, loan_amount, interest_rate, tenure,
                 loan_type="Personal Loan"):

        self.loan_id = loan_id
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.tenure = tenure
        self.loan_type = loan_type

        self.emi = 0
        self.balance = loan_amount
        self.status = "Active"
        self.paid_months = 0

        self.repayment_history = []

    # Display loan details
    def display(self):

        print("\n----- Loan Details -----")
        print(f"Loan ID       : {self.loan_id}")
        print(f"Loan Type     : {self.loan_type}")
        print(f"Loan Amount   : ₹{self.loan_amount:.2f}")
        print(f"Interest Rate : {self.interest_rate}%")
        print(f"Tenure        : {self.tenure} years")
        print(f"EMI           : ₹{self.emi:.2f}")
        print(f"Balance       : ₹{self.balance:.2f}")
        print(f"Status        : {self.status}")
        print(f"Paid Months   : {self.paid_months}")

    # Calculate EMI
    def calculate_emi(self):

        monthly_rate = self.interest_rate / (12 * 100)
        total_months = self.tenure * 12

        if monthly_rate == 0:

            self.emi = self.loan_amount / total_months

        else:

            self.emi = (
                self.loan_amount
                * monthly_rate
                * (1 + monthly_rate) ** total_months
            ) / (
                (1 + monthly_rate) ** total_months - 1
            )

        return self.emi

    # Pay one EMI
    def pay_emi(self):

        if self.status == "Closed":

            print("\nLoan is already closed.")
            return

        total_months = self.tenure * 12

        if self.paid_months >= total_months:

            self.status = "Closed"

            print("\nLoan tenure is completed.")
            return

        monthly_rate = self.interest_rate / (12 * 100)

        interest = self.balance * monthly_rate

        principal = self.emi - interest

        if principal > self.balance:
            principal = self.balance

        payment = interest + principal

        self.balance = self.balance - principal

        if self.balance < 0:
            self.balance = 0

        self.paid_months += 1

        if self.balance == 0:
            self.status = "Closed"

        payment_date = datetime.now().strftime("%d-%m-%Y")

        payment_details = {
            "emi_number": self.paid_months,
            "date": payment_date,
            "emi_amount": payment,
            "interest": interest,
            "principal": principal,
            "balance": self.balance
        }

        self.repayment_history.append(payment_details)

        print("\n----- EMI Payment -----")
        print(f"EMI Paid       : ₹{payment:.2f}")
        print(f"Date           : {payment_date}")
        print(f"Interest       : ₹{interest:.2f}")
        print(f"Principal      : ₹{principal:.2f}")
        print(f"Remaining      : ₹{self.balance:.2f}")
        print(f"Paid Months    : {self.paid_months}")
        print(f"Status         : {self.status}")

    # Show repayment history
    def show_repayment_history(self):

        if len(self.repayment_history) == 0:

            print("\nNo repayment history available.")
            return

        print("\n----- Repayment History -----")

        for payment in self.repayment_history:

            print(f"\nEMI Number : {payment['emi_number']}")
            print(f"Date       : {payment.get('date', 'Old Record')}")
            print(f"EMI Amount : ₹{payment['emi_amount']:.2f}")
            print(f"Interest   : ₹{payment['interest']:.2f}")
            print(f"Principal  : ₹{payment['principal']:.2f}")
            print(f"Balance    : ₹{payment['balance']:.2f}")

    # Total amount paid
    def get_total_paid(self):

        total = 0

        for payment in self.repayment_history:

            total += payment["emi_amount"]

        return total

    # Total interest paid
    def get_total_interest(self):

        total = 0

        for payment in self.repayment_history:

            total += payment["interest"]

        return total

    # Total principal paid
    def get_total_principal(self):

        total = 0

        for payment in self.repayment_history:

            total += payment["principal"]

        return total

    # Show loan summary
    def loan_summary(self):

        total_paid = self.get_total_paid()
        total_interest = self.get_total_interest()
        total_principal = self.get_total_principal()

        remaining_months = (self.tenure * 12) - self.paid_months

        if remaining_months < 0:
            remaining_months = 0

        print("\n----- Loan Summary -----")
        print(f"Loan ID              : {self.loan_id}")
        print(f"Loan Type            : {self.loan_type}")
        print(f"Original Loan Amount : ₹{self.loan_amount:.2f}")
        print(f"EMI                  : ₹{self.emi:.2f}")
        print(f"Total Paid           : ₹{total_paid:.2f}")
        print(f"Principal Paid       : ₹{total_principal:.2f}")
        print(f"Interest Paid        : ₹{total_interest:.2f}")
        print(f"Outstanding Balance  : ₹{self.balance:.2f}")
        print(f"Paid Months          : {self.paid_months}")
        print(f"Remaining Months     : {remaining_months}")
        print(f"Status               : {self.status}")

    # Close loan by paying full balance
    def close_loan(self):

        if self.status == "Closed":

            print("\nLoan is already closed.")
            return

        amount = self.balance
        payment_date = datetime.now().strftime("%d-%m-%Y")

        self.balance = 0
        self.status = "Closed"

        payment_details = {
            "emi_number": self.paid_months + 1,
            "date": payment_date,
            "emi_amount": amount,
            "interest": 0,
            "principal": amount,
            "balance": 0
        }

        self.repayment_history.append(payment_details)

        print("\n----- Full Loan Payment -----")
        print(f"Date          : {payment_date}")
        print(f"Amount Paid   : ₹{amount:.2f}")
        print(f"Remaining     : ₹0.00")
        print("Status        : Closed")

    # Convert loan object to dictionary
    def to_dict(self):

        return {
            "loan_id": self.loan_id,
            "loan_type": self.loan_type,
            "loan_amount": self.loan_amount,
            "interest_rate": self.interest_rate,
            "tenure": self.tenure,
            "emi": self.emi,
            "balance": self.balance,
            "status": self.status,
            "paid_months": self.paid_months,
            "repayment_history": self.repayment_history
        }

    # Create loan object from dictionary
    @classmethod
    def from_dict(cls, data):

        loan = cls(
            data["loan_id"],
            data["loan_amount"],
            data["interest_rate"],
            data["tenure"],
            data.get("loan_type", "Personal Loan")
        )

        loan.emi = data["emi"]
        loan.balance = data["balance"]
        loan.status = data["status"]
        loan.paid_months = data["paid_months"]

        loan.repayment_history = data.get(
            "repayment_history",
            []
        )

        return loan