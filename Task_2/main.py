import tkinter as tk

root = tk.Tk()
root.title("Easy Calculator")
root.geometry("300x350")
# Store numbers and operator
first_num = ""
operator = ""

# Display box
entry = tk.Entry(root, width=20, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4, pady=10)


# When number button is clicked
def number_click(num):
    entry.insert(tk.END, num)


# When + - * / is clicked
def operator_click(op):
    global first_num, operator
    first_num = entry.get()
    operator = op
    entry.delete(0, tk.END)


# Clear
def clear():
    entry.delete(0, tk.END)


# When = is clicked
def equal():
    second_num = entry.get()
    entry.delete(0, tk.END)

    if operator == "+":
        entry.insert(0, float(first_num) + float(second_num))
    elif operator == "-":
        entry.insert(0, float(first_num) - float(second_num))
    elif operator == "*":
        entry.insert(0, float(first_num) * float(second_num))
    elif operator == "/":
        if second_num == "0":
            entry.insert(0, "Error")
        else:
            entry.insert(0, float(first_num) / float(second_num))


# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('+',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('*',3,3),
    ('C',4,0), ('0',4,1), ('=',4,2), ('/',4,3),
]

for (text, row, col) in buttons:
    if text.isdigit():  # for numbers
        btn = tk.Button(root, text=text, width=5, height=2,
                        command=lambda t=text: number_click(t))
    elif text in "+-*/":  # operators
        btn = tk.Button(root, text=text, width=5, height=2,
                        command=lambda t=text: operator_click(t))
    elif text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, command=clear)
    elif text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, command=equal)

    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
