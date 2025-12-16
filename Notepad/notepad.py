import tkinter as tk
from tkinter import filedialog, messagebox
class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Notepad")
        self.root.geometry("800x600")
        self.filename = None
        self.is_dark_mode = False
        self.text_area = tk.Text(self.root, font=("Consolas", 12), wrap='word', undo=True)
        self.text_area.pack(expand=True, fill='both')
        scrollbar = tk.Scrollbar(self.text_area)
        self.text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As...", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Find & Replace", command=self.open_find_replace_dialog)

        self.view_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Dark Mode", command=self.toggle_dark_mode)
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.filename = None
        self.root.title("Notepad - New File")
    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            self.filename = file_path
            self.root.title(f"Notepad - {self.filename}")
            try:
                with open(file_path, "r") as f:
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(1.0, f.read())
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")
    def save_file(self):
        if self.filename:
            try:
                with open(self.filename, "w") as f:
                    f.write(self.text_area.get(1.0, tk.END))
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")
        else:
            self.save_as_file()
    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            self.filename = file_path
            self.root.title(f"Notepad - {self.filename}")
            with open(file_path, "w") as f:
                f.write(self.text_area.get(1.0, tk.END))
    def open_find_replace_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Find & Replace")
        dialog.geometry("350x150")
        dialog.resizable(False, False)

        tk.Label(dialog, text="Find:").grid(row=0, column=0, padx=10, pady=10)
        find_entry = tk.Entry(dialog, width=30)
        find_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(dialog, text="Replace:").grid(row=1, column=0, padx=10, pady=10)
        replace_entry = tk.Entry(dialog, width=30)
        replace_entry.grid(row=1, column=1, padx=10, pady=10)

        def perform_replace():
            target = find_entry.get()
            replacement = replace_entry.get()
            
            if target:
                content = self.text_area.get(1.0, tk.END)
                count = content.count(target)
                new_content = content.replace(target, replacement)
                
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, new_content.rstrip())
                
                messagebox.showinfo("Result", f"Replaced {count} occurrences.")
                dialog.destroy()

        tk.Button(dialog, text="Replace All", command=perform_replace).grid(row=2, column=0, columnspan=2, pady=10)

    def toggle_dark_mode(self):
        if not self.is_dark_mode:
            bg_color = "#2b2b2b"
            fg_color = "#e6e6e6"
            cursor_color = "white"
            self.text_area.config(bg=bg_color, fg=fg_color, insertbackground=cursor_color)
            self.is_dark_mode = True
        else:
            bg_color = "white"
            fg_color = "black"
            cursor_color = "black"
            self.text_area.config(bg=bg_color, fg=fg_color, insertbackground=cursor_color)
            self.is_dark_mode = False

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
