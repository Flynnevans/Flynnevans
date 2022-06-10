#login only
import sqlite3
from tkinter import *
from tkinter import messagebox

def Create_Tables():
    # creating table Staff
    conn = sqlite3.connect('Mincrete.db')
    print("Opened database successfully")

    # using create if exists to prevent the code to crash if the database already exists.

    conn.execute('''CREATE TABLE IF NOT EXISTS Login_details 
               (Username        TEXT     PRIMARY KEY     NOT NULL,
                Password      TEXT    NOT NULL);''')

    print("Login Details table is created succesfully")

    conn.close()

def InsertData():
    # inserting data into parent table DEPRATEMENTS
    # Enter values using input statements

    conn = sqlite3.connect('Mincrete.db')
    # insert data into database table
    # conn.execute('''insert into Login_details  (Username, Password) values (?, ?)''', )
    conn.execute('''insert into Login_details  (Username, Password) values (?, ?)''',("Flynn","Pass"))


    conn.commit()  # do not forget to commit the data (i.e. save the data on the table
    conn.close()



def displayContents():
    # here we will use select query
    conn = sqlite3.connect('Mincrete.db')
    # Select all records in a table:
    cursor = conn.execute(''' SELECT Username, Password FROM  Login_details ''')

    # Display what you have selected

    for row in cursor:
        print("Username = ", row[0])
        print("Password = ", row[1], "\n")









def username_validation(username, password):
    conn = sqlite3.connect('Mincrete.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Login_details where Username=? and Password=?",
                   (username, password))
    row=cursor.fetchall()
    result = len(row)
    if result == 1:
        messagebox.showinfo("info", "login success")
    else:
        messagebox.showinfo("info", "login failed")
    pass








Create_Tables()

if __name__ == "__main__":
    pass