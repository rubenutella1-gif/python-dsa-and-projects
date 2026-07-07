#Decaring class and objects and ithe __init__()("Constructor")
""" class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"Your name is {self.name} and age is {self.age}")
p1=Person("Rubenu",22)
p2=Person("Kiran",21)
p3=Person("Prabhas",23)
p1.display()
p2.display()
p3.display() """
#Declaring the class and creating class variable, object and the class method,static method 
""" class Student:
    school_name="ABC School"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("name :",self.name)
        print("age :",self.age)
        print("school name :",Student.school_name)
    #class method
    @classmethod
    def change_method(cls,new_name):
        cls.school_name=new_name
    #static method
    @staticmethod
    def is_passed(marks):
        return marks>=35
s1=Student("Rubenu",21)
s1.show()
Student.change_method("XYZ school")
s1.show()
print("Passed?",Student.is_passed(34)) """
#Basic program for constructor
""" class Book:
    def __init__(self,author,title):
        self.author=author
        self.title=title
    def display(self):
        print(f"Book : {self.title}, Author : {self.author}")
s1=Book("Poulo coelho","The Alchemist")
s1.display() """
#Create a class called Employee that:

#Takes emp_name and emp_salary in the constructor

#Has a method called show_details() that prints them
""" class Employe:
    def __init__(self,emp_name,emp_salary):
        self.emp_name=emp_name
        self.emp_salary=emp_salary
    def show_details(self):
        print(f"Name :{self.emp_name}, Salary : {self.emp_salary}")
s1=Employe("KIRAN",100000)
s1.show_details() """
#class variable and how to access it
""" class Bank_account:
    bank_name="SBI"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show_info(self):
        print(f"Name : {self.name}, Salary: {self.salary}")
    @classmethod
    def show_bank_name(cls):
        print(f"Bank_name : {Bank_account.bank_name}")
obj=Bank_account("Rubenu",100000)
obj.show_info()
Bank_account.show_bank_name() """
#Creating a class using the sytatic methods
""" class MathCheck:
    @staticmethod
    def is_positive(n):
        if n>0:
            return f"{n} is positive"
        return f"{n} is negative"
print(MathCheck.is_positive(0))
print(MathCheck.is_positive(2)) """
# Encapsulation one of the main piller of the OOPS concepts it binds the functions ,
# variables,methods and show the required output
""" class Accoount:
    def __init__(self,name,balance):
        self.__name=name
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print(f"Please enter valid amount")
    def get_balance(self):
        print(f"{self.__balance}, is the balance amount ")
        print(f"{self.__name}, is the account holder ")
obj=Accoount("Rubenu",50000)
obj.deposit(100000)
obj.get_balance() """
""" 📌 Create these three classes:
Person – base class

__init__(self, name)

Method: show_person()

Employee – inherits from Person

__init__(self, name, emp_id)

Method: show_employee()

Manager – inherits from Employee

__init__(self, name, emp_id, department)

Method: show_manager()

✅ Expected Output:
plaintext
Copy
Edit
Name: Rubenu
Employee ID: 101
Department: HR """
""" class Person:
    def __init__(self,name):
        self.name=name
    def show_person(self):
        print(f"Name : {self.name}")
class Employee(Person):
    def __init__(self, name,emp_id,department):
        super().__init__(name)
        self.emp_id=emp_id
        self.department=department
    def show_employee(self):
        print(f"Employee ID: {self.emp_id}\n Department : {self.department}")
class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id, department)
    def show_manager(self):
       self.show_person()
       self.show_employee()
obj=Manager("Rubenu",101,"HR")
obj.show_manager() """
#Polimorphism
""" class Shape:
    def area(self):
        print("Area formula not found ")
class Circle(Shape):
    def area(self):
        print("Area of Circle: π × r²")
class Square(Shape):
    def area(self):
        print("Area of Square: side × side")
for shape in (Shape(),Circle(),Square()):
    shape.area() """

# Abstraction 
""" from abc import ABC,abstractmethod
class BankAccount(ABC):
    @abstractmethod
    def account_type(self):
        pass
class SavingsAccount(BankAccount):
    def account_type(self):
        print("This is a Savings Account ")
class CurrentAccount(BankAccount):
    def account_type(self):
        print("This is a CurrentAccount ")
obj1=SavingsAccount()
obj2=CurrentAccount()
obj1.account_type()
obj2.account_type() """
# Abstraction method 
from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def check_balance(self):
        pass
class SBI_ATM(ATM):
    def __init__(self,starting_balance):
        self.balance=starting_balance
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance-=amount
            print(f"Withdraw amount Rs{amount}")
            print(f"After withdraw Current balance is Rs{self.balance}")
        else:
            print("Insufficient balance ")
    def check_balance(self):
        print(f"Current balance is Rs{self.balance}")
obj1=SBI_ATM(15000)
obj1.check_balance()
obj1.withdraw(5000)