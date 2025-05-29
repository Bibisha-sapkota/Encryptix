import random
import sqlite3
from tkinter import *
from tkinter import messagebox

# Create database and table
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (Username TEXT, GeneratedPassword TEXT)")
conn.commit()
conn.close()

# GUI Application
class PasswordApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Password Generator")
        master.geometry("400x300")
        master.resizable(False, False)

        self.username = StringVar()
        self.length = IntVar()
        self.generated_password = StringVar()

        Label(master, text="Username:", font=("Arial", 12)).pack(pady=5)
        self.entry_username = Entry(master, textvariable=self.username, font=("Arial", 12))
        self.entry_username.pack()

        Label(master, text="Password Length (min 6):", font=("Arial", 12)).pack(pady=5)
        self.entry_length = Entry(master, textvariable=self.length, font=("Arial", 12))
        self.entry_length.pack()

        Button(master, text="Generate Password", command=self.generate_password, font=("Arial", 12), bg="lightblue").pack(pady=10)
        
        Label(master, text="Generated Password:", font=("Arial", 12)).pack()
        self.entry_password = Entry(master, textvariable=self.generated_password, font=("Arial", 12), fg="green")
        self.entry_password.pack()

        Button(master, text="Save to Database", command=self.save_to_db, font=("Arial", 12), bg="lightgreen").pack(pady=10)

    def generate_password(self):
        username = self.username.get()
        length = self.length.get()

        if not username.isalpha():
            messagebox.showerror("Error", "Username must contain only letters.")
            return

        if length < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters.")
            return

        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#%&!"
        password = ''.join(random.sample(chars, length))
        self.generated_password.set(password)

    def save_to_db(self):
        username = self.username.get()
        password = self.generated_password.get()

        if not username or not password:
            messagebox.showerror("Error", "Please generate a password first.")
            return

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE Username=?", (username,))
        if cursor.fetchone():
            messagebox.showerror("Error", "Username already exists.")
        else:
            cursor.execute("INSERT INTO users (Username, GeneratedPassword) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Saved", "Password saved successfully.")
        conn.close()

if __name__ == "__main__":
    root = Tk()
    app = PasswordApp(root)
    root.mainloop()
