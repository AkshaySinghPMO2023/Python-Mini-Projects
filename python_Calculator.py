import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.entry_var, justify='right', font=('Arial', 14))
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(master, text=text, command=lambda t=text: self.on_button_click(t), padx=10, pady=10)
            button.grid(row=row, column=col, sticky='nsew')

        # Configure row and column weights so that they expand proportionally
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def on_button_click(self, text):
        current_text = self.entry_var.get()

        if text == '=':
            try:
                result = eval(current_text)
                self.entry_var.set(result)
            except Exception as e:
                self.entry_var.set("Error")
        else:
            self.entry_var.set(current_text + text)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
