# Lesson: Building a Simple GUI App with Tkinter

import tkinter as tk

greeting_count = 1

root = tk.Tk()
label = tk.Label(root, text="")

def set_message():
    global greeting_count
    label["text"] = f"Hello!\n You've clicked the button ({greeting_count}) times!"
    greeting_count += 1

button = tk.Button(root, text="Greet", command=set_message)

button.pack()
label.pack()

root.mainloop()