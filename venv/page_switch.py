from Mainpage import homepage
import sqlite3
from tkinter import messagebox

def adminValidator(username, password, validation):
    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Login_details where Username=? and Password=?",
                   ("Richevs", validation))
    row = cursor.fetchall()
    result = len(row)
    if result == 1:
        insertdata(username, password)
    else:
        messagebox.showinfo("info", "Signup failed")
    pass


def insertdata(username1, password1):
    conn = sqlite3.connect('Mincrete.db')

    conn.execute('''insert into Login_details  (Username, Password) values (?, ?)''', (username1, password1))

    conn.commit()
    messagebox.showinfo("info", "signup was successful")
    conn.close()


def username_validation(username, password):
    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Login_details where Username=? and Password=?",
                   (username, password))
    row = cursor.fetchall()
    result = len(row)
    if result == 1:
        messagebox.showinfo("info", "login success")
        homepage()

    else:
        messagebox.showinfo("info", "login failed")
    pass


