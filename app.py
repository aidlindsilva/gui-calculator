import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x450")
        self.root.configure(bg="#1e1e2e")  # Dark theme background

        self.expression = ""

        # Display Screen
        self.display = tk.Entry(
            root, 
            font=("Arial", 24), 
            bd=0, 
            bg="#252538", 
            fg="#ffffff", 
            justify="right"
        )
        self.display.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

        # Button Layout Configuration
        button_frame = tk.Frame(root, bg="#1e1e2e")
        button_frame.pack(fill="both", expand=True)

        buttons = [
            'C', '(', ')', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', ''
        ]

        # Grid layout generation
        row = 0
        col = 0
        for button in buttons:
            if button == '':
                continue
                
            # Differentiate button colors for styling
            if button in ['C', '(', ')', '/', '*', '-', '+', '=']:
                bg_color = "#ff9e3b" if button == "=" else "#313244"
                fg_color = "#ffffff"
            else:
                bg_color = "#45475a"
                fg_color = "#ffffff"

            action = lambda x=button: self.on_button_click(x)
            
            btn = tk.Button(
                button_frame, text=button, font=("Arial", 18), bd=0,
                bg=bg_color, fg=fg_color, activebackground="#585b70",
                activeforeground="#ffffff", command=action
            )
            
            # Special spanning for the grid if needed, otherwise standard 1x1 grid
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Make buttons resize proportionally with window adjustments
        for i in range(5):
            button_frame.rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.update_display()
        elif char == '=':
            try:
                # eval handles mathematical string evaluation safely here as input is restricted to buttons
                result = str(eval(self.expression))
                self.expression = result
                self.update_display()
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.expression = ""
                self.update_display()
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.expression = ""
                self.update_display()
        else:
            self.expression += str(char)
            self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()