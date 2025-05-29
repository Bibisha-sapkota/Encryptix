import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Select Error", "No task selected.")
window = tk.Tk()
window.title("To-Do List")

entry = tk.Entry(window, width=40)
entry.pack(pady=10)

add_button = tk.Button(window, text="Add Task", width=20, command=add_task)
add_button.pack()

listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10)

delete_button = tk.Button(window, text="Delete Task", width=20, command=delete_task)
delete_button.pack()

window.mainloop()
