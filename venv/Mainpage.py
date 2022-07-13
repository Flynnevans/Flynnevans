from tkinter import *
from LoginPage_GUI import windowswap
from time import strftime

def clock():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)



def accountsPage():

    accounts = Tk()
    accounts.title("Accounts")
    accounts.geometry("550x350")
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

    home_menu.add_command(label="Home", command=lambda: windowswap(accounts.destroy(), homepage()))
    home_menu.add_command(label="Exit", command=lambda: accounts.destroy())

    accounts_menu.add_command(label="Accounts", command=lambda: windowswap(accounts.destroy(), accountsPage()))



    accounts.mainloop()

def homepage():
    home = Tk()
    home.title("home")
    home.geometry("550x350")
    home.config(bg="#728c8d")
    my_menu = Menu(home)
    home.config(menu=my_menu)

    blankFrame = Frame(home, bg="#728c8d", width="125", height="100")
    blankFrame.grid(column=0, row=0)

    titleFrame = Frame(home, bg="#728c8d", width="550", height="100")
    titleFrame.grid(column=1, row=0)


    welcomelabel = Label(titleFrame, text="Welcome to mincrete")
    welcomelabel.config(font=("arial", 20))
    welcomelabel.config(bg="#728c8d", justify='center')
    welcomelabel.grid(row=0, column=1, columnspan=1, sticky="NSEW", pady=10, padx=10)

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

    home.mainloop()





accountsPage()