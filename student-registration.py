import tkinter as tk
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    course TEXT,
    phone TEXT
)
""")
conn.commit()

def register():
    name = entry_name.get()
    email = entry_email.get()
    course = entry_course.get()
    phone = entry_phone.get()

    if name == "" or email == "" or course == "" or phone == "":
        messagebox.showwarning("Error", "All fields are required!")
        return

    cursor.execute(
        "INSERT INTO students (name, email, course, phone) VALUES (?, ?, ?, ?)",
        (name, email, course, phone)
    )
    conn.commit()
    messagebox.showinfo("Success", "Student Registered Successfully!")
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_phone.delete(0, tk.END)

root = tk.Tk()
root.title("Student Registration")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Student Registration Form", font=("Arial", 16)).pack(pady=10)
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root, width=30)
entry_email.pack()

tk.Label(root, text="Course").pack()
entry_course = tk.Entry(root, width=30)
entry_course.pack()
tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root, width=30)
entry_phone.pack()

tk.Button(root, text="Register", command=register, bg="green", fg="white").pack(pady=20)

root.mainloop()
conn.close()