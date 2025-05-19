import tkinter as tk
from tkinter import ttk, messagebox
import math

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator")
        self.geometry("420x600")
        self.resizable(False, False)
        self.configure(bg="#222831")
        self.expression = ""
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        # Display
        self.display_var = tk.StringVar()
        self.display = tk.Entry(self, textvariable=self.display_var, font=("Consolas", 22), bd=0, bg="#393e46", fg="#eeeeee", justify='right')
        self.display.place(x=10, y=10, width=400, height=50)

        # History
        self.history_label = tk.Label(self, text="History", font=("Consolas", 12), bg="#222831", fg="#00adb5")
        self.history_label.place(x=10, y=70)
        self.history_box = tk.Listbox(self, font=("Consolas", 11), bg="#393e46", fg="#eeeeee", height=7)
        self.history_box.place(x=10, y=100, width=400, height=120)

        # Buttons
        btns = [
            ['7', '8', '9', '/', 'sin'],
            ['4', '5', '6', '*', 'cos'],
            ['1', '2', '3', '-', 'tan'],
            ['0', '.', '(', ')', '+'],
            ['sqrt', 'log', 'ln', '^', 'C'],
            ['pi', 'e', 'Ans', '=', 'Del']
        ]
        for i, row in enumerate(btns):
            for j, btn in enumerate(row):
                action = lambda x=btn: self.on_button_click(x)
                b = tk.Button(self, text=btn, font=("Consolas", 15), bd=0, bg="#00adb5", fg="#222831", command=action, activebackground="#393e46", activeforeground="#00adb5")
                b.place(x=10 + j*80, y=240 + i*55, width=75, height=50)

    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display_var.set("")
        elif char == 'Del':
            self.expression = self.expression[:-1]
            self.display_var.set(self.expression)
        elif char == '=':
            try:
                result = self.safe_eval(self.expression)
                self.history.append(f"{self.expression} = {result}")
                self.update_history()
                self.display_var.set(str(result))
                self.expression = str(result)
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
        elif char == 'Ans':
            if self.history:
                last = self.history[-1].split('=')[-1].strip()
                self.expression += last
                self.display_var.set(self.expression)
        elif char == 'pi':
            self.expression += str(math.pi)
            self.display_var.set(self.expression)
        elif char == 'e':
            self.expression += str(math.e)
            self.display_var.set(self.expression)
        elif char == 'sqrt':
            self.expression += "sqrt("
            self.display_var.set(self.expression)
        elif char == 'log':
            self.expression += "log10("
            self.display_var.set(self.expression)
        elif char == 'ln':
            self.expression += "log("
            self.display_var.set(self.expression)
        elif char == '^':
            self.expression += "**"
            self.display_var.set(self.expression)
        elif char in ['sin', 'cos', 'tan']:
            self.expression += f"{char}("
            self.display_var.set(self.expression)
        else:
            self.expression += char
            self.display_var.set(self.expression)

    def update_history(self):
        self.history_box.delete(0, tk.END)
        for item in self.history[-7:]:
            self.history_box.insert(tk.END, item)

    def safe_eval(self, expr):
        # Allowed names
        allowed_names = {
            k: v for k, v in math.__dict__.items() if not k.startswith("__")
        }
        allowed_names['sqrt'] = math.sqrt
        allowed_names['log10'] = math.log10
        allowed_names['log'] = math.log
        allowed_names['pi'] = math.pi
        allowed_names['e'] = math.e
        return eval(expr, {"__builtins__": {}}, allowed_names)

if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()