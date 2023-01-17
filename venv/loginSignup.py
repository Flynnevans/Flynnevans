#login only
import sqlite3
from tkinter import *
from tkinter import messagebox
from time import strftime
import Mainpage


def windowswap(close, open):
    close
    open



def delete_Table():
    conn = sqlite3.connect('Mincrete.db')
    conn.execute('DROP TABLE order_details')
    conn.commit()
    conn.close()

    conn = sqlite3.connect('Mincrete.db')
    conn.execute('DROP TABLE cust_details')
    conn.commit()
    conn.close()


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
                phonenumber     TEXT    NOT NULL,
                email       TEXT        NOT NULL,
                postcode      TEXT       NOT NULL);''')
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
                time       VARCHAR        NOT NULL,
                AMPM       TEXT        NOT NULL,
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



def search_orders(Order_num):
    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM order_details where orderid = ?", (Order_num, ))
    found = cursor.fetchall()
    cursor.close()
    conn.close()
    return found

def dump():
    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cust_details")
    found = cursor.fetchall()
    cursor.close()
    conn.close()
    return found






def customer_insert(order, customer):

    if len(customer) > 4:
        print("0")
        CustomerID = customer[0][0] + strftime('%M%S') + customer[1][0]

        conn = sqlite3.connect('Mincrete.db')
        cursor = conn.cursor()
        cursor.execute('''insert into cust_Details(custID, fname, sname, address, phonenumber, email, postcode) 
        values(?,?,?,?,?,?,?)''',(CustomerID,customer[0],customer[1],customer[2],customer[4],customer[5],customer[3]))

        conn.commit()
        conn.close()

        orderDet_insert(order, CustomerID)
    else:
        conn = sqlite3.connect('Mincrete.db')
        cursor = conn.cursor()
        cursor = conn.execute("SELECT * FROM cust_Details WHERE custID = ? and postcode = ? and sname = ?",(customer[0],
                              customer[1],customer[2]))
        results = cursor.fetchone()



        try:
            if customer[0] == results[0]:
                if customer[2] == results[2]:
                    if customer[1] == results[6]:
                        CustomerID = customer[0]
                        orderDet_insert(order, CustomerID)
        except:
            messagebox.showinfo("info", "No details were found")
            Mainpage.homepage()


        conn.commit()
        conn.close()






def orderDet_insert(order, CustomerID):
    date = strftime('%x')
    string = strftime('%H%M%S')
    OrderID = string + date[0:2] + date[3:5] + date[6:8]




    text = ("Take note: your orderID is", OrderID,"your customerID is", CustomerID)
    messagebox.showinfo("Take Note Of these", text)


    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()
    cursor.execute('''insert into order_details (orderID, custID, length, width, depth,
     concrete, day, month, year, time, AMPM) 
    values (?,?,?,?,?,?,?,?,?,?,?)''',(OrderID, CustomerID, order[0],order[1],order[2],order[3],order[4],
                                   order[5],order[6], order[7], order[8]))
    conn.commit()
    conn.close()
    Mainpage.homepage()






if __name__ == '__main__':
    # delete_Table()
    # order_table()
    # customer_table()
    #print(dump())
    pass
