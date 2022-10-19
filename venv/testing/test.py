#login only
import sqlite3
from tkinter import *
from tkinter import messagebox

def Create_Tables():
    # creating table Staff
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")

    # using create if exists to prevent the code to crash if the database already exists.

    conn.execute('''CREATE TABLE IF NOT EXISTS Login_details 
               (Username        TEXT     PRIMARY KEY     NOT NULL,
                Password      TEXT    NOT NULL);''')

    print("Login Details table is created succesfully")

    conn.close()

def adminValidator(username,password,validation):
        conn = sqlite3.connect('Mincrete.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Login_details where Username=? and Password=?",
                       ("Richard", validation))
        row = cursor.fetchall()
        result = len(row)
        if result == 1:
            insertdata(username,password)
        else:
            messagebox.showinfo("info", "Signup failed")
        pass

def insertdata(username1,password1):
    # inserting data into parent table DEPRATEMENTS
    # Enter values using input statements

    conn = sqlite3.connect('Mincrete.db')
    # insert data into database table
    # conn.execute('''insert into Login_details  (Username, Password) values (?, ?)''', )
    conn.execute('''insert into Login_details  (Username, Password) values (?, ?)''',(username1,password1))

    conn.commit()  # do not forget to commit the data (i.e. save the data on the table
    messagebox.showinfo("info", "signup was successful")
    conn.close()


def adminpass():

    conn = sqlite3.connect('test.db')
    conn.execute('''insert into Login_details  (Username, Password) values (?, ?)''',("Richevs","Concrete"))

    conn.commit()  # do not forget to commit the data (i.e. save the data on the table
    messagebox.showinfo("info", "signup was successful")
    conn.close()





def username_validation(username, password):
    from Mainpage import homepage
    conn = sqlite3.connect('Mincrete.db')
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM Login_details where Username=? and Password=?",
                   (username, password))
    row=cursor.fetchall()
    result = len(row)
    if result == 1:
        messagebox.showinfo("info", "login success")
        homepage()
    else:
        messagebox.showinfo("info", "login failed")
    pass

#delete_name = input("enter name")
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('''DELETE FROM Login_details where Username=? and password=?''',
               ("Richevs","Concrete"))
conn.close()




#Create_Tables()
#adminpass()
# insertdata("hi","bye")

if __name__ == "__main__":
    pass