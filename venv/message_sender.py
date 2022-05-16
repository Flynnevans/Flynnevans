from tkinter import *
from tkinter import messagebox

def re_enter(title,message):
    page = Tk()
    messagebox.askretrycancel(title,message)
    page.quit()
    page.mainloop


