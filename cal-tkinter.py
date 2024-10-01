import tkinter as tk

def click(event):
    current = display.get()
    if event.widget.cget("text") == "=":
        try:
            result = eval(current)
            display.set(result)
        except Exception as e:
            display.set("Error")
    elif event.widget.cget("text") == "C":
        display.set("")
    else:
        display.set(current + event.widget.cget("text"))

root = tk.Tk()
root.title("Calculator")
display = tk.StringVar()

entry = tk.Entry(root, textvariable=display, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    btn = tk.Button(root, text=button, font=('Arial', 18), width=4)
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    btn.bind('<Button-1>', click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
