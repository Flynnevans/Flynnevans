#from datetime import datetime


#def validate_date(d):
   # try:
    #    datetime.strptime(d, '%d/%m/%Y %I:%M %p')
    #    return True
    #except ValueError:
    #    return False

#if (validate_date("2/2/2009 3:00 PM")):
   # print("hello")

#try:
 #   print(x)
#except:
 #   print("error")



#username = "phill"
#namebank = ["jon", "jill", "mike", "elliot", "phill"]
#print(namebank.index(username))


# from tkinter import *
#
# win = Tk()
# win.geometry ("400x300")
# sbb = Scrollbar(win)
#
# sbb.pack(side=RIGHT, fill=Y)
#
# mylist = Listbox(win, yscrollcommand=sbb.set)
#
#
name = "flynn evans"
address = "3 woodbridge road"
phone = "07555 942035"
# mylist.insert(END,str(name) +", "+ str(address) + ", " + str(phone))
#
#
# mylist.pack(side=LEFT)
# sbb.config(command=mylist.yview)
#
# mainloop()


import tkinter as tk

root = tk.Tk()
scrollbar = tk.Scrollbar(root, orient="vertical")
lb = tk.Listbox(root, width=50, height=20, yscrollcommand=scrollbar.set)
scrollbar.config(command=lb.yview)

scrollbar.pack(side="right", fill="y")
lb.pack(side="left",fill="both", expand=True)

for i in range(0,30):
    lb.insert("end", "order #07652 "+ " flynn alan evans " +" 3 woodbridge rd "+" 07555 942035 ")

root.mainloop()