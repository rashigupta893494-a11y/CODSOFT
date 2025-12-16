import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Enter a positive number")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
    
    except ValueError:
        messagebox.showerror("Error", "Please enter a number")

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.config(bg="#f0a500")  # Background color

# Label
tk.Label(root, text="Enter password length:", bg="#f0a500", font=("Arial", 12)).pack(pady=10)

# Entry box
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Button
tk.Button(root, text="Generate Password", command=generate_password,
          bg="#ff5733", fg="white", font=("Arial", 12)).pack(pady=10)

# Result label
result_label = tk.Label(root, text="", bg="#f0a500", fg="blue", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
