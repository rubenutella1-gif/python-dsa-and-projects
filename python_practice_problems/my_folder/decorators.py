""" def my_decorate(func):
    def wrapper():
        print("********")
        func()
        print("********")
    return wrapper
@my_decorate
def show():
     print("Hello, Rubenu !")
show() """
def my_decorator(func):
    def wrapper(num):
        if num%2==0:
            func(num)
        else:
            print("Odd number not allowed ")
    return wrapper
@my_decorator
def process_number(n):
    print(f"Process number is {n}")
process_number(5)
process_number(8)