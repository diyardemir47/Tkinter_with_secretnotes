import tkinter as tk
from tkinter import messagebox
import hashlib

def encrypt_text():
    text = text_entry.get()  # Metin girişi içindeki değeri al
    encrypted_text = hashlib.sha256(text.encode()).hexdigest()  # Metni SHA-256 ile şifrele

    filename = filename_entry.get() + ".txt"  # Dosya adını al ve uzantı ekle

    with open(filename, "w") as file:
        file.write(encrypted_text)
    messagebox.showinfo("Success", f"Text encrypted and saved to {filename}")

def decrypt_text():
    try:
        filename = filename_entry.get() + ".txt"
        with open(filename, "r") as file:
            encrypted_text = file.read()

            decrypted_text = ""
            for char in encrypted_text:
                decrypted_char = chr(ord(char) - 1)  # Her karakterin ASCII değerini bir azaltarak çöz
                decrypted_text += decrypted_char

            decrypted_filename = filename.split(".")[0] + "_decrypted.txt"
            with open(decrypted_filename, "w") as decrypted_file:
                decrypted_file.write(decrypted_text)
            messagebox.showinfo("Success", f"Text decrypted and saved to {decrypted_filename}")
    except FileNotFoundError:
        messagebox.showerror("Error", "No encrypted text found. Encrypt a text first.")

# Pencere oluşturma
window = tk.Tk()
window.title("File Encryption App")
window.geometry("300x500")

# Dosya adı metin girişi
filename_label = tk.Label(window, text="Enter a filename:")
filename_label.pack()

filename_entry = tk.Entry(window)
filename_entry.pack()

# Metin girişi
text_label = tk.Label(window, text="Enter text:")
text_label.pack()

text_entry = tk.Entry(window)
text_entry.pack()

# Şifreleme düğmesi
encrypt_button = tk.Button(window, text="Encrypt and Save", command=encrypt_text)
encrypt_button.pack()

# Şifre çözme düğmesi
decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_text)
decrypt_button.pack()

# Pencereyi başlatma
window.mainloop()
