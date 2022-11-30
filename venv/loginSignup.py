#login only
import sqlite3
from tkinter import *
from tkinter import messagebox
from time import strftime








def Create_Tables():
    conn = sqlite3.connect('Mincrete.db')
    print("Opened database successfully")

    conn.execute('''CREATE TABLE IF NOT EXISTS Login_details 
               (Username        TEXT     PRIMARY KEY     NOT NULL,
                Password      TEXT    NOT NULL);''')
    print("Login Details table is created succesfully")

    conn.close()









def customer_table():
    conn = sqlite3.connect('Mincrete.db')
    print("Opened database successfully")

    conn.execute('''CREATE TABLE IF NOT EXISTS cust_details 
               (custID        TEXT     PRIMARY KEY     NOT NULL,
                fname      TEXT    NOT NULL,
                sname         TEXT      NOT NULL,
                address       TEXT      NOT NULL,
                phonenumber     INT    NOT NULL,
                email       TEXT        NOT NULL);''')
    print("Customer Details table is created succesfully")

    conn.close()


def order_table():
    conn = sqlite3.connect('Mincrete.db')
    print("Opened database successfully")

    conn.execute('''CREATE TABLE IF NOT EXISTS order_details 
               (orderID        TEXT     PRIMARY KEY     NOT NULL,
               custID           TEXT    NOT NULL,
                length      INT    NOT NULL,
                width         INT      NOT NULL,
                depth       INT      NOT NULL,
                concrete     TEXT    NOT NULL,
                day       INT        NOT NULL,
                month       INT        NOT NULL,
                year        INT        NOT NULL,
                accepted     TEXT    NOT NULL,
                FOREIGN KEY (custID) REFERENCES cust_Details (custID));''')
    print("Customer Details table is created succesfully")


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


    conn = sqlite3.connect('Mincrete.db')

    conn.execute('''insert into Login_details  (Username, Password) values (?, ?)''',(username1,password1))

    conn.commit()
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



def delete_account(x,y):
    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Login_details where Username =? and Password=?",(x,y ))
    conn.commit()
    conn.close()

def custDet_insert():
    pass


def orderDet_insert(order, customer):
    date = strftime('%x')
    string = strftime('%H%M%S')
    OrderID = string + date[0:2] + date[3:5] + date[6:8]

    CustomerID = customer[0][0]+strftime('%H%M%S')+customer[1][0]


    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()
    conn.execute('''insert into order_details (orderID, custID, length, width, depth, concrete, day, month, year, accepted) 
    values (?,?,?,?,?,?,?,?,?,?)''',(OrderID, CustomerID, order[0],order[1],order[2],order[3],order[5],order[6],order[7],order[4]))

