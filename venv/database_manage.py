#login only
import sqlite3
from tkinter import *
from tkinter import messagebox
from time import strftime
# from Mainpage import homepage



def windowswap(close, open):
    close
    open



def delete_Table():
    conn = sqlite3.connect('Mincrete.db')
    conn.execute('DROP TABLE order_details')
    conn.commit()
    conn.close()

    # conn = sqlite3.connect('Mincrete.db')
    # conn.execute('DROP TABLE cust_details')
    # conn.commit()
    # conn.close()




# Define a function to create tables in the database
def Create_Tables():

    # Connect to the database
    conn = sqlite3.connect('Mincrete.db')
    # Print a message to confirm that the database is opened successfully
    print("Opened database successfully")
    # Create a table named 'Login_details' if it doesn't already exist
    conn.execute('''CREATE TABLE IF NOT EXISTS Login_details 
               (Username        TEXT     PRIMARY KEY     NOT NULL,
                Password      TEXT    NOT NULL);''')
    # Close the database connection
    conn.close()






def EditRecord(old,new):




    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM order_details WHERE custID =? and day =? and month =? and year =? and AMPM =? and time =?", (old[0],old[1],old[2],old[3],old[5],old[4]))
    results = cursor.fetchone()
    try:
        if old[0] == results[1] and old[1]== results[6] and  old[2] == results[7] and old[3] == results[8] and old[5] == results[10] and old[4] == results [9]:

            conn.execute('''UPDATE order_details  SET length = ? WHERE orderID = ? ''', (new[0],results[0]))
            conn.execute('''UPDATE order_details  SET width = ? WHERE orderID = ? ''', (new[1],results[0]))
            conn.execute('''UPDATE order_details  SET depth = ? WHERE orderID = ? ''',(new[2], results[0]))
            conn.execute('''UPDATE order_details  SET concrete = ? WHERE orderID = ? ''',(new[3], results[0]))
            conn.execute('''UPDATE order_details  SET day = ? WHERE orderID = ? ''',(new[4], results[0]))
            conn.execute('''UPDATE order_details  SET month = ? WHERE orderID = ? ''',(new[5], results[0]))
            conn.execute('''UPDATE order_details  SET year = ? WHERE orderID = ? ''',(new[6], results[0]))
            conn.execute('''UPDATE order_details  SET time = ? WHERE orderID = ? ''',(new[7], results[0]))
            conn.execute('''UPDATE order_details  SET AMPM = ? WHERE orderID = ? ''',(new[8], results[0]))
            conn.execute('''UPDATE order_details  SET price = ? WHERE orderID = ? ''', (new[9], results[0]))

            conn.commit()
            conn.close()

        else:
            messagebox.showinfo("info", "No details were found")
    except:
        messagebox.showinfo("Error", "No details were found")
    else:
        messagebox.showinfo("info", "Order has been Edited")



def DeleteRecord(customerid, days, months, years):




    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM order_details WHERE custID =? and day =? and month =? and year =?", (customerid,
                                                                                                              days, months,
                                                                                                              years))
    results = cursor.fetchone()
    try:
        if customerid == results[1]:
            if days == results[6]:
                if months == results[7]:
                    if years == results[8]:
                        conn.execute("DELETE FROM order_details WHERE  custID =? and day =? and month =? and year =?",
                                     (customerid, days,
                                      months, years))

                        conn.commit()
                        conn.close()
                    else:
                        messagebox.showinfo("info", "No details were found")

                else:
                    messagebox.showinfo("info", "No details were found")

            else:
                messagebox.showinfo("info", "No details were found")
        else:
            messagebox.showinfo("info", "No details were found")
    except:
        messagebox.showinfo("info", "No details were found")
    else:
        messagebox.showinfo("info", "Order has been removed")


def customer_table():
    # Connect to the database
    conn = sqlite3.connect('Mincrete.db')

    # Create a table named 'cust_details' if it doesn't already exist
    conn.execute('''CREATE TABLE IF NOT EXISTS cust_details 
               (custID        TEXT     PRIMARY KEY     NOT NULL,
                fname      TEXT    NOT NULL,
                sname         TEXT      NOT NULL,
                address       TEXT      NOT NULL,
                phonenumber     TEXT    NOT NULL,
                email       TEXT        NOT NULL,
                postcode      TEXT       NOT NULL);''')

    # Close the database connection
    conn.close()


# Define a function to create a table in the database for storing order details
def order_table():
    # Connect to the database
    conn = sqlite3.connect('Mincrete.db')

    # Create a table named 'order_details' if it doesn't already exist
    # The 'custID' column references the primary key in the 'cust_details' table
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
                Price      FLOAT       NOT NULL,
                FOREIGN KEY (custID) REFERENCES cust_Details (custID));''')

    # Close the database connection
    conn.close()




def delete_account(x,y):
    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Login_details where Username =? and Password=?",(x,y ))
    conn.commit()
    conn.close()



# def search_orders(Order_num):
#     conn = sqlite3.connect('Mincrete.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM order_details where orderid = ?", (Order_num, ))
#     found = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return found

# def dump():
#     conn = sqlite3.connect('Mincrete.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM cust_details")
#     found = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return found






def customer_insert(order, customer):

    if len(customer) > 4:
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



        if customer[0] == results[0]:
            if customer[2] == results[2]:
                if customer[1] == results[6]:
                    CustomerID = customer[0]
                    orderDet_insert(order, CustomerID)
                else:
                    messagebox.showinfo("info", "No details were found")

            else:
                messagebox.showinfo("info", "No details were found")

        else:
            messagebox.showinfo("info", "No details were found")





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
     concrete, day, month, year, time, AMPM, Price) 
    values (?,?,?,?,?,?,?,?,?,?,?,?)''',(OrderID, CustomerID, order[0],order[1],order[2],order[3],order[4],
                                   order[5],order[6], order[7], order[8], order[9]))
    conn.commit()
    conn.close()







if __name__ == '__main__':
    order_table()
    pass
