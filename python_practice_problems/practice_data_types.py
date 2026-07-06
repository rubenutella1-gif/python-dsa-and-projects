# 1  what will be the output of the following code
""" my_list=[1,2,3,4,5]
print(my_list[1:4]) """#[2, 3, 4]

# 2 fill in the blank that add 'apple' to the end of the list
""" friuts=['banana','orange']
friuts.append('apple')
print(friuts)  """# ['banana', 'orange', 'apple']
# 3 which method you choose to remove last element in list
""" friuts=['banana','orange']
friuts.pop()
print(friuts) """# ['banana']
# 4 what will be the output of the following code
""" numbers=[1,2,3]
numbers.extend([4,5])
print(len(numbers)) """ # 5
#5 write a code to find maximum value in a list
""" lst1=[45,78,12,67,34]
print(max(lst1)) """# 78
# strings
#6 what will be the output of the followig code
""" text="Hello world"
print(text[0:5]) """# Hello
#7 Fill in the to convert string into uppercase
""" message="python programming"
upper_message=message.upper()
print(upper_message) """# PYTHON PROGRAMMING
#8 which string method splits a string into list
""" text="Hello world"
text.split()
print(text) """# Hello world
#9 what will be the output
""" name='Alice'
age=21
print(f"My name is {name} and I am {age} years old") """# My name is Alice and I am 21 years old
# 10  write a code to count how many times that letter a present in the string "Banana"
""" a="Banana"
a.lower()
print(a.count('a')) """# 3 Times
# Tuples
# 11 what is the main difference between list and tiuple
""" Tuples are immutable and the lists are mutable
"""
# 12 what will be the output of the following
""" my_tuple=(1,2,3,4,5)
print(my_tuple[2]) """ # 3
# 13 Fill in the blank to creat a tuple that has one element in it
""" single_tuple=(5,)
print(single_tuple)
print(type(single_tuple)) """# comma is neccesary because without comma it take it as a integer
# 14 what will happen if tryu to execute this code
""" colours=('red','blue','green')
colours[1]='yellow'
print(colours) """# It will cause type error
# 15 write a code to convert tuple into a list
""" tup1=(1,2,3,4,5,6)
tup1=list(tup1)
print(tup1) """# [1, 2, 3, 4, 5, 6]
# Dictionary
# 16 What will be the output 
""" student={'name':'john','age':20,'grade':'A'}
print(student["name"]) """# john
# 17 Fill in the blank to add new key value pair in dictionary
""" person = {'name': 'Alice', 'age': 30}
person['role']='Engineer'
print(person) """ # {'name': 'Alice', 'age': 30, 'role': 'Engineer'}
# 18 Which method return all the key in a dictionary
# dictionary_name.key() to return all the keys in a dictionary
""" dict1={'name': 'Alice', 'age': 30, 'role': 'Engineer'}
print(dict1.keys()) """#dict_keys(['name', 'age', 'role'])
# 19 what will be the output of the following
""" scores = {'math': 85, 'science': 92, 'english': 78}
print(len(scores)) """ # 3
# 20 write a code to get value for key 'city' from a dictionary called 'address'
# , with a default value of 'unknown' if the key does not exist
""" address={
    'house_no':5-200,
    'city':'Nandigama',
    'p.no':8639591117
}
print(address.get("city"))
print(address.get("city1","Unknown")) """
