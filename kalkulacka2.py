from tkinter import *

# ---------------- LOGIKA ----------------
def button_press(value):
    global equation
    equation += str(value)
    display_var.set(equation)

def calculate(event=None):
    global equation
    try:
        result = str(eval(equation))
        display_var.set(result)
        equation = result
    except:
        display_var.set("Chyba")
        equation = ""

def clear(event=None):
    global equation
    equation = ""
    display_var.set("")

def backspace(event=None):
    global equation
    equation = equation[:-1]
    display_var.set(equation)

def key_input(event):
    if event.char in "0123456789+-*/.":
        button_press(event.char)

# ---------------- OKNO ----------------
window = Tk()
window.title("Kalkulačka")
window.geometry("400x520")
window.configure(bg="#1e1e1e")
window.resizable(False, False)

equation = ""
display_var = StringVar()

# ---------------- DISPLAY ----------------
display = Label(
    window,
    textvariable=display_var,
    font=("Segoe UI", 24),
    bg="#111",
    fg="white",
    anchor="e",
    padx=10,
    height=2
)
display.pack(fill="x", pady=10)

# ---------------- TLAČÍTKA ----------------
frame = Frame(window, bg="#1e1e1e")
frame.pack(expand=True, fill="both")

buttons = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
]

for text, row, col in buttons:
    Button(
        frame,
        text=text,
        font=("Segoe UI", 16),
        bg="#2d2d2d" if text.isdigit() else "#3a3a3a",
        fg="white",
        bd=0,
        command=lambda t=text: calculate() if t == "=" else button_press(t)
    ).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

Button(
    frame,
    text="AC",
    font=("Segoe UI", 16),
    bg="#b33a3a",
    fg="white",
    bd=0,
    command=clear
).grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# ---------------- GRID RESPONSIVE ----------------
for i in range(6):
    frame.rowconfigure(i, weight=1)
for i in range(4):
    frame.columnconfigure(i, weight=1)

# ---------------- KLÁVESNICE ----------------
window.bind("<Key>", key_input)
window.bind("<Return>", calculate)
window.bind("<BackSpace>", backspace)
window.bind("<Escape>", clear)

window.mainloop()
