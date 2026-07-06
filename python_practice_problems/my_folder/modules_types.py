# importing the math module
#import math
""" print(math.sqrt(64))
print(math.pow(3,3))
print(math.factorial(5))
print(math.floor(5.9))
print(math.ceil(5.1))
print(math.pi) """
""" try:
    user_input=int(input("Enter a input"))
    if user_input<0:
        raise ValueError("Negative values not allowed")
except ValueError as e:
    print("Error:",e)
else:
    print(math.sqrt(user_input))
    print(math.pow(user_input,2))
    print(math.floor(user_input))
    print(math.ceil(user_input))
    print(math.pi)
    print(math.factorial(user_input)) """
#import random
""" name=input("Enter your name:")
print(f"Hello {name} play a guess game")
try:
    attempts=0
    while True:
        guess=int(input("Enter a number :"))
        guess_number=random.randint(1,5)
        attempts+=1
        if guess<1 or guess>5:
            raise ValueError(" Value must be in between 1,5")
        if guess==guess_number:
            print(f"Congratulations you guess the correct number in {attempts} attempts")
            break
        else:
            print("Wrong guess please try again !")
except ValueError as e:
    print("Error :",e) """
#datetime module
""" from datetime import datetime

# Get the current date and time
now = datetime.now()

# 1. Print date in DD-MM-YYYY format
print("Today's date:", now.strftime("%d-%m-%Y"))

# 2. Print the day of the week
print("Day of the week:", now.strftime("%A"))

# 3. Time-based greeting
hour = now.hour

if hour < 12:
    print("Good Morning!")
elif hour < 18:
    print("Good Afternoon!")
else:
    print("Good Evening!")
 """
# import os

# 1. Get and print current working directory
""" current_dir = os.getcwd()
print("📂 Current Working Directory:", current_dir)

# 2. Check if folder 'TestFolder' exists
folder_name = "TestFolder"

if not os.path.exists(folder_name):
    # 3. Create the folder if it doesn't exist
    os.mkdir(folder_name)
    print(f"✅ Folder '{folder_name}' created.")
else:
    print(f"📁 Folder '{folder_name}' already exists.")

# 4. List all files and folders in the current directory
print("\n📃 Files and Folders in Current Directory:")
items = os.listdir()
for item in items:
    print("-", item) """