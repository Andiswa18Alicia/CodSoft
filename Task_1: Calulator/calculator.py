import tkinter as tk
from tkinter import PhotoImage

def add_digit(digit):
    current_text = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(0, current_text + digit)

def clear():
    entry_display.delete(0, tk.END)

def calculate():
    expression = entry_display.get()
    try:
        result = str(eval(expression))
        entry_display.delete(0, tk.END)
        entry_display.insert(0, result)
    except Exception:
        entry_display.delete(0, tk.END)
        entry_display.insert(0, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Load the background image
bg_image = PhotoImage(file="_calculator.png")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# the background image
background_label = tk.Label(window, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# label for the title
title_label = tk.Label(window, text="Simple Calculator", font=("Arial", 18, "bold"), bg="white")
title_label.place(relx=0.5, rely=0.05, anchor="n")

# Entry widget for displaying the expression
entry_display = tk.Entry(window, width=20, font=("Arial", 16))
entry_display.place(relx=0.5, rely=0.3, anchor="n")

# buttons for numbers and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 0, 0
button_frame = tk.Frame(window)
button_frame.place(relx=0.5, rely=0.5, anchor="n")

for button in buttons:
    if button == '=':
        tk.Button(button_frame, text=button, command=calculate, font=("Arial", 16)).grid(row=row, column=col, padx=10, pady=10)
    elif button == 'C':
        tk.Button(button_frame, text=button, command=clear, font=("Arial", 16)).grid(row=row, column=col, padx=10, pady=10)
    else:
        tk.Button(button_frame, text=button, command=lambda b=button: add_digit(b), font=("Arial", 16)).grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col > 3:
        col = 0
        row += 1

# window size to cover the entire screen
window.geometry(f"{screen_width}x{screen_height}")

# GUI event loop
window.mainloop()