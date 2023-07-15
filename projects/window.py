import os
import tkinter as tk

root = tk.Tk()
working_dir = os.path.dirname(__file__)

root.title("My Window")
root.iconphoto(True, tk.PhotoImage(file=working_dir + "\mgd_rule.png"))
root.geometry("500x300+200+200")
root.resizable(width=True, height=True)
root.minsize(width=500, height=300)
root.maxsize(width=1000, height=400)

button = tk.Button(
    root,
    background="#FF0000",
    activebackground="#FF0000",
    foreground="#00FF00",
    text="Press me",
    activeforeground="#0000FF"
)
button.pack(padx=30, pady=30)

root.mainloop()