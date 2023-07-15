import tkinter as tk

class App:
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.temp_val = tk.DoubleVar(self.master, 0.0)
        self.format_val = tk.IntVar(self.master, 0)
        self.result_val = tk.StringVar(self.master)

        self.temp_val.trace("w", self.convert_temp)
        self.format_val.trace("w", self.convert_temp)

        temp_frame = tk.Frame(self.master)
        temp_frame.pack()
        self.temp_label = tk.Label(temp_frame, text="Temperature:")
        self.temp_label.pack(side="left")
        self.temp_entry = tk.Entry(temp_frame, textvariable=self.temp_val)
        self.temp_entry.pack(side="right")

        format_frame = tk.Frame(self.master)
        format_frame.pack()
        self.format_label = tk.Label(format_frame, text="Output Format: ")
        self.format_label.pack(side="left")

        radio_frame = tk.Frame(format_frame)
        radio_frame.pack(side="right")

        self.format_celcius = tk.Radiobutton(
            radio_frame, text="Celcius", variable=self.format_val, value=0
        )
        self.format_celcius.pack(side="left")
        self.format_fahrenheit = tk.Radiobutton(
            radio_frame, text="Fahrenheit", variable=self.format_val, value=1
        )
        self.format_fahrenheit.pack(side="left")

        #self.button =  tk.Button(self.master, text="Calculate", command=self.convert_temp)
        #self.button.pack()
        self.results = tk.Label(self.master, textvariable=self.result_val)
        self.results.pack()


    def start(self):
        self.master.mainloop()

    def convert_temp(self, *args):
        try:
            input_value = self.temp_val.get()
        except tk.TclError:
            self.result_val.set("Invalid temperature value")
        else:
            if self.format_val.get() == 0:
                # Convert to celcius
                self.result_val.set(f"{round(input_value -32 * 5 / 9, 2)}°C")
            else:
                # Convert to fahrenheit
                self.result_val.set(f"{round(input_value * 9 / 5 + 32, 2)}°F")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    app.start()