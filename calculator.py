import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.result_var = tk.StringVar()
        self.create_widgets()
        
    def create_widgets(self):
        # Display
        result_display = tk.Entry(self, textvariable=self.result_var, font=('Arial', 24), bd=10, relief="ridge", justify="right")
        result_display.grid(row=0, column=0, columnspan=4)
        
        # Button definitions
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0, 4)
        ]
        
        # Create buttons
        for (text, row, col, *span) in buttons:
            button = tk.Button(self, text=text, font=('Arial', 18), bd=5, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=(span[0] if span else 1), sticky="nsew")
        
        # Configure row and column weights
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set('')
        elif char == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)  # Use with caution!
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + char)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
