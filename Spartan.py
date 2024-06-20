import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

def spartan_cipher(text, key):
    calculation = math.ceil(len(text) / key)
    num_columns = key
    num_rows = calculation
    num_blanks = (num_columns * num_rows) - len(text)
    ciphertext = [''] * num_columns

    column = 0
    row = 0
    for char in text:
        ciphertext[column] += char
        column += 1
        if column == num_columns or (column == num_columns - 1 and row > num_rows - num_blanks):
            column = 0
            row += 1

    return ''.join(ciphertext)

def encrypt_button_click():
    plaintext = plaintext_entry.get()
    key = int(key_entry.get())
    ciphertext = spartan_cipher(plaintext, key)
    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(tk.END, ciphertext)

def decrypt_button_click():
    ciphertext = ciphertext_entry.get()
    key = int(key_entry.get())
    plaintext = decrypt_spartan_cipher(ciphertext, key)
    if plaintext:
        plaintext_entry.delete(0, tk.END)
        plaintext_entry.insert(tk.END, plaintext)
    else:
        messagebox.showerror("Decryption Error", "Invalid ciphertext or key.")

def decrypt_spartan_cipher(ciphertext, key):
    num_columns = key
    num_rows = math.ceil(len(ciphertext) / key)
    plaintext = [''] * num_rows

    column = 0
    row = 0
    for char in ciphertext:
        plaintext[row] += char
        row += 1
        if row == num_rows:
            row = 0
            column += 1

    return ''.join(plaintext)

# Create the main window
window = tk.Tk()
window.title("Spartan Cipher - Encryption and Decryption")
window.geometry("300x400")
window.configure(bg="#E8CFAF")  # Light brown color

# Create a style for labels
label_style = ttk.Style()
label_style.configure("LabelStyle.TLabel", background="#E8CFAF", foreground="#333333", font=("Arial", 15))

# Create the title label
title_label = ttk.Label(window, text="Spartan Cipher", style="TitleLabel.TLabel", font=("Arial", 20, "bold" , "italic"))
title_label.pack(pady=10)

# Create the labels and entry fields
plaintext_label = ttk.Label(window, text="Plaintext:", style="LabelStyle.TLabel")
plaintext_label.pack(pady=10)
plaintext_entry = ttk.Entry(window, font=("Arial", 12))
plaintext_entry.pack()

key_label = ttk.Label(window, text="Key Column:", style="LabelStyle.TLabel")
key_label.pack()
key_entry = ttk.Entry(window, font=("Arial", 12))
key_entry.pack(pady=10)

ciphertext_label = ttk.Label(window, text="Ciphertext:", style="LabelStyle.TLabel")
ciphertext_label.pack()
ciphertext_entry = ttk.Entry(window, font=("Arial", 12))
ciphertext_entry.pack(pady=10)

# Create a style for the encrypt button
button_style = ttk.Style()
button_style.configure("EncryptButton.TButton", font=("Arial", 12), background="#F3E5AB", borderwidth=0)  # Light gray button without border

# Create the encrypt button
encrypt_button = ttk.Button(window, text="Encrypt", command=encrypt_button_click, style="EncryptButton.TButton")
encrypt_button.pack(pady=10)

# Create the decrypt button
decrypt_button = ttk.Button(window, text="Decrypt", command=decrypt_button_click, style="EncryptButton.TButton")
decrypt_button.pack(pady=10)

# Apply a custom style to the entry fields
entry_style = ttk.Style()
entry_style.configure("TEntry", font=("Arial", 15))

# Apply a custom style to the title label
title_style = ttk.Style()
title_style.configure("TitleLabel.TLabel", background="#E8CFAF", font=("Arial", 20, "bold"))

# Start the main event loop
window.mainloop()
