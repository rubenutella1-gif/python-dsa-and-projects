""" #Your computer is like a big room.
Files are papers.
Directories are drawers.
You put papers into drawers to keep them neat. """
#Creating directory
#Getting the current dictoinary of the file
""" import os
print("Current directory :",os.getcwd())
try:
    os.mkdir("my_folder")
    print("Folder created successfully ")
except FileExistsError:
    print("File already exist ")
os.chdir("my_folder")
print("NOw inside :",os.getcwd()) """
""" import os
items=os.listdir()
for item in items:
    print(item) """