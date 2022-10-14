from tkinter import *
import sqlite3
from time import strftime
from tkinter import messagebox
from loginSignup import insertdata

def windowswap(close, open):
    close
    open


def account_add():

    accounts = Tk()
    accounts.title("Create account")
    accounts.geometry("200x150")
    accounts.config(bg="#728c8d")

    textFrame = Frame(accounts, bg="#728c8d", width="200", height="90")
    textFrame.grid(column=0, row=0)
    buttonFrame = Frame(accounts, bg="#728c8d", width="200", height="60")
    buttonFrame.grid(column=0, row=1)

    User_input = StringVar()
    Userinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=User_input)
    Userinput.grid(row=0, column=1, padx=10, pady=10)

    Pass_input = StringVar()
    Passinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=Pass_input)
    Passinput.grid(row=1, column=1, padx=10, pady=10)

    username_label = Label(textFrame, text="Username:")
    username_label.config(font=("arial", 9), bg="#728c8d")
    username_label.grid(row=0, column=0, columnspan=1, sticky="NE", pady=10, padx=10)

    password_label = Label(textFrame, text="Password:")
    password_label.config(font=("arial", 9), bg="#728c8d")
    password_label.grid(row=1, column=0, columnspan=1, sticky="NE", pady=10, padx=10)

    create_button = Button(buttonFrame, text="Create account", width=12, height=3, bg="#C6CFFF",
                        command= lambda: insertdata(Userinput.get(), Passinput.get()))
    create_button.grid(row=1, column=2, padx=25, pady=10)

    accounts_add.mainloop()

def updatepass_user(username, newpass):
    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Login_details Set Password = ? WHERE Username = ?", newpass, username)
    conn.commit()
    messagebox.showinfo("info", "signup was successful")
    conn.close()


def pass_editor(username, password1):
    pass_edit = Tk()
    pass_edit.title("Editor")
    pass_edit.geometry("300x150")
    pass_edit.config(bg="#728c8d")

    textFrame = Frame(pass_edit, bg="#728c8d", width="200", height="90")
    textFrame.grid(column=0, row=0)
    buttonFrame = Frame(pass_edit, bg="#728c8d", width="200", height="60")
    buttonFrame.grid(column=0, row=1)

    newPass_input = StringVar()
    newPassinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=newPass_input)
    newPassinput.grid(row=1, column=1, padx=10, pady=10)

    password_label = Label(textFrame, text="New Password:")
    password_label.config(font=("arial", 9), bg="#728c8d")
    password_label.grid(row=1, column=0, columnspan=1, sticky="NE", pady=10, padx=10)

    conn = sqlite3.connect('Mincrete.db')
    cursor = conn.cursor()

    edit_pass_button = Button(buttonFrame, text="Edit Password", width=12, height=3, bg="#C6CFFF",
                              command=lambda: updatepass_user(username,newPass_input))
    edit_pass_button.grid(row=1, column=1, padx=25, pady=10)




def account_edit():
    accounts_edit = Tk()
    accounts_edit.title("Edit")
    accounts_edit.geometry("300x150")
    accounts_edit.config(bg="#728c8d")

    textFrame = Frame(accounts_edit, bg="#728c8d", width="200", height="90")
    textFrame.grid(column=0, row=0)
    buttonFrame = Frame(accounts_edit, bg="#728c8d", width="200", height="60")
    buttonFrame.grid(column=0, row=1)

    User_input = StringVar()
    Userinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=User_input)
    Userinput.grid(row=0, column=1, padx=10, pady=10)

    Pass_input = StringVar()
    Passinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=Pass_input)
    Passinput.grid(row=1, column=1, padx=10, pady=10)

    username_label = Label(textFrame, text="Username:")
    username_label.config(font=("arial", 9), bg="#728c8d")
    username_label.grid(row=0, column=0, columnspan=1, sticky="NE", pady=10, padx=10)

    password_label = Label(textFrame, text="Password:")
    password_label.config(font=("arial", 9), bg="#728c8d")
    password_label.grid(row=1, column=0, columnspan=1, sticky="NE", pady=10, padx=10)

    editpass_button = Button(buttonFrame, text="Edit password", width=12, height=3, bg="#C6CFFF",
                           command=lambda: (pass_editor(Userinput.get(), Passinput.get())))
    editpass_button.grid(row=1, column=2, padx=25, pady=10)

    edit_user_button = Button(buttonFrame, text="Edit username", width=12, height=3, bg="#C6CFFF",
                         command=lambda: (editor(Userinput.get(), Passinput.get())))
    edit_user_button.grid(row=1, column=1, padx=25, pady=10)

    accounts_edit.mainloop()

