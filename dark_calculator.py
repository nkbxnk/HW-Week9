import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title(" Black & Red Calculator")
root.geometry("360x550")
root.configure(bg="#121212")
root.resizable(False, False)

entry = tk.Entry(
    root,
    font=("Consolas", 26),
    bg="#1E1E1E",
    fg="#FF3B3B",
    insertbackground="white",
    bd=0,
    justify="right"
)
entry.pack(fill="both", padx=15, pady=20, ipady=20)
frame = tk.Frame(root, bg="#121212")
frame.pack(expand=True, fill="both")

buttons = [
    ["C", "%", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "(", ")"]
]

for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        if text == "=":
            cmd = calculate
            bg = "#FF1E1E"
        elif text == "C":
            cmd = clear
            bg = "#8B0000"
        else:
            cmd = lambda t=text: click(t)
            bg = "#2B2B2B"

        btn = tk.Button(
            frame,
            text=text,
            command=cmd,
            font=("Arial", 18, "bold"),
            bg=bg,
            fg="white",
            activebackground="#FF4444",
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2"
        )

        btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)


for i in range(5):
    frame.rowconfigure(i, weight=1)

for i in range(4):
    frame.columnconfigure(i, weight=1)

root.mainloop()