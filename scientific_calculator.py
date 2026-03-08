import tkinter as tk
import math

def click(event):
    text = event.widget.cget("text")
    current = entry.get()

    if text == "=":
        try:
            expression = current.replace("^", "**")
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif text == "C":
        entry.delete(0, tk.END)

    elif text in ["sin", "cos", "tan", "log", "sqrt", "fact"]:
        try:
            num = float(current)
            entry.delete(0, tk.END)
            if text == "sin":
                entry.insert(tk.END, math.sin(math.radians(num)))
            elif text == "cos":
                entry.insert(tk.END, math.cos(math.radians(num)))
            elif text == "tan":
                entry.insert(tk.END, math.tan(math.radians(num)))
            elif text == "log":
                entry.insert(tk.END, math.log10(num))
            elif text == "sqrt":
                entry.insert(tk.END, math.sqrt(num))
            elif text == "fact":
                entry.insert(tk.END, math.factorial(int(num)))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    else:
        entry.insert(tk.END, text)


root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.configure(bg="#f0f0f0")

entry = tk.Entry(root, font="Arial 24", justify="right", bd=10, relief=tk.RIDGE)
entry.pack(fill=tk.BOTH, ipadx=8, pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/", "sqrt"],
    ["4", "5", "6", "*", "log"],
    ["1", "2", "3", "-", "sin"],
    ["0", ".", "=", "+", "cos"],
    ["C", "(", ")", "^", "tan"],
    ["fact"]
]

for row in buttons:
    r = tk.Frame(button_frame)
    r.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(r, text=btn, font="Arial 18", relief=tk.RAISED, bd=4)
        b.pack(side=tk.LEFT, expand=True, fill="both", padx=2, pady=2)
        b.bind("<Button-1>", click)

root.mainloop()
