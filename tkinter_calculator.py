import tkinter as tk


def button_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        current = screen.get()
        new = current + text
        screen.set(new)


root = tk.Tk()
root.title("Python")

screen = tk.StringVar()
entry = tk.Entry(root, textvariable=screen, font="lucida 20 bold", justify=tk.RIGHT)
entry.pack(fill=tk.X, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', 'C', 'C', 'C'
]

row = 0
col = 0
for button in buttons:
    btn = tk.Button(button_frame, text=button, font="lucida 15 bold", padx=20, pady=20)
    btn.grid(row=row, column=col)
    btn.bind("<Button-1>", button_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
    