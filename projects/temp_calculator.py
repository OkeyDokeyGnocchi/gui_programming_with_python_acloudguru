import tkinter as tk

class App:
    def __init__(self, master):
        super().__init__()
        self.master = master

        temp_frame = tk.Frame(self.master)
        temp_frame.pack()
        self.temp_label = tk.Label(temp_frame, text="Temperature:")
        self.temp_label.pack(side="left")
        self.temp_entry = tk.Entry(temp_frame)
        self.temp_entry.pack(side="right")

        format_frame = tk.Frame(self.master)
        format_frame.pack()
        self.format_label = tk.Label(format_frame, text="Output Format: ")
        self.format_label.pack(side="left")

        radio_frame = tk.Frame(format_frame)
        radio_frame.pack(side="right")

        # TODO make the radio buttons actually matter
        self.format_celcius = tk.Radiobutton(radio_frame, text="Celcius")
        self.format_celcius.pack(side="left")
        self.format_fahrenheit = tk.Radiobutton(radio_frame, text="Fahrenheit")
        self.format_fahrenheit.pack(side="left")

        self.button =  tk.Button(self.master, text="Calculate")
        self.button.pack()
        self.results = tk.Label(self.master, text="")
        self.results.pack()


    def start(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.start()