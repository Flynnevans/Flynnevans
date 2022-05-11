from tkinter import *
import PIL

def signup_window():
    signup_page = Tk()
    signup_page.title("signup Page")
    signup_page.geometry("400x300")
    signup_page.config(bg="#2f9066")

    signup_label = Label(signup_page, text="Sign up now")
    signup_label.config(font=("arial", 12))
    signup_label.config(bg="#2f9066")
    signup_label.grid(row=0, column=1, columnspan=2, sticky="NSW", pady=10, padx=0)

    userlabel = Label(signup_page, text="Username:")
    userlabel.config(font=("arial", 9),bg= "#2f9066")
    userlabel.grid(row=1, column=0, columnspan=1, sticky="E", pady=10, padx=10)

    passlabel = Label(signup_page, text="Password:")
    passlabel.config(font=("arial", 9),bg= "#2f9066")
    passlabel.grid(row=2, column=0, columnspan=1, sticky="NE", pady=10, padx=10)

    userenter = Entry(signup_page, width=15, bg="#2f9066")
    userenter.grid(row=1, column=1, padx=10, pady=10, sticky="SE")

    passenter = Entry(signup_page, width=15, bg="#2f9066")
    passenter.grid(row=2, column=1, padx=10, pady=10, sticky="SE")

    repassenter = Entry(signup_page, width=15, bg="#2f9066")
    repassenter.grid(row=3, column=1, padx=10, pady=10, sticky="SE")

    rePasslabel = Label(signup_page, text="Re-enter Password:")
    rePasslabel.config(font=("arial", 9), bg="#2f9066")
    rePasslabel.grid(row=3, column=0, columnspan=1, sticky="NW", pady=10, padx=10)

    signup_lable = Button(signup_page, text="Sign up", width=8, height=2, bg="#C6CFFF")
    signup_lable.grid(row=4, column=0, padx=10, pady=10, sticky="E")

    backup_lable = Button(signup_page, text="Back", width=8, height=2, bg="#C6CFFF", command=signup_page.destroy)
    backup_lable.grid(row=4, column=1, padx=10, pady=10, sticky="E")



def login_window():
    login_page = Tk()
    login_page.title("Login Page")
    login_page.geometry("400x300")
    login_page.config(bg="#2f9066")

    login_label = Label(login_page, text="Login now")
    login_label.config(font=("arial", 12))
    login_label.config(bg="#2f9066")
    login_label.grid(row=0, column=1, columnspan=1, sticky="NSEW", pady=10, padx=10)

    loginlabel = Label(login_page, text="Username:")
    loginlabel.config(font=("arial", 9), bg="#2f9066")
    loginlabel.grid(row=1, column=0, columnspan=1, sticky="E", pady=10, padx=10)

    loginlabel = Label(login_page, text="Password:")
    loginlabel.config(font=("arial", 9), bg="#2f9066")
    loginlabel.grid(row=2, column=0, columnspan=1, sticky="NE", pady=10, padx=10)

    loginenter = Entry(login_page, width=15, bg="#2f9066")
    loginenter.grid(row=1, column=1, padx=10, pady=10, sticky="SE")

    loginenter = Entry(login_page, width=15, bg="#2f9066")
    loginenter.grid(row=2, column=1, padx=10, pady=10, sticky="SE")

    login_lable = Button(login_page, text="Login", width=8, height=2, bg="#C6CFFF")
    login_lable.grid(row=3, column=0, padx=10, pady=10, sticky="E")


    backup_lable = Button(login_page, text="Back", width=8, height=2, bg="#C6CFFF", command=login_page.destroy)
    backup_lable.grid(row=3, column=2, padx=10, pady=10, sticky="E")


def CreateGUI():
    page = Tk()
    page.title ("Main Page")
    page.geometry ("400x300")
    page.config(bg="#2f9066")

    welcomelabel = Label(page, text="Welcome to Main")
    welcomelabel.config(font=("arial", 12))
    welcomelabel.config(bg= "#2f9066")
    welcomelabel.grid(row = 0, column = 1, columnspan= 1, sticky = "E", pady =10, padx= 10)

    exit_lable = Button(page, text="Exit", width = 8,height= 2 ,command = quit, bg= "#C6CFFF")
    exit_lable.grid(row=3, column =0 , padx=10 , pady=10, sticky = "S")

    signup_lable=Button(page,text="Sign up",width=8,height= 2 , bg= "#C6CFFF",command=signup_window)
    signup_lable.grid(row=3,column=1,padx=10,pady=10,sticky="S")

    login_lable = Button(page, text="Login", width=8,height= 2 , bg= "#C6CFFF",command=login_window)
    login_lable.grid(row=3, column=2, padx=10, pady=10, sticky="SE")



    page.mainloop()


CreateGUI()