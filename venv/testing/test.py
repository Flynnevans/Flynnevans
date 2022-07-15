
from tkinter import *
from tkinter.ttk import *


from time import strftime


root = Tk()
root.title("Clock")
root.geometry("500x350")
root.config(bg="#728c8d")




def clock():
    string = strftime('%H:%M:%S %p \n %x')
    lbl.config(text=string)
    lbl.after(1000, time)
    lbl.grid(row=1,column=2)



lbl = Label(root, font=("calibri", 10, "bold"),
            background="#728c8d",
            foreground="black")


#lbl.pack(anchor="center")
time()

mainloop()