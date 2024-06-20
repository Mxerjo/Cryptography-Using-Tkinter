import tkinter as tk
from tkinter import ttk
import re

def create_playfair_matrix(keyword):
    keyword = re.sub(r'[^A-Z]', '', keyword.upper())
    keyword = re.sub(r'J', 'I', keyword)
    keyword = ''.join(dict.fromkeys(keyword))
    alphabet = ''.join(chr(65 + i) for i in range(26) if chr(65 + i) != 'J' and chr(65 + i) not in keyword)
    matrix = [keyword[i:i+5] for i in range(0, len(keyword), 5)]
    for char in alphabet:
        if char not in keyword:
            matrix[-1] += char
            if len(matrix[-1]) == 5:
                matrix.append('')
    return matrix

def find_position(matrix, char):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(message, keyword):
    matrix = create_playfair_matrix(keyword)
    message = re.sub(r'[^A-Z]', '', message.upper())
    message = re.sub(r'J', 'I', message)
    if len(message) % 2 != 0:
        message += 'X'
    encrypted_message = ""
    for i in range(0, len(message), 2):
        char1, char2 = message[i], message[i+1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        if row1 == row2:
            encrypted_char1 = matrix[row1][(col1 + 1) % 5]
            encrypted_char2 = matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            encrypted_char1 = matrix[(row1 + 1) % 5][col1]
            encrypted_char2 = matrix[(row2 + 1) % 5][col2]
        else:
            encrypted_char1 = matrix[row1][col2]
            encrypted_char2 = matrix[row2][col1]
        encrypted_message += encrypted_char1 + encrypted_char2
    return encrypted_message

def playfair_decrypt(message, keyword):
    matrix = create_playfair_matrix(keyword)
    decrypted_message = ""
    for i in range(0, len(message), 2):
        char1, char2 = message[i], message[i+1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)
        if row1 == row2:
            decrypted_char1 = matrix[row1][(col1 - 1) % 5]
            decrypted_char2 = matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_char1 = matrix[(row1 - 1) % 5][col1]
            decrypted_char2 = matrix[(row2 - 1) % 5][col2]
        else:
            decrypted_char1 = matrix[row1][col2]
            decrypted_char2 = matrix[row2][col1]

        # Handle the replacement of 'I' with 'J'
        if decrypted_char1 == 'I':
            decrypted_char1 = 'J'
        if decrypted_char2 == 'I':
            decrypted_char2 = 'J'

        decrypted_message += decrypted_char1 + decrypted_char2
    return decrypted_message

def encrypt_button_click():
    message = plaintext_entry.get()
    keyword = keyword_entry.get()

    result = playfair_encrypt(message, keyword)
    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(tk.END, result)

def decrypt_button_click():
    message = ciphertext_entry.get()
    keyword = keyword_entry.get()

    result = playfair_decrypt(message, keyword)
    plaintext_entry.delete(0, tk.END)
    plaintext_entry.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Playfair Cipher - Encryption and Decryption")
window.resizable(False, False)

# Set the window background color
window.configure(background="#E1F3D8")

# Create and configure the frame
frame = ttk.Frame(window, padding="50", style="CustomFrame.TFrame")
frame.grid(column=0, row=0)

# Create and configure the title label
title_label = ttk.Label(frame, text="Playfair Cipher", style="TitleLabel.TLabel")
title_label.grid(column=0, row=0, columnspan=2, pady=10)

# Create and configure the labels
plaintext_label = ttk.Label(frame, text="Plaintext:", style="CustomLabel.TLabel")
plaintext_label.grid(column=0, row=1, sticky="W")

ciphertext_label = ttk.Label(frame, text="Ciphertext:", style="CustomLabel.TLabel")
ciphertext_label.grid(column=0, row=2, sticky="W")

keyword_label = ttk.Label(frame, text="Keyword:", style="CustomLabel.TLabel")
keyword_label.grid(column=0, row=3, sticky="W")

# Create and configure the entry fields
plaintext_entry = ttk.Entry(frame, width=30)
plaintext_entry.grid(column=1, row=1, padx=5, pady=5)

ciphertext_entry = ttk.Entry(frame, width=30)
ciphertext_entry.grid(column=1, row=2, padx=5, pady=5)

keyword_entry = ttk.Entry(frame, width=30)
keyword_entry.grid(column=1, row=3, padx=5, pady=5)

# Create and configure the buttons
encrypt_button = ttk.Button(frame, text="Encrypt", command=encrypt_button_click, style="CustomButton.TButton")
encrypt_button.grid(column=0, row=4, columnspan=2, padx=5, pady=10)

decrypt_button = ttk.Button(frame, text="Decrypt", command=decrypt_button_click, style="CustomButton.TButton")
decrypt_button.grid(column=0, row=5, columnspan=2, padx=5, pady=10)

# Style the widgets
window.style = ttk.Style()
window.style.configure("CustomFrame.TFrame", background="#E1F3D8")
window.style.configure("TitleLabel.TLabel", background="#E1F3D8", font=("Arial", 20, "bold" , "italic"))
window.style.configure("CustomLabel.TLabel", background="#E1F3D8", font=("Arial", 15))
window.style.configure("CustomButton.TButton", background="#A4C2A8", font=("Arial", 15))

# Run the main window event loop
window.mainloop()
