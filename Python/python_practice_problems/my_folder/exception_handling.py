#1 Zero division error
""" try:
    n1=int(input("Enter a number"))
    n2=int(input("Enter a number"))
    print(n1/n2)
except ZeroDivisionError:
    print("Denominator cannot be zero") """
# Value error
""" try:
    num1=int(input("Enter a number "))
    num2=int(input("Enter a number "))
    print(num1+num2)
except ValueError:
    print("You entered wrong input ")
     """
#Using else and finally
""" while True:
    try:
        num = int(input("Enter a number greater than 5: "))
        if num <= 5:
            raise ValueError("Number must be greater than 5.")
    except ValueError as e:
        print("Error:", e)
    else:
        print("Good job! You entered:", num)
    finally:
        print("Program execution complete.")  """
#Using indexError
""" while True:
    my_list=[1,2,3]
    try:
        index=int(input("Enter index range (0-2) :"))
        print(my_list[index])
    except IndexError:
        print("Index number is out of range") 
    except ValueError:
        print("Please engter valid input ) """
#Custom exception
class InvalidAgeError(Exception):
    pass
try:
    Age=int(input("Enter your age :"))
    if Age<18 or Age>60:
        raise InvalidAgeError("Age must be between 18 and 60")
    print("You entered correct Age :",Age)
except InvalidAgeError as i:
    print("Error :",i)
except ValueError:
    print("You entered wrong input")