import sqlite3
def table():


    conn = sqlite3.connect('Mincrete.db')
    print("Opened database successfully")

    Conn.execute('''CREATE TABLE IF NOT EXISTS Orders 
               (Order_ID         INT     PRIMARY KEY     NOT NULL,
                Product_ID      TEXT    NOT NULL,
                Quantity    INT        NOT NULL);''')

    print("Orders table is created succesfully")

    conn.execute('''CREATE TABLE IF NOT EXISTS Customer
             (Customer_ID   INT  PRIMARY KEY     NOT NULL,
               NAME           TEXT    NOT NULL,
               ADDRESS        CHAR(50),
               Order_ID INT  NOT NULL, 
               FOREIGN KEY (Order_ID) REFERENCES Orders (Order_ID));''')

    print("Customer table is created succesfully")