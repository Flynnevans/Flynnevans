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

    tree = ttk.Treeview(root, columns=columns, show='headings')
    style = ttk.Style(root)
    # set ttk theme to "clam" which support the fieldbackground option
    style.theme_use("clam")
    style.configure("Treeview", background="#728c8d",
                    fieldbackground="#728c8d", foreground="grey")
    tree.column("OrderID", width=80)
    tree.column("CustID", width=50)
    tree.column('Length', width=50)
    tree.column('Width', width=50)
    tree.column('Depth', width=50)
    tree.column('Concrete', width=60)
    tree.column('Day', width=50)
    tree.column('Month', width=50)
    tree.column('Year', width=50)
    tree.column('Time', width=50)
    tree.column('AM/PM', width=55)
    tree.column('Price', width=50)
    # define headings
    tree.heading('OrderID', text='OrderID')
    tree.heading('CustID', text='CustID')
    tree.heading('Length', text='Length')
    tree.heading('Width', text='Width')
    tree.heading('Depth', text='Depth')
    tree.heading('Concrete', text='Concrete')
    tree.heading('Day', text='Day')
    tree.heading('Month', text='Month')
    tree.heading('Year', text='Year')
    tree.heading('Time', text='Time')
    tree.heading('AM/PM', text='AM/PM')
    tree.heading('Price', text='Price')







    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM order_details")
    records = cursor.fetchall()

    for record in records:
        tree.insert('', tk.END, values=record)


    tree.bind('<<TreeviewSelect>>')

    tree.grid(row=0, column=0, sticky='nsew')

    # add a scrollbar
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')


    root.mainloop()

order_table_view()