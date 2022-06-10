from tkinter import *
from login import *

def login_window():

    login_page = Tk()
    login_page.title("Login Page")
    login_page.geometry("800x600")
    login_page.config(bg="#728c8d")

    login_label = Label(login_page, text="Login now")
    login_label.config(font=("arial", 12))
    login_label.config(bg="#728c8d")
    login_label.grid(row=0, column=1, columnspan=1, sticky="NSEW", pady=10, padx=10)

    loginlabel = Label(login_page, text="Username:")
    loginlabel.config(font=("arial", 9), bg="#728c8d")
    loginlabel.grid(row=1, column=0, columnspan=1, sticky="E", pady=10, padx=10)

    User_input = StringVar()
    Userinput = Entry(login_page, width=15, bg="#728c8d", textvariable=User_input)
    Userinput.grid(row=1, column=1, padx=10, pady=10, sticky="SE")



    loginlabel = Label(login_page, text="Password:")
    loginlabel.config(font=("arial", 9), bg="#728c8d")
    loginlabel.grid(row=2, column=0, columnspan=1, sticky="NE", pady=10, padx=10)

    Pass_input = StringVar()
    Passinput = Entry(login_page, width=15, bg="#728c8d", textvariable=Pass_input)
    Passinput.grid(row=2, column=1, padx=10, pady=10, sticky="SE")






    login_lable = Button(login_page, text="Login", width=8, height=2, bg= "#C6CFFF", command=lambda: username_validation(Userinput.get(),Passinput.get()))
    login_lable.grid(row=3, column=0, padx=10, pady=10, sticky="E")

    backup_lable = Button(login_page, text="Back", width=8, height=2, bg= "#C6CFFF", command=login_page.destroy)
    backup_lable.grid(row=3, column=2, padx=10, pady=10, sticky="E")

    mainloop()

def mainpage_GUI():

    page = Tk()
    page.title ("Main Page")
    page.geometry ("800x600")
    page.config(bg="#728c8d")

    welcomelabel = Label(page, text="Welcome to Main")
    welcomelabel.config(font=("arial", 12))
    welcomelabel.config(bg= "#728c8d")
    welcomelabel.grid(row = 0, column = 1, columnspan= 1, sticky = "NSEW", pady =10, padx= 10)

    exit_lable = Button(page, text="Exit", width = 20,height= 5 ,command = quit, bg= "#C6CFFF")
    exit_lable.grid(row=3, column =0 , padx=10 , pady=10, sticky = "S")

    login_lable = Button(page, text="Login", width=20, height=5, bg="#C6CFFF", command=login_window)
    login_lable.grid(row=3, column=1, padx=10, pady=10, sticky="SE")



    page.mainloop()

mainpage_GUI()