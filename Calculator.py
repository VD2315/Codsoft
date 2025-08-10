import tkinter as tk

def click(event):
    current = entry.get()
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief=tk.RIDGE, justify="right",
                 bg="#ffffff", fg="#333333")
entry.pack(padx=10, pady=10, fill="both")

button_frame = tk.Frame(root, bg="#f2f2f2")
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C"]
]

def get_button_color(text):
    if text.isdigit() or text == ".":
        return "#FFD9B3", "#000000"  # light orange
    elif text == "=":
        return "#4CAF50", "#ffffff"  # green
    elif text == "C":
        return "#FF6666", "#ffffff"  # red
    else:
        return "#D9D9D9", "#000000"  # light gray for operators

for row in buttons:
    row_frame = tk.Frame(button_frame, bg="#f2f2f2")
    row_frame.pack(expand=True, fill="both")
    for btn_text in row:
        bg_color, fg_color = get_button_color(btn_text)
        btn = tk.Button(row_frame, text=btn_text, font="Arial 18", height=2, width=5,
                        bg=bg_color, fg=fg_color, activebackground="#cccccc", relief=tk.RAISED)
        btn.pack(side="left", expand=True, fill="both")
        btn.bind("<Button-1>", click)

root.mainloop()
