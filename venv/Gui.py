from tkinter import *
from login import *

# def login_window():
#
#     login_page = Tk()
#     login_page.title("Login Page")
#     login_page.geometry("350x250")
#     login_page.config(bg="#728c8d")
#
#
#
#
#     login_label = Label(login_page, text="Login now")
#     login_label.config(font=("arial", 12))
#     login_label.config(bg="#728c8d")
#     login_label.grid(row=0, column=1, columnspan=1, sticky="NSEW", pady=10, padx=10)
#
#     loginlabel = Label(login_page, text="Username:")
#     loginlabel.config(font=("arial", 9), bg="#728c8d")
#     loginlabel.grid(row=1, column=0, columnspan=1, sticky="E", pady=10, padx=10)
#
#     User_input = StringVar()
#     Userinput = Entry(login_page, width=15, bg="#728c8d", textvariable=User_input)
#     Userinput.grid(row=1, column=1, padx=10, pady=10, sticky="SE")
#
#
#
#     loginlabel = Label(login_page, text="Password:")
#     loginlabel.config(font=("arial", 9), bg="#728c8d")
#     loginlabel.grid(row=2, column=0, columnspan=1, sticky="NE", pady=10, padx=10)
#
#     Pass_input = StringVar()
#     Passinput = Entry(login_page, width=15, bg="#728c8d", textvariable=Pass_input)
#     Passinput.grid(row=2, column=1, padx=10, pady=10, sticky="SE")
#
#
#     login_lable = Button(login_page, text="Login", width=8, height=2, bg= "#C6CFFF", command=lambda: username_validation(Userinput.get(),Passinput.get()))
#     login_lable.grid(row=3, column=0, padx=10, pady=10, sticky="E")
#
#     backup_lable = Button(login_page, text="Back", width=8, height=2, bg= "#C6CFFF", command=login_page.destroy)
#     backup_lable.grid(row=3, column=2, padx=10, pady=10, sticky="E")
#
#     mainloop()


def login_window():
    login_page = Tk()
    login_page.title("Login Page")
    login_page.geometry("350x250")
    login_page.config(bg="#728c8d")

#create 2 frames grid them in 1 column in column 0
    textFrame = Frame(login_page, bg="red", width="350", height="150")
    textFrame.grid(column = 0, row = 0)
    buttonFrame = Frame(login_page, bg = "blue", width = "350", height="100")
    buttonFrame.grid(column = 0, row = 1)

    login_label = Label(textFrame, text="Login now")
    login_label.config(font=("arial", 12))
    login_label.config(bg="#728c8d")
    login_label.grid(row=0, column=1, columnspan=1, sticky="NSEW", pady=10, padx=10)

    loginlabel = Label(textFrame, text="Username:")
    loginlabel.config(font=("arial", 9), bg="#728c8d")
    loginlabel.grid(row=1, column=0, columnspan=1, sticky="E", pady=10, padx=10)

    User_input = StringVar()
    Userinput = Entry(textFrame, width=15, bg="#728c8d", textvariable=User_input)
    Userinput.grid(row=1, column=1, padx=10, pady=10, sticky="SE")

    loginlabel = Label(textFrame, text="Password:")
    loginlabel.config(font=("arial", 9), bg="#728c8d")
    loginlabel.grid(row=2, column=0, columnspan=1, sticky="NE", pady=10, padx=10)

    Pass_input = StringVar()
    Passinput = Entry(textFrame, width=15, bg="#728c8d", textvariable=Pass_input)
    Passinput.grid(row=2, column=1, padx=10, pady=10, sticky="SE")

    login_button = Button(buttonFrame, text="Login", width=8, height=2, bg="#C6CFFF",
                         command=lambda: username_validation(Userinput.get(), Passinput.get()))
    login_button.grid(row=0, column=0, padx=10, pady=10, sticky="E")

    back_button = Button(buttonFrame, text="Back", width=8, height=2, bg="#C6CFFF", command=login_page.destroy)
    back_button.grid(row=0, column=2, padx=10, pady=10, sticky="E")

    mainloop()

def mainpage_GUI():

    page = Tk()

    page.title ("Main Page")
    page.geometry ("525x225")
    page.config(bg="#728c8d")


    welcomelabel = Label(page, text="Mincrete Database")
    welcomelabel.config(font=("arial", 20))
    welcomelabel.config(bg= "#728c8d")
    welcomelabel.grid(row = 0, column =1, columnspan= 1, sticky = "NSE", pady =10, padx= 10)

    exit_lable = Button(page, text="Exit", width = 15,height= 3 ,command = quit, bg= "#C6CFFF")
    exit_lable.grid(row=2, column =0 , padx=10 , pady=10, sticky = "S")

    login_lable = Button(page, text="Login", width=15, height=3, bg="#C6CFFF", command=login_window)
    login_lable.grid(row=2, column=1, padx=10, pady=10, sticky="S")

    signup_lable = Button(page, text="Signup", width=15, height=3, bg="#C6CFFF")
    signup_lable.grid(row=2, column=2, padx=10, pady=10, sticky="E")


    page.mainloop()

mainpage_GUI()