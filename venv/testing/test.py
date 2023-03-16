import sqlite3
import tkinter as tk
from tkinter import messagebox

# create a database connection
conn = sqlite3.connect('user_data.db')

# create a table to store user data
conn.execute('''CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                surname TEXT NOT NULL
                );''')

# create a Tkinter window
root = tk.Tk()
root.title('Add User')

# create entry widgets for name and surname
name_label = tk.Label(root, text='Name:')
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

surname_label = tk.Label(root, text='Surname:')
surname_label.grid(row=1, column=0)
surname_entry = tk.Entry(root)
surname_entry.grid(row=1, column=1)

# function to insert user data into the database
def add_user():
    name = name_entry.get()
    surname = surname_entry.get()
    conn.execute(f"INSERT INTO user (name, surname) VALUES ('{name}', '{surname}')")
    conn.commit()
    tk.messagebox.showinfo('Success', 'User added to database')
    name_entry.delete(0, tk.END)
    surname_entry.delete(0, tk.END)

# create a button to add user data to the database
add_button = tk.Button(root, text='Add User', command=add_user)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

# start the Tkinter event loop
root.mainloop()

# close the database connection when the GUI is closed
conn.close()
