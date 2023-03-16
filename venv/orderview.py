import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import sqlite3



def order_table_view():
    root = tk.Tk()
    root.title('Customer Orders')
    root.geometry('660x230')


    # define columns
    columns = ('OrderID', 'CustID', 'Length', 'Width', 'Depth', 'Concrete', 'Day', 'Month', 'Year','Time','AM/PM','Price')

    orders = ttk.Treeview(root, columns=columns, show='headings')
    style = ttk.Style(root)
    # set ttk theme to "clam" which support the fieldbackground option
    style.theme_use("clam")
    style.configure("Treeview", background="#728c8d",
                    fieldbackground="#728c8d" ,foreground="black")
    orders.column("OrderID", width=80)
    orders.column("CustID", width=50)
    orders.column('Length', width=50)
    orders.column('Width', width=50)
    orders.column('Depth', width=50)
    orders.column('Concrete', width=60)
    orders.column('Day', width=50)
    orders.column('Month', width=50)
    orders.column('Year', width=50)
    orders.column('Time', width=50)
    orders.column('AM/PM', width=55)
    orders.column('Price', width=50)
    # define headings
    orders.heading('OrderID', text='OrderID')
    orders.heading('CustID', text='CustID')
    orders.heading('Length', text='Length')
    orders.heading('Width', text='Width')
    orders.heading('Depth', text='Depth')
    orders.heading('Concrete', text='Concrete')
    orders.heading('Day', text='Day')
    orders.heading('Month', text='Month')
    orders.heading('Year', text='Year')
    orders.heading('Time', text='Time')
    orders.heading('AM/PM', text='AM/PM')
    orders.heading('Price', text='Price')







    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM order_details")
    records = cursor.fetchall()

    for record in records:
        orders.insert('', tk.END, values=record)


    orders.bind('<<TreeviewSelect>>')

    orders.grid(row=0, column=0, sticky='nsew')

    # add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=orders.yview)
    orders.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')


    root.mainloop()



if __name__ == '__main__':
    pass