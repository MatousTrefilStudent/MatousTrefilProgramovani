import tkinter as tk
import math

root = tk.Tk()
root.title("Kalkulačka")
root.geometry("300x500")

class Calculator:
    def __init__(self, system):
        self.system = system

        # Frame for the display label
        self.display_frame = tk.Frame(root)
        self.display_frame.pack(side="top", fill="x")

        self.display_var = tk.StringVar()
        self.display_label = tk.Label(self.display_frame, textvariable=self.display_var,
                                      font=("Arial", 24), anchor="e", bg="white")
        self.display_label.pack(fill="x", padx=5, pady=5)

        # Frame for the number buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side="top", fill="both", expand=True)

        self.create_number_keyboard()

    def new_system(self, system):
        # Clear old buttons
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        self.system = system
        self.create_number_keyboard()

    def create_number_keyboard(self):
        self.buttons = []
        grid_size = math.ceil(self.system ** 0.5)
        for i in range(self.system):
            self.buttons.append(NumberButton(i, self, grid_size))

        # Configure rows and columns to expand
        total_rows = math.ceil(self.system / grid_size)
        for i in range(total_rows):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for i in range(grid_size):
            self.button_frame.grid_columnconfigure(i, weight=1)


class NumberButton:
    def __init__(self, number, calculator, grid_size):
        self.number = number
        self.calculator = calculator

        self.button = tk.Button(calculator.button_frame, text=self.number, 
                                command=self.clicked)
        self.button.grid(
            row=number // grid_size,
            column=number % grid_size,
            sticky="nsew"
        )

    def clicked(self):
        # Update the display label
        self.calculator.display_var.set(str(self.number))
        # Example: recreate keyboard based on the clicked number
        self.calculator.new_system(self.number)


# Start calculator with 70 buttons
calc = Calculator(70)

root.mainloop()
