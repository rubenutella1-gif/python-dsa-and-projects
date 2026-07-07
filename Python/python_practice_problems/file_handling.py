"""file=open("simple.txt","w")
file.write("Python is awesome /and it is used in many mnc companies\n")
file.write("Python is awesome /and it is used in many mnc companies2\n")
file.write("Python is awesome /and it is used in many mnc companies3\n")
file.write("Python is awesome /and it is used in many mnc companies4\n")
file.write("Python is awesome /and it is used in many mnc companies5\n")"""

""" file.close()
file=open("simple.txt","r")
print()
print(file.read())
print()
file.close() """
"""file=open("simple.txt","r")
print("Using the readline() :")
for line in file.readlines():
    print(line.strip())

file.close()
file1=open("simple.txt","w+")
file1.write("Rewriting the file")
file1.seek(0)
print(file1.read())
print(file.read())
file1.close()"""
""" file=open("practice.txt","w+")
file.write("Python is Powerful")
file.seek(0)
print(file.read())
file.close() """
# Clear the file first
""" with open("practice.txt", "w") as file:
    file.write("")  # Clear file content

# Now reopen in r+ mode
with open("practice.txt", "r+") as file:
    file.seek(0)
    lines = [line.strip() for line in file.readlines()]

    if "and fun to learn" not in lines:
        file.write("and fun to learn\n")

    file.seek(0)
    final_content = file.read()
    print(final_content)
    print("Occurrences:", final_content.count("and fun to learn"))   """ 
""" with open("sample.txt","w") as file:
    file.write("Python\n")
    file.write("Coding is awesome\n")
    file.write("Python is fun to learn\n")
with open("sample.txt","r") as file:
    file.seek(0)
    content=file.read()
    print("Using the read()")
    print(content) """
""" with open("data.txt","w") as file:
    file.write("Python is Powerful\n")
    file.write("It is easy to learn\n")
    file.write("File handling is interesting\n")
    file.write("Practice makes perfect\n")
with open("data.txt","r") as file:
    lines=file.readlines()
    file.seek(0)
    print(file.readline())
    print(len(lines)) """
""" with open("append.txt","a") as file:
    file.write("Hello world !\n")
with open("append.txt","r") as file:
    file.seek(0)
    print(file.read()) """
""" with open("apppend_plus.txt","a+") as file:
    file.write("python learning is awesome :\n")
    file.write("It is easy to learn :\n")
    file.seek(0)
    content=file.read()
    print("append method content is :\n",content) """
""" with open("apppend_plus.txt","w+") as file:
    file.write("python learning is awesome :\n")
    file.write("It is easy to learn :\n")
    file.seek(0)
    content=file.read()
    print("append method content is :\n",content) """
try:
    with open("practice2.txt","x") as f:
        f.write("Hello wolrd\n")
        f.write("python is easy to learn\n")
except FileExistsError:
    print("File already exist")
with open("practice2.txt","r") as f:
    content=f.read()
    print(content)