def accountsPage():



    accounts = Tk()
    accounts.title("Accounts")
    accounts.geometry("450x200")

    accounts.config(bg="#728c8d")

    account_menu = Menu(accounts)
    accounts.config(menu=account_menu)


    home_menu = Menu(account_menu)
    accounts_menu = Menu(account_menu)
    orders_menu = Menu(account_menu)
    calculator_menu = Menu(account_menu)
    schedule_menu = Menu(account_menu)

    account_menu.add_cascade(label="Home", menu=home_menu)
    account_menu.add_cascade(label="Accounts", menu=accounts_menu)
    account_menu.add_cascade(label="Orders", menu=orders_menu)
    account_menu.add_cascade(label="Calculator", menu=calculator_menu)
    account_menu.add_cascade(label="Schedule", menu=schedule_menu)

    textFrame = Frame(accounts, bg="#728c8d", width="450", height="100")
    textFrame.grid(column=0, row=0)

    buttonFrame = Frame(accounts, bg="#728c8d", width="450", height="100")
    buttonFrame.grid(column=0, row=1)

    home_menu.add_command(label="Home", command=lambda: windowswap(accounts.destroy(), homepage()))
    home_menu.add_command(label="Exit", command=lambda: accounts.destroy())

    accounts_menu.add_command(label="Accounts", command=lambda: windowswap(accounts.destroy(), accountsPage()))

    edit_button = Button(buttonFrame, text="Edit account", width=12, height=3, bg="#C6CFFF",
                           command=lambda: account_edit())
    edit_button.grid(row=1, column=0, padx=25, pady=10)
    # ===================================================================================
    remove_button = Button(buttonFrame, text="Remove account", width=12, height=3, bg="#C6CFFF",
                         command=lambda: account_delete())
    remove_button.grid(row=1, column=1, padx=25, pady=10)
    # ================================================================================
    add_button = Button(buttonFrame, text="Create account", width=12, height=3, bg="#C6CFFF",
                         command=lambda: account_add())
    add_button.grid(row=1, column=2, padx=25, pady=10)

    accountMenu_label = Label(textFrame, text="Welcome to the accounts page")
    accountMenu_label.config(font=("arial", 12))
    accountMenu_label.config(bg="#728c8d")
    accountMenu_label.grid(row=0, column=0, columnspan=1, sticky="NSEW", pady=10, padx=10)


    accounts.mainloop()




def homepage():
    home = Tk()
    home.title("home")
    home.geometry("550x350")
    home.config(bg="#728c8d")
    my_menu = Menu(home)
    home.config(menu=my_menu)

    blankFrame = Frame(home, bg="#728c8d", width="120", height="100")
    blankFrame.grid(column=0, row=0)

    titleFrame = Frame(home, bg="#728c8d", width="310", height="100")
    titleFrame.grid(column=1, row=0)

    blankFrame2 = Frame(home, bg="#728c8d", width="120", height="100")
    blankFrame2.grid(column=2, row=0)

    left_frame = Frame(home, bg="#728c8d",width="120", height="250")
    left_frame.grid(column=0, row=1)

    center_frame = Frame(home, bg="#728c8d", width="310", height="250")
    center_frame.grid(column=1, row=1)

    right_frame = Frame(home, bg="#728c8d", width="120", height="250")
    right_frame.grid(column=2, row=1)




    welcomelabel = Label(titleFrame, text="Welcome to mincrete")
    welcomelabel.config(font=("arial", 20))
    welcomelabel.config(bg="#728c8d", justify='center')
    welcomelabel.grid(row=0, column=1, columnspan=1, sticky="N", pady=30, padx=30)

    home_menu = Menu(my_menu)
    accounts_menu = Menu(my_menu)
    orders_menu = Menu(my_menu)
    calculator_menu = Menu(my_menu)
    schedule_menu = Menu(my_menu)

    my_menu.add_cascade(label="Home", menu=home_menu)
    my_menu.add_cascade(label="Accounts", menu=accounts_menu)
    my_menu.add_cascade(label="Orders", menu=orders_menu)
    my_menu.add_cascade(label="Calculator", menu=calculator_menu)
    my_menu.add_cascade(label="Schedule", menu=schedule_menu)

    home_menu.add_command (label="Home", command=lambda: windowswap(home.destroy(),homepage()))
    home_menu.add_command (label="Exit", command=lambda: home.destroy())

    accounts_menu.add_command(label="Accounts", command=lambda: windowswap(home.destroy(), accountsPage()))

    lbl = Label(center_frame, font=("calibri", 15, "bold"),
                background="#728c8d",
                foreground="black")

    def time():
        string = strftime('%H:%M:%S %p \n %x')
        lbl.config(text=string)
        lbl.after(1000,time)
        lbl.grid(column=0,row=1,sticky="S")
    time()

    welcomelabel = Label(center_frame, text="Todays Orders:")
    welcomelabel.config(font=("Ariel", 10))
    welcomelabel.config(bg="#728c8d")
    welcomelabel.grid(row=0, column=0,sticky="N", pady=10, padx=10)


    home.mainloop()






