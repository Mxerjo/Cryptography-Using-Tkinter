import tkinter as tk
from tkinter import ttk

def caesar_encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(message, key):
    return caesar_encrypt(message, -key)

def encrypt_decrypt_button_click():
    message = message_entry.get()
    shift = int(shift_entry.get())
    choice = encrypt_decrypt_var.get()

    if choice == 0:
        result = caesar_encrypt(message, shift)
        output_entry.delete(0, tk.END)
        output_entry.insert(tk.END, result)
    elif choice == 1:
        result = caesar_decrypt(message, shift)
        output_entry.delete(0, tk.END)
        output_entry.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher - Encryption and Decryption")
window.geometry("300x400")
window.configure(bg="#F3E5AB")

# Create a style for labels
label_style = ttk.Style()
label_style.configure("LabelStyle.TLabel", background="#F3E5AB", foreground="#333333", font=("Arial", 12))

# Create the title label
title_label = ttk.Label(window, text="Caesar Cipher", style="TitleLabel.TLabel", font=("Arial", 20, "bold" , "italic"))
title_label.pack(pady=10)

# Create the message label and entry field
message_label = ttk.Label(window, text="Plain Text:", style="LabelStyle.TLabel")
message_label.pack(pady=10)
message_entry = ttk.Entry(window, font=("Arial", 12))
message_entry.pack(pady=5)

# Create the shift label and entry field
shift_label = ttk.Label(window, text="Shifting:", style="LabelStyle.TLabel")
shift_label.pack()
shift_entry = ttk.Entry(window, font=("Arial", 12))
shift_entry.pack(pady=5)

# Create the encrypt/decrypt radio buttons
encrypt_decrypt_var = tk.IntVar()
encrypt_radio = ttk.Radiobutton(window, text="ENCRYPT", variable=encrypt_decrypt_var, value=0, style="TRadiobutton")
encrypt_radio.pack()
decrypt_radio = ttk.Radiobutton(window, text="DECRYPT", variable=encrypt_decrypt_var, value=1, style="TRadiobutton")
decrypt_radio.pack()

# Create the output label and entry field
output_label = ttk.Label(window, text="Result:", style="LabelStyle.TLabel")
output_label.pack(pady=10)
output_entry = ttk.Entry(window, font=("Arial", 12))
output_entry.pack(pady=5)

# Create the encrypt/decrypt button
encrypt_decrypt_button = ttk.Button(window, text="ENTER", command=encrypt_decrypt_button_click)
encrypt_decrypt_button.pack(pady=10)

# Apply a custom style to the radio buttons
radio_style = ttk.Style()
radio_style.configure("TRadiobutton", background="#F3E5AB", font=("Arial", 12))

# Apply a custom style to the title label
title_style = ttk.Style()
title_style.configure("TitleLabel.TLabel", background="#F3E5AB", font=("Arial", 20, "bold"))

# Start the main event loop
window.mainloop()
