import subprocess
import tkinter as tk
from tkinter import messagebox

def run_pipeline():
    # Select text editor
    text_editor = text_editor_type_var.get()

    # Command to open bashrc based on text editor
    command = f"{text_editor} ~/.bashrc"

    try:
        subprocess.run(["wsl", "bash", "-c", command], check=True) 

    except subprocess.CalledProcessError as e:
        app.after(0, lambda: messagebox.showerror("Error", str(e)))

# Set up tkinter app
app = tk.Tk()
app.title("basrc modifier")

# Fasta text_editor_type selection
tk.Label(app, text="Command line text editor to open bashrc:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
text_editor_type_var = tk.StringVar(value="micro")
text_editor_type_options = ["micro", "vim","nvim"]
text_editor_type_dropdown = tk.OptionMenu(app, text_editor_type_var, *text_editor_type_options)
text_editor_type_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Start button
tk.Button(app, text="Run program", command=run_pipeline).grid(row=1, column=1, padx=10, pady=20)

app.mainloop()
