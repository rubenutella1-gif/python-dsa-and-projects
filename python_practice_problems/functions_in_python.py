# declaration of functions
""" def greet():
    print("Hello !")
greet() """
#  Function with parameters
""" def greet(name):
    print("Hello ",name)
greet("Rubenu") """
# Functions with return value
""" def sum(a,b):
    return a+b
print(sum(5,5)) """
""" def greet(name="user"):
    print("Hello !",name)
greet()
greet("Ramesh") """
#Keyword arguements in python can change the order of keywords
""" def fun1(name,age):
    print(f"My name is {name} and age is {age}")
fun1("Rubenu",22)
fun1(age=22,name="Ramesh")   """
# Arbitory Arguements
""" def fun1(*a):
    print("Total :",sum(a))
fun1(1,2,3,4,5) """
# Arbitory keyword arguements
""" def fun1(**a):
    print("User Details : ")
    for key,value in a.items():
        print(f"{key}:{value}")
fun1(user="Kiran",age=22,user1="Prabhas",age1=25) """
# lambda function
""" add=lambda a,b:a+b
print(add(5,6)) """
# square of a number using the lambda function
""" power=lambda a:a*a
print(power(int(input("Enter a number to print power : ")))) """
# using map() ,ethod in the lambda functions
# map() aplies each element in the list
""" num=[1,2,3,4,5,6]
squares=list(map(lambda x:x*x,num))
print(squares) """
# using the filter() method with the lambda function
""" num=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x:x%2==0,num))
print(even) """
# using sorted() with the lambda function (Anonimous function)
""" num=[(6,2),(5,2),(1,3)]
sorted_list=sorted(num,key=lambda x:x[0])
print(sorted_list) """  
# map() method without using the lambda function
""" def square(x):
    return  x*x
num=[1,2,3,4,5,6]
squares=list(map(square,num))
print(squares) """
# filter without using the lambda function
""" def is_even(x):
    return x%2==0
num=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(is_even,num))
print(evens) """
# Lambda function is a anonymous function it is used when there is function used one time in the program 
""" square=lambda x:x*x
print(square(int(input("Enter a number")))) """
# lambda funcrion using the map() method
""" num=[1,2,3,4,5,6,7,8,9,10]
squares=list(map(lambda x:x*x,num))
print(squares) """
# lambda function using the filter() method
""" num=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(lambda x:x%2==0,num))
print(evens) """
# lambda function using the sorted()
""" num=[1,2,4,1,4,54,1,4,5,7,10,2]
sorted_list=list(sorted(num,key=lambda x:x%10))
print(sorted_list)
sorted_list2=sorted(num)
print(sorted_list2)
 """