import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def encrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    encrypted_text = caesar_cipher(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", encrypted_text)

def decrypt_text():
    text = input_text.get("1.0", tk.END).strip()
    shift = -int(shift_entry.get())  # Decrypting is just shifting back
    decrypted_text = caesar_cipher(text, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", decrypted_text)

# Create main window
root = tk.Tk()
root.title("Caesar Cipher Encryption/Decryption")

# Create input frame
input_frame = ttk.Frame(root, padding="20")
input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

input_label = ttk.Label(input_frame, text="Enter text:")
input_label.grid(row=0, column=0, sticky=tk.W)

input_text = tk.Text(input_frame, width=40, height=5)
input_text.grid(row=1, column=0, columnspan=2, pady=(0, 10))

shift_label = ttk.Label(input_frame, text="Shift value:")
shift_label.grid(row=2, column=0, sticky=tk.W)

shift_entry = ttk.Entry(input_frame)
shift_entry.grid(row=2, column=1, sticky=tk.W, padx=(5, 0))

# Create buttons
encrypt_button = ttk.Button(input_frame, text="Encrypt", command=encrypt_text)
encrypt_button.grid(row=3, column=0, pady=(10, 0), sticky=tk.W)

decrypt_button = ttk.Button(input_frame, text="Decrypt", command=decrypt_text)
decrypt_button.grid(row=3, column=1, pady=(10, 0), sticky=tk.W)

# Create output frame
output_frame = ttk.Frame(root, padding="20")
output_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

output_label = ttk.Label(output_frame, text="Output:")
output_label.grid(row=0, column=0, sticky=tk.W)

output_text = tk.Text(output_frame, width=40, height=5)
output_text.grid(row=1, column=0, columnspan=2)

root.mainloop()
