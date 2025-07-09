#button,entry
import tkinter as tk

root = tk.Tk()
root.title("Basic Widgets")

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=lambda: print("Submitted!"))
button.pack()

root.mainloop()

#label colouring
import tkinter as tk
root = tk.Tk()
w = tk.Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill=tk.X)
w = tk.Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill=tk.X)
w = tk.Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=tk.X)
tk.mainloop()

#multi label colouring , grid
import tkinter as tk

colours = ['red','green','orange','white','yellow','blue']
r = 0
for c in colours:
    tk.Label(text=c, relief=tk.RIDGE, width=15).grid(row=r,column=0)
    tk.Entry(bg=c, relief=tk.SUNKEN, width=10).grid(row=r,column=1)
    r = r + 1
tk.mainloop()"""

#simple addition program
"""from tkinter import *
def sum():
    a=int(ent1.get())
    b=int(ent2.get())
    s=a+b
    output.insert(1.0,str(s))    
win=Tk() #creating the main window and storing the window object in 'win'
win.title('Sum of Numbers')
win.geometry('300x200') #setting the size of the window
text=Label(win, text='Enter the numbers in the below fields and click Add')
ent1 = Entry(win) 
ent2 = Entry(win) 
btn=Button(win,text='Add',command=sum)
output=Text(win,height=1,width=6)
text.pack()
ent1.pack()
ent2.pack()
btn.pack()
output.pack()
win.mainloop()

#calculator
import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2
        elif operation == "mul":
            result = num1 * num2
        elif operation == "div":
            result = num1 / num2
        else:
            result = "Select operation"

        result_label.config(text="Result: " + str(result))
    except Exception as e:
        result_label.config(text="Error")

" Main window"
root = tk.Tk()
root.title("Radio Button Calculator")
root.geometry("300x300")

"Input fields"
tk.Label(root, text="Enter first number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

"Radio buttons for operations"
operation_var = tk.StringVar()
operation_var.set(None)

tk.Label(root, text="Select operation:").pack()
tk.Radiobutton(root, text="Add", variable=operation_var, value="add").pack()
tk.Radiobutton(root, text="Subtract", variable=operation_var, value="sub").pack()
tk.Radiobutton(root, text="Multiply", variable=operation_var, value="mul").pack()
tk.Radiobutton(root, text="Divide", variable=operation_var, value="div").pack()

"Calculate button"
tk.Button(root, text="Calculate", command=calculate).pack(pady=10)

"Result label"
result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()

#USERNAME AND PASWORD
import tkinter as tk
from tkinter import messagebox

def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if not username:
        messagebox.showwarning("Input Error", "Username cannot be empty.")
    elif not password:
        messagebox.showwarning("Input Error", "Password cannot be empty.")
    elif len(password) < 6:
        messagebox.showwarning("Input Error", "Password must be at least 6 characters long.")
    else:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")

# Main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x250")

# Username field
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

# Password field
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Login button
tk.Button(root, text="Login", command=validate_login).pack(pady=20)

root.mainloop()

#TEMPERATURE CONVERTER
import tkinter as tk
from tkinter import messagebox

def convert_temp():
    try:
        temp = float(entry.get())
        unit = temp_var.get()

        if unit == "CtoF":
            result = (temp * 9/5) + 32
            result_label.config(text=f"{temp}°C = {result:.2f}°F")
        elif unit == "FtoC":
            result = (temp - 32) * 5/9
            result_label.config(text=f"{temp}°F = {result:.2f}°C")
        else:
            messagebox.showwarning("Selection Error", "Please select a conversion type.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# GUI setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x250")

tk.Label(root, text="Enter Temperature:").pack(pady=5)
entry = tk.Entry(root)
entry.pack()

# Radio buttons for selecting conversion
temp_var = tk.StringVar()
tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=temp_var, value="CtoF").pack(pady=2)
tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=temp_var, value="FtoC").pack(pady=2)

# Convert button
tk.Button(root, text="Convert", command=convert_temp).pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result will be shown here", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()














