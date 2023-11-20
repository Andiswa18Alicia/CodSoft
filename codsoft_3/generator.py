import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_and_display():
    try:
        length = int(entry_length.get())

        if length <= 0:
            messagebox.showwarning("Invalid Input", "Password length must be greater than 0.")
        else:
            password = generate_password(length)
            messagebox.showinfo("Generated Password", f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid password length.")

window = tk.Tk()
window.title("Password Generator")


window.configure(bg='#89CFF0')


label_length = tk.Label(window, text="Enter the desired length of the password:")
label_length.pack(pady=10)

entry_length = tk.Entry(window)
entry_length.pack(pady=10)

button_generate = tk.Button(window, text="Generate Password", command=generate_password_and_display)
button_generate.pack(pady=20)

window.mainloop()
