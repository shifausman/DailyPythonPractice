#keypress
"""import tkinter as tk

def on_key(event):
    print(f"Key Pressed: {event.keysym}")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()

entry.bind("<KeyPress>", on_key)
root.mainloop()"""

#messagebox.showinfo
"""from tkinter import messagebox
messagebox.showinfo("Information", "This is an Info Dialog!")"""

#message.showerror
"""from tkinter import messagebox
messagebox.showerror("Error","Error occured")"""

#messagebox.askyesno
"""from tkinter import messagebox
response = messagebox.askyesno("Confirm", "Do you want to continue?")
if response:
    print("User clicked YES")
else:
    print("User clicked NO")"""

#messagebox.askokcancel
"""from tkinter import messagebox
response = messagebox.askokcancel("Confirm", "Do you want to proceed?")
if response:
    print("Proceeding...")
else:
    print("Cancelled")"""

