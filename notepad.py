from tkinter.filedialog import *
import tkinter as tk

canvas = tk.Tk()
canvas.geometry("700x600")
canvas.title("Untitled - Soumya's Notepad")
canvas.config(bg = "white")

# Backend-functions ->
# For File menu :
def new_file():
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.INSERT, "")
    canvas.title("Untitled - Soumya's Notepad")
    file_name = None
    return file_name

def open_file():
    file_name = askopenfilename(defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file_name:
        text_area.delete(1.0, tk.END)
        with open(file_name, "r") as file:
            text_area.insert(tk.INSERT, file.read())
        canvas.title(f"{file_name} - Soumya's Notepad")
    return file_name

def save_file():
    file_name = asksaveasfilename(initialfile = "Untitled.txt", defaultextension = ".txt", filetypes = [("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file_name:
        with open(file_name, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        canvas.title(f"{file_name} - Soumya's Notepad")
    return file_name

def exit_now():
    canvas.destroy()

# For Edit menu :
def cut():
    text_area.clipboard_clear()
    text_area.clipboard_append(text_area.selection_get())
    text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)

def copy():
    text_area.clipboard_clear()
    text_area.clipboard_append(text_area.selection_get())

def paste():
    text_area.insert(tk.INSERT, text_area.clipboard_get())

def undo():
    text_area.edit_undo()

def redo():
    text_area.edit_redo()

# For Help menu :
def about_app():
    tk.messagebox.showinfo("About Notepad", "This is a simple notepad application built with tkinter. This application is developed by Soumyadev Saha, a student of B.Tech CSE, Jadavpur University.")

menu_bar = tk.Menu(canvas)

# Adding buttons->
# File menu :
file_menu = tk.Menu(menu_bar, tearoff = 0)
file_menu.add_command(label = "New", command = new_file)
file_menu.add_command(label = "Open", command = open_file)
file_menu.add_command(label = "Save As", command = save_file)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = exit_now)
menu_bar.add_cascade(label = "File", menu = file_menu)

# Edit Menu :
edit_menu = tk.Menu(menu_bar, tearoff = 0)
edit_menu.add_command(label = "Cut", command = cut)
edit_menu.add_command(label = "Copy", command = copy)
edit_menu.add_command(label = "Paste", command = paste)
edit_menu.add_separator()
edit_menu.add_command(label = "Undo", command = undo)
edit_menu.add_command(label = "Redo", command = redo)
menu_bar.add_cascade(label = "Edit", menu = edit_menu)

# Help Menu:
help_menu = tk.Menu(menu_bar, tearoff = 0)
help_menu.add_command(label = "About App", command = about_app)
menu_bar.add_cascade(label = "Help", menu = help_menu)

# Packing the menu bar->
canvas.config(menu = menu_bar)

# Adding text area->
text_area = tk.Text(canvas, width = 50, height = 20, bg = "alice blue", font = ("Poppins", 10)) 
text_area.pack(expand = True, fill = "both", padx = 10, pady = 10)

canvas.mainloop()