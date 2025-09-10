import tkinter as tk
from tkinter import messagebox

                                                                    # --- Caesar Cipher Functions ---
def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def decrypt(text, shift):
    return encrypt(text, -shift)

                                                                    # --- GUI Function ---
def process_text():
    text = entry_text.get("1.0", tk.END).strip()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Error", "Shift value must be an integer.")
        return

    if choice.get() == "encrypt":
        result = encrypt(text, shift)
    else:
        result = decrypt(text, shift)
    
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# --- Main Window ---
window = tk.Tk()
window.title("Text Encryption & Decryption (Caesar Cipher)")
window.geometry("700x600")
window.resizable(False, False)
window['bg' ] = "#000000"




# --- Widgets ---
tk.Label(window, text="Enter Text:", fg="green" , bg="black",  ).pack()
entry_text = tk.Text(window, height=5, width=60, bg="white")
entry_text.pack()

tk.Label(window, text="Enter Shift Value:" ,fg="green", bg="black").pack()
entry_shift = tk.Entry(window , bg="green")
entry_shift.pack()

choice = tk.StringVar(value="encrypt")
tk.Radiobutton(window, text="Encrypt", variable=choice, value="encrypt",fg="green",bg="black").pack()
tk.Radi
