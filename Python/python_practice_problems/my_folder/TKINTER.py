#creating window by using the package tkinter
""" import tkinter as tk
window=tk.Tk()
#set title and width
window.title("My first window")
window.geometry("300x200")
#inserting image 
image=tk.PhotoImage(file="weather.png")
#creating label
label=tk.Label(window,text="Welcome to tkinter ",font=("Times New Roman",50,"italic"),fg="white",image=image,compound="center")
label.pack(pady=20)
label.image=image
#run the GUI
window.mainloop() """
# creating button using the tkinter package
""" import tkinter as tk
def greet():
    label.config(text="Hello Rubenu !")
window=tk.Tk()
window.title("My_first_button")
window.geometry("300x200")
label=tk.Label(window,text="Click the button",font=("Arial",85))
label.pack(pady=10)
button=tk.Button(window,text="Click me",command=greet,font=("Arial",30),bg="Yellow")
button.pack(pady=10)
window.mainloop() """
# creating the user input text by using the tkinter module
""" import tkinter as tk
def show_greet():
    name=entry.get()
    label.config(text=f"I LOVE {name} !")
window=tk.Tk()
window.title("User input text")
window.geometry("300x200")
entry=tk.Entry(window,font=("Arial",20))
entry.pack(pady=10)
label=tk.Label(window,text="Enter your name",font=("Arial",20))
label.pack(pady=10)
button=tk.Button(window,text="Submit",command=show_greet,font=("Arial",40))
button.pack(pady=10)
window.mainloop() """
# creating multi line text using the tkinter module
""" import tkinter as tk
def show_text():
    content=text_box.get("1.0","end-1c")
    label.config(text=f"You entered text is:\n{content}")
#creating window
window=tk.Tk()
window.title("Multi line text")
window.geometry("500x400")
#creating text area
text_box=tk.Text(window,height=5,width=40,font=("Times New Roman",20))
text_box.pack(pady=10)
#creating button 
button=tk.Button(window,text="Click Me",command=show_text,font=("Arial",20))
button.pack(pady=10)
#creating label for displaying the content 
label=tk.Label(window,text="",font=("Arial",20))
label.pack(pady=10)
#run the window
window.mainloop() """
# Creating check button using the tkinter module
""" import tkinter as tk
def show_status():
    if agree_var.get()==1:
        label.config(text="you are agreed to terms ")
    else:
        label.config(text="You are not agreed")
window=tk.Tk()
window.title("Checkbutton window")
window.geometry("300x200")
#variable to track check box state
agree_var=tk.IntVar()
#creating checkbutton
check_box=tk.Checkbutton(window,text="You are agreed",variable=agree_var,font=("Arial",15))
check_box.pack(pady=10)
#creating button to confirm
button=tk.Button(window,text="Submit",command=show_status,font=("Arial",15))
button.pack(pady=10)
#creating label to display the output
label=tk.Label(window,text="",font=("Arial",15))
label.pack(pady=10)
#run the coede
window.mainloop() """
#Creating multiple checkboxes
import tkinter as tk

def show_selection():
    selected = []
    if cheese_var.get():
        selected.append("Cheese")
    if tomato_var.get():
        selected.append("Tomato")
    if olives_var.get():
        selected.append("Olives")
    
    # Display result
    label.config(text="Selected Toppings:\n" + ", ".join(selected))

window = tk.Tk()
window.title("Pizza Toppings")
window.geometry("350x250")

# Variables to hold checkbox states
cheese_var = tk.IntVar()
tomato_var = tk.IntVar()
olives_var = tk.IntVar()

# Checkbuttons
tk.Checkbutton(window, text="Cheese", variable=cheese_var, font=("Arial", 12)).pack(anchor="w")
tk.Checkbutton(window, text="Tomato", variable=tomato_var, font=("Arial", 12)).pack(anchor="w")
tk.Checkbutton(window, text="Olives", variable=olives_var, font=("Arial", 12)).pack(anchor="w")

# Submit button
tk.Button(window, text="Submit", command=show_selection, font=("Arial", 12)).pack(pady=10)

# Label to display the selected items
label = tk.Label(window, text="", font=("Arial", 12))
label.pack()

window.mainloop()