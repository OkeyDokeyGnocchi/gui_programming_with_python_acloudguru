import tkinter as tk
import sys
from tkinter import messagebox

root = tk.Tk()
root.minsize(width=200, height=250)
root.resizable(width=False, height=False)


def display_message(func_name, **kwargs):
    def display():
        answer = getattr(sys.modules[messagebox.__name__], func_name)(**kwargs)
        if answer == True:
            print("You clicked something that returned True")
        elif answer == False:
            print("You clikced something that returned False")
        elif answer == "yes":
            print("You clicked something that returned 'yes'")
        elif answer == "no":
            print("You clicked something that returned 'no'")
        elif answer == None:
            print("You clicked something that returned None")
    
    return display

functions = [
    ("askokcancel", "askokcancel", messagebox.QUESTION),
    ("askquestion", "askquestion", messagebox.QUESTION),
    ("askretrycancel", "askretrycancel", messagebox.QUESTION),
    ("askyesno", "askyesno", messagebox.QUESTION),
    ("askyesnocancel", "askyesnocancel", messagebox.QUESTION),
    ("showerror", "showerror", messagebox.ERROR),
    ("showinfo", "showinfo", messagebox.INFO),
    ("showwarning", "showwarning", messagebox.WARNING),
]

for func, detail, icon in functions:
    button = tk.Button(
        root,
        text=f"Display {func}",
        command=display_message(
            func,
            title=f"Rendered {func}",
            message="Message goes here",
            icon=icon,
            detail=detail
        ),
    )
    button.pack()

root.mainloop()