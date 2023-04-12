import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create display widget
        self.display = tk.Entry(master, width=25, justify="right", font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Define button labels and their positions
        button_labels = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "="
        ]
        button_positions = [(i, j) for i in range(1, 5) for j in range(4)]

        # Create buttons
        self.buttons = []
        for position, label in zip(button_positions, button_labels):
            row, column = position
            button = tk.Button(master, text=label, width=5, height=2, font=("Arial", 16),
                               command=lambda label=label: self.button_click(label))
            button.grid(row=row, column=column, padx=5, pady=5)
            self.buttons.append(button)

    def button_click(self, label):
        # Handle button clicks and update display
        if label == "C":
            self.display.delete(0, tk.END)
        elif label == "=":
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        else:
            self.display.insert(tk.END, label)

# Create and run the calculator app
root = tk.Tk()
app = Calculator(root)
root.mainloop()
