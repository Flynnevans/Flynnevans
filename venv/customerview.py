import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import sqlite3



def customer_table_view():
    root = tk.Tk()
    root.title('Customer Details')
    root.geometry('610x230')


    # define columns
    columns = ('CustID', 'Fname', 'Sname', 'Address', 'PhoneNo', 'Email', 'Postcode')

    orders = ttk.Treeview(root, columns=columns, show='headings')
    style = ttk.Style(root)
    # set ttk theme to "clam" which support the fieldbackground option
    style.theme_use("clam")
    style.configure("Treeview", background="#728c8d",
                    fieldbackground="#728c8d" ,foreground="black")
    orders.column("CustID", width=50)
    orders.column('Fname', width=50)
    orders.column('Sname', width=50)
    orders.column('Address', width=110)
    orders.column('PhoneNo', width=80)
    orders.column('Email', width=180)
    orders.column('Postcode', width=70)

    # define headings
    orders.heading('CustID', text='CustID')
    orders.heading('Fname', text='Fname')
    orders.heading('Sname', text='Sname')
    orders.heading('Address', text='Address')
    orders.heading('PhoneNo', text='PhoneNo')
    orders.heading('Email', text='Email')
    orders.heading('Postcode', text='Postcode')








    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cust_details")
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
    customer_table_view()
    pass