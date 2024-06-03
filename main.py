import tkinter as tk
from sympy import sympify, pi, sin, cos, tan, cot, sec, csc, asin, acos, atan, acot, asec, acsc, sinh, cosh, tanh, coth, sech, csch, asinh, acosh, atanh, acoth, asech, acsch, deg, limit, oo, diff, integrate, summation, Product, Symbol
import time

class ToolTip(object):
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        self.widget.bind("<Enter>", self.show_tip)
        self.widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event):
        x = y = 0
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, background="yellow", relief="solid", borderwidth=1, wraplength=200)
        label.pack(ipadx=1)

    def hide_tip(self, event):
        if self.tip_window:
            self.tip_window.destroy()
        self.tip_window = None

def insert_text(text):
    entry.insert(tk.END, text)

def solve_equation():
    equation = entry.get()
    try:
        result = sympify(equation)
        result_label.config(text=f"Решение: {result}")
    except Exception as e:
        result_label.config(text=f"Ошибка: {e}")

# Создание окна
root = tk.Tk()
root.title("Math Solver")

# Поле ввода
entry = tk.Entry(root, width=40)
entry.grid(row=0, column=0, columnspan=6, pady=10)

# Функция для создания кнопок с подсказками и примерами использования
def create_button(text, row, col, command=None, tooltip_text="", example_usage="", width=5):
    if not command:
        command = lambda: insert_text(text)
    button = tk.Button(root, text=text, command=command, width=width)
    button.grid(row=row, column=col)
    tooltip_full_text = f"{tooltip_text}\nПример: {example_usage}" if example_usage else tooltip_text
    ToolTip(button, tooltip_full_text)

# Кнопки цифр и операторов с подсказками
buttons = [
    ('(', 1, 0, None, "Открывающая скобка", ""),
    (')', 1, 1, None, "Закрывающая скобка", ""),
    ('7', 1, 2, None, "Цифра 7", ""),
    ('8', 1, 3, None, "Цифра 8", ""),
    ('9', 1, 4, None, "Цифра 9", ""),
    ('/', 1, 5, None, "Деление", "/(10,2)=5"),

    ('^', 2, 0, None, "Возведение в степень", "^(2,3)=8"),
    ('sqrt', 2, 1, lambda: insert_text('sqrt('), "Квадратный корень", "sqrt(16)=4"),
    ('4', 2, 2, None, "Цифра 4", ""),
    ('5', 2, 3, None, "Цифра 5", ""),
    ('6', 2, 4, None, "Цифра 6", ""),
    ('*', 2, 5, None, "Умножение", "*(5,2)=10"),

    ('x', 3, 0, None, "Переменная x", ""),
    ('y', 3, 1, None, "Переменная y", ""),
    ('1', 3, 2, None, "Цифра 1", ""),
    ('2', 3, 3, None, "Цифра 2", ""),
    ('3', 3, 4, None, "Цифра 3", ""),
    ('-', 3, 5, None, "Вычитание", "-(5,2)=3"),

    ('pi', 6, 0, lambda: insert_text('pi'), "Константа Пи", "pi=3.14"),
    ('%', 4, 3, None, "Процент", "%(100,5)=5"),
    ('0', 4, 0, None, "Цифра 0", ""),
    ('.', 4, 1, None, "Десятичная точка", ""),
    ('+', 4, 2, None, "Сложение", "+(3,2)=5"),

    ('deg', 6, 3, lambda: insert_text('deg('), "Градусы", "deg(π)=180"),
    ('sin', 7, 0, None, "Синус", "sin(π/2)=1"),
    ('cos', 7, 1, None, "Косинус", "cos(0)=1"),
    ('tan', 7, 2, None, "Тангенс", "tan(π/4)=1"),
    ('cot', 7, 3, None, "Котангенс", "cot(π/4)=1"),
    ('sec', 8, 0, None, "Секанс", "sec(0)=1"),
    ('csc', 8, 1, None, "Косеканс", "csc(π/2)=1"),
    ('asin', 8, 2, None, "Арксинус", "asin(1)=π/2"),
    ('acos', 8, 3, None, "Арккосинус", "acos(1)=0"),
    ('atan', 9, 0, None, "Арктангенс", "atan(1)=π/4"),
    ('acot', 9, 1, None, "Арккотангенс", "acot(1)=π/4"),
    ('asec', 9, 2, None, "Арксеканс", "asec(1)=0"),
    ('acsc', 9, 3, None, "Арккосеканс", "acsc(1)=π/2"),
    ('sinh', 10, 0, None, "Гиперболический синус", "sinh(0)=0"),
    ('cosh', 10, 1, None, "Гиперболический косинус", "cosh(0)=1"),
    ('tanh', 10, 2, None, "Гиперболический тангенс", "tanh(0)=0"),
    ('coth', 10, 3, None, "Гиперболический котангенс", "coth(1)=1.313"),
    ('sech', 11, 0, None, "Гиперболический секанс", "sech(0)=1"),
    ('csch', 11, 1, None, "Гиперболический косеканс", "csch(1)=0.850"),
    ('asinh', 11, 2, None, "Гиперболический арксинус", "asinh(0)=0"),
    ('acosh', 11, 3, None, "Гиперболический арккосинус", "acosh(1)=0"),
    ('atanh', 12, 0, None, "Гиперболический арктангенс", "atanh(0)=0"),
    ('acoth', 12, 1, None, "Гиперболический арккотангенс", "acoth(1)=∞"),
    ('asech', 12, 2, None, "Гиперболический арксеканс", "asech(1)=0"),
    ('acsch', 12, 3, None, "Гиперболический арккосеканс", "acsch(1)=∞"),
    ('lim', 13, 0, lambda: insert_text('limit('), "Предел", "lim(x->0)sin(x)/x=1"),
    ('lim+', 13, 1, lambda: insert_text('limit(,oo)'), "Предел справа", ""),
    ('lim-', 13, 2, lambda: insert_text('limit(,-oo)'), "Предел слева", ""),
    ('∞', 13, 3, lambda: insert_text('oo'), "Бесконечность", "1/∞=0"),
    ('diff', 14, 0, lambda: insert_text('diff('), "Производная", "diff(x^2)=2x"),
    ('∂', 14, 1, lambda: insert_text('diff('), "Частная производная", ""),
    ('∫', 14, 2, lambda: insert_text('integrate('), "Интеграл", "∫(x^2 dx)=x^3/3"),
    ('∫_a^b', 14, 3, lambda: insert_text('integrate(, (x, a, b))'), "Определенный интеграл", "∫(x^2 dx, 0, 1)=1/3"),
    ('Σ', 15, 0, lambda: insert_text('summation('), "Суммирование ряда", "Σ(n,( n, 1, 10))=55"),
    ('Π', 15, 1, lambda: insert_text('Product('), "Произведение ряда", "Π(n, n, 1, 4)=24")
]


# Debugging to identify the problematic tuple
for button in buttons:
    if len(button) != 6:
        print("Faulty button definition:", button)

# Assuming all button definitions are corrected now
for (text, row, col, command, tooltip_text, example_usage) in buttons:
    create_button(text, row, col, command, tooltip_text, example_usage)

# Кнопка для решения уравнения
solve_button = tk.Button(root, text="Решить", command=solve_equation, width=22)
solve_button.grid(row=16, column=0, columnspan=6, pady=10)

# Метка для отображения результата
result_label = tk.Label(root, text="")
result_label.grid(row=17, column=0, columnspan=6, pady=10)

root.mainloop()
