import tkinter as tk
from tkinter import messagebox
import random
import string
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        self.length_var = tk.IntVar(value=12)
        self.use_upper = tk.BooleanVar(value=True)
        self.use_lower = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)
        self.generated_password = tk.StringVar()
        title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        settings_frame = tk.Frame(root)
        settings_frame.pack(pady=5, padx=20, fill="x")

        tk.Label(settings_frame, text="Length:").pack(side="left")
        length_entry = tk.Entry(settings_frame, textvariable=self.length_var, width=5)
        length_entry.pack(side="left", padx=5)

        options_frame = tk.Frame(root)
        options_frame.pack(pady=5, padx=20, fill="x")
        tk.Checkbutton(options_frame, text="Uppercase (A-Z)", variable=self.use_upper).pack(anchor="w")
        tk.Checkbutton(options_frame, text="Lowercase (a-z)", variable=self.use_lower).pack(anchor="w")
        tk.Checkbutton(options_frame, text="Digits (0-9)", variable=self.use_digits).pack(anchor="w")
        tk.Checkbutton(options_frame, text="Symbols (!@#$)", variable=self.use_symbols).pack(anchor="w")

        generate_btn = tk.Button(root, text="Generate Password", command=self.generate_password, bg="#007acc", fg="white", font=("Helvetica", 10, "bold"))
        generate_btn.pack(pady=15, fill="x", padx=40)
        result_entry = tk.Entry(root, textvariable=self.generated_password, font=("Consolas", 12), justify="center", state="readonly")
        result_entry.pack(pady=5, fill="x", padx=40)

        copy_btn = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_btn.pack(pady=5)
    def generate_password(self):
        length = self.length_var.get()
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return
        character_pool = ""
        if self.use_upper.get():
            character_pool += string.ascii_uppercase
        if self.use_lower.get():
            character_pool += string.ascii_lowercase
        if self.use_digits.get():
            character_pool += string.digits
        if self.use_symbols.get():
            character_pool += string.punctuation
        if not character_pool:
            messagebox.showwarning("Warning", "Please select at least one character type")
            return
        password = "".join(random.choice(character_pool) for _ in range(length))
        self.generated_password.set(password)
    def copy_to_clipboard(self):
        password = self.generated_password.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.root.update()
            messagebox.showinfo("Success", "Password copied to clipboard")
        else:
            messagebox.showwarning("Warning", "No password to copy")
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
