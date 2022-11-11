from tkinter import *
import sqlite3
from time import strftime
from tkinter import messagebox
from loginSignup import insertdata
import validation

def windowswap(close, open):
    close
    open

def order_details():
    orderDet = Tk()
    orderDet.title("Order Details")
    orderDet.geometry("350x525")
    orderDet.config(bg="#728c8d")

    titleFrame = Frame(orderDet, bg="#728c8d", width="350", height="50")
    titleFrame.grid(column=0, row=0)
    detailsFrame = Frame(orderDet, bg="#728c8d", width="350", height="350")
    detailsFrame.grid(column=0, row=1)
    dateframe = Frame(orderDet, bg="#728c8d", width="350", height="50")
    dateframe.grid(column=0, row=2)
    buttonFrame = Frame(orderDet, bg="#728c8d", width="350", height="100")
    buttonFrame.grid(column=0, row=3)

    welcomelabel = Label(titleFrame, text="Order Details")
    welcomelabel.config(font=("arial", 20))
    welcomelabel.config(bg="#728c8d", justify='center')
    welcomelabel.grid(row=0, column=0, columnspan=1, sticky="E", pady=30, padx=60)

    length_label = Label(detailsFrame, text="Length(CM):")
    length_label.config(font=("arial", 9), bg="#728c8d")
    length_label.grid(row=0, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    length_input = IntVar()
    lengthinput = Entry(detailsFrame, width=15, bg="#aaaaaa", textvariable=length_input)
    lengthinput.grid(row=0, column=1, padx=10, pady=10)
    # -----------------------------

    width_label = Label(detailsFrame, text="Width(CM):")
    width_label.config(font=("arial", 9), bg="#728c8d")
    width_label.grid(row=1, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    width_input = IntVar()
    widthinput = Entry(detailsFrame, width=15, bg="#aaaaaa", textvariable=width_input)
    widthinput.grid(row=1, column=1, padx=10, pady=10)
    # -------------------------------

    depth_label = Label(detailsFrame, text="Depth(CM):")
    depth_label.config(font=("arial", 9), bg="#728c8d")
    depth_label.grid(row=2, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    depth_input = IntVar()
    depthinput = Entry(detailsFrame, width=15, bg="#aaaaaa", textvariable=depth_input)
    depthinput.grid(row=2, column=1, padx=10, pady=10)
    # -------------------------------

    concrete_label = Label(detailsFrame, text="Concrete:")
    concrete_label.config(font=("arial", 9), bg="#728c8d")
    concrete_label.grid(row=3, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    options = ["Gen1 S2",
               "Gen3 S2",
               "C16/20 S2",
               "C20/25 S2",
               "C25/30 S2",
               "C28/35 S2",
               "RC28/35 S2",
               "C32/40 S2"]

    Con_type_input = StringVar()
    Con_type_input.set("CEM1 ")
    Con_typeinput = OptionMenu(detailsFrame, Con_type_input, *options)
    Con_typeinput.config(bg="#aaaaaa")
    Con_typeinput.grid(row=3, column=1, padx=10, pady=10)

    # -------------------------------

    date_label = Label(dateframe, text="Date:")
    date_label.config(font=("arial", 9), bg="#728c8d")
    date_label.grid(row=0, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    days = ["1","2","3","4","5","6","7","8","9","10",
            "11","12","13","14","15","16","17","18",
            "19","20","21","22","23","24","25","26",
            "27","28","29","30","31"]

    day_input = IntVar()
    day_input.set("DD")
    dayinput = OptionMenu(dateframe, day_input, *days)
    dayinput.config(bg="#aaaaaa")
    dayinput.grid(row=0, column=1, padx=5, pady=10)


    month = ["1", "2", "3", "4", "5", "6", "7", "08", "09", "10",
            "11", "12"]

    month_input = IntVar()
    month_input.set("MM")
    monthinput = OptionMenu(dateframe, month_input, *month)
    monthinput.config(bg="#aaaaaa")
    monthinput.grid(row=0, column=2, padx=5, pady=10)



    year = ["2022", "2023"]

    year_input = IntVar()
    year_input.set("YYYY")
    yearinput = OptionMenu(dateframe, year_input, *year)
    yearinput.config(bg="#aaaaaa")
    yearinput.grid(row=0, column=3, padx=5, pady=10)
    # -------------------------------

    time_label = Label(detailsFrame, text="Time(HH:MM):")
    time_label.config(font=("arial", 9), bg="#728c8d")
    time_label.grid(row=4, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    time_input = StringVar()
    timeinput = Entry(detailsFrame, width=15, bg="#aaaaaa", textvariable=time_input)
    timeinput.grid(row=4, column=1, padx=10, pady=10)

    AMPM_input = StringVar()
    AMPM_input.set("AM/PM")
    AMPMinput = OptionMenu(detailsFrame, AMPM_input, "AM", "PM")
    AMPMinput.config(bg="#aaaaaa")
    AMPMinput.grid(row=4, column=2, padx=10, pady=10)



    #-----------------------------------

    accepted_label = Label(dateframe, text="Accepted:")
    accepted_label.config(font=("arial", 9), bg="#728c8d")
    accepted_label.grid(row=2, column=1, columnspan=1, sticky="N", pady=10, padx=10)

    accepted_input = StringVar()
    accepted_input.set("Y/N")
    acceptedinput = OptionMenu(dateframe, accepted_input, "Yes","No")
    acceptedinput.config(bg="#aaaaaa")
    acceptedinput.grid(row=2, column=2, padx=10, pady=10)



    def orderlist():
        global orderdetails


        if AMPM_input.get() == "AM" and int(time_input.get()[0:2]) < 7:
            messagebox.showinfo("info", "invalid time")

        if AMPM_input.get() == "PM":
            if int(time_input.get()[0:1]) >= 5 and int(time_input.get()[0:1]) != 12:
                messagebox.showinfo("info", "invalid time")

        if int(time_input.get()[0:1]) > 12:
            messagebox.showinfo("info", "invalid time")

        if int(time_input.get()[3:5]) > 59:
            messagebox.showinfo("info", "invalid time")




        else:
            volume = (length_input.get() * width_input.get() * depth_input.get()) / 1000000
            if volume > 6:
                messagebox.showinfo("Warning", "Additional delivery charge will be added as extra mixer will be needed")

            else:
                if Con_type_input.get() == "CEM1 ":
                    messagebox.showinfo("info",
                                        "No concrete type has been entered")
                else:

                    AMPM = AMPM_input.get()
                    time = time_input.get()
                    length = length_input.get()
                    width = width_input.get()
                    depth = depth_input.get()
                    concrete = Con_type_input.get()
                    accepted = accepted_input.get()
                    day = day_input.get()
                    month = month_input.get()
                    year = year_input.get()




                    a = strftime('%x')
                    x = str(year_input.get())
                    y = str(month_input.get())
                    z = str(day_input.get())
                    if int(a[6:8]) < int(x[2:4]):
                        insert_orders(length, width, depth, concrete, accepted, day, month, year, time, AMPM)
                    elif int(a[6:8]) == int(x[2:4]):

                        if int(a[3:5]) < int(y):
                            insert_orders(length, width, depth, concrete, accepted, day, month, year, time, AMPM)
                        elif int(a[3:5]) == int(y):
                            if int(a[0:2]) < int(z):
                                insert_orders(length, width, depth, concrete, accepted, day, month, year, time, AMPM)
                            elif int(a[0:2]) == int(z):
                                messagebox.showinfo("Info", "Same day delivery is not available")
                            else:
                                messagebox.showinfo("Error", "That date is invalid")
                        else:
                            messagebox.showinfo("Error", "That date is invalid")
                    else:
                        messagebox.showinfo("Error", "That date is invalid")


    confirm_button = Button(buttonFrame, text="Confirm", width=12, height=3, bg="#C6CFFF",
                          command=lambda: orderlist())
    confirm_button.grid(row=0, column=0, padx=25, pady=10)

    return_button = Button(buttonFrame, text="Return", width=12, height=3, bg="#C6CFFF",
                           command=lambda: windowswap(orderDet.destroy(), new_customerwindow()))
    return_button.grid(row=0, column=1, padx=25, pady=10)

    orderDet.mainloop()

def insert_orders(length, width, depth, concrete, accepted, day, month, year, time, AMPM):
    global orderdetails
    volume = (length * width * depth) / 1000000
    orderdetails = [length, width, depth, concrete, accepted, day, month, year, time, AMPM]

    messagetext = ((volume), " Cubic meters of ", concrete, " to be delivered on ", (day), "/",
                   (month), "/", (year), " at", (time), (AMPM))

    result = messagebox.askquestion('Confirm', messagetext)
    if result == 'yes':
        print("")
        # insert into database
    else:
        windowswap(orderDet.destroy(), order_details())



def new_customerwindow():

    newcustomer = Tk()
    newcustomer.title("New customer")
    newcustomer.geometry("350x450")
    newcustomer.config(bg="#728c8d")

    titleFrame = Frame(newcustomer, bg="#728c8d", width="350", height="50")
    titleFrame.grid(column=0, row=0)
    detailsFrame = Frame(newcustomer, bg="#728c8d", width="350", height="300")
    detailsFrame.grid(column=0, row=1)
    buttonFrame = Frame(newcustomer,bg="#728c8d", width="350", height="100")
    buttonFrame.grid(column=0, row=2)

    welcomelabel = Label(titleFrame, text="Customer Details")
    welcomelabel.config(font=("arial", 20))
    welcomelabel.config(bg="#728c8d", justify='center')
    welcomelabel.grid(row=0, column=0, columnspan=1, sticky="E", pady=30, padx=60)



    fname_label = Label(detailsFrame, text="First Name:")
    fname_label.config(font=("arial", 9), bg="#728c8d")
    fname_label.grid(row=0, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    firstName_input = StringVar()
    firstnameinput = Entry(detailsFrame, width=15, bg="#aaaaaa", textvariable=firstName_input)
    firstnameinput.grid(row=0, column=1, padx=10, pady=10)
    # -----------------------------

    sname_label = Label(detailsFrame, text="Surname Name:")
    sname_label.config(font=("arial", 9), bg="#728c8d")
    sname_label.grid(row=1, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    surname_input = StringVar()
    surnameinput = Entry(detailsFrame, width=15, bg="#aaaaaa", textvariable=surname_input)
    surnameinput.grid(row=1, column=1, padx=10, pady=10)
    # -------------------------------

    address_label = Label(detailsFrame, text="Address:")
    address_label.config(font=("arial", 9), bg="#728c8d")
    address_label.grid(row=2, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    address_input = StringVar()
    addressinput = Entry(detailsFrame, width=15, bg="#aaaaaa", textvariable=address_input)
    addressinput.grid(row=2, column=1, padx=10, pady=10)
    # -------------------------------

    postcode_label = Label(detailsFrame, text="Postcode:")
    postcode_label.config(font=("arial", 9), bg="#728c8d")
    postcode_label.grid(row=3, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    postcode_input = StringVar()
    postcodeinput = Entry(detailsFrame, width=15, bg="#aaaaaa", textvariable=postcode_input)
    postcodeinput.grid(row=3, column=1, padx=10, pady=10)

    # -------------------------------

    phone_label = Label(detailsFrame, text="Phone Number:")
    phone_label.config(font=("arial", 9), bg="#728c8d")
    phone_label.grid(row=4, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    phone_input = StringVar()
    phoneinput = Entry(detailsFrame, width=15, bg="#aaaaaa", textvariable=phone_input)
    phoneinput.grid(row=4, column=1, padx=10, pady=10)

    #----------------------------------

    email_label = Label(detailsFrame, text="Email Address:")
    email_label.config(font=("arial", 9), bg="#728c8d")
    email_label.grid(row=5, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    email_input = StringVar()
    emailinput = Entry(detailsFrame, width=15, bg="#aaaaaa", textvariable=email_input)
    emailinput.grid(row=5, column=1, padx=10, pady=10)



    def customerlist():
        global customerdetails
        fname = firstName_input.get()
        sname = surname_input.get()
        address = address_input.get()

        if validation.postcodeIsValid(postcode_input.get()) == True:
            postcode = postcode_input.get()

            if validation.len_validation(phone_input.get(),11,1) == True:
                phonenumber = phone_input.get()

                if validation.isvalidEmail(email_input.get()) == True:
                    email = email_input.get()

                    customerdetails = [fname,sname,address,postcode,phonenumber,email]
                    windowswap(newcustomer.destroy(), order_details())
                else:
                    messagebox.showinfo("info", "Email address was invalid")
            else:
                messagebox.showinfo("info", "Phone number was invalid")
        else:
            messagebox.showinfo("info", "Postcode was invalid / out of range")





    order_button = Button(buttonFrame, text="Create Order", width=12, height=3, bg="#C6CFFF",
                           command=lambda: customerlist())
    order_button.grid(row=0, column=0, padx=25, pady=10)

    return_button = Button(buttonFrame, text="Return Home", width=12, height=3, bg="#C6CFFF",
                           command=lambda: windowswap(newcustomer.destroy(), homepage()))
    return_button.grid(row=0, column=1, padx=25, pady=10)



    newcustomer.mainloop()




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
    home.geometry("570x350")
    home.config(bg="#728c8d")
    my_menu = Menu(home)
    home.config(menu=my_menu)

    blankFrame = Frame(home, bg="#728c8d", width="60", height="100")
    blankFrame.grid(column=0, row=0)

    blankFrame2 = Frame(home, bg="#728c8d", width="10", height="100")
    blankFrame2.grid(column=1, row=0)


    titleFrame = Frame(home, bg="#728c8d", width="310", height="100")
    titleFrame.grid(column=2, row=0)

    blankFrame3 = Frame(home, bg="#728c8d", width="10", height="100")
    blankFrame3.grid(column=3, row=0)

    blankFrame4 = Frame(home, bg="#728c8d", width="60", height="100")
    blankFrame4.grid(column=4, row=0)

    left_frame = Frame(home, bg="#728c8d",width="60", height="250")
    left_frame.grid(column=0, row=1)

    centerleft_frame=Frame(home, bg="#728c8d",width="10", height="250")
    centerleft_frame.grid(column=1, row=1)

    center_frame = Frame(home, bg="#728c8d", width="310", height="250")
    center_frame.grid(column=2, row=1)

    centerright_frame = Frame(home, bg="#728c8d", width="10", height="250")
    centerright_frame.grid(column=3, row=1)

    right_frame = Frame(home, bg="#728c8d", width="60", height="250")
    right_frame.grid(column=4, row=1)

    # -----------------------------------------
    newcustomer_button = Button(left_frame, text="New", width=12, height=3, bg="#C6CFFF",
                           command=lambda:windowswap(home.destroy(), new_customerwindow()))
    newcustomer_button.grid(row=1, column=1, padx=10, pady=10)

    oldcustomer_button = Button(right_frame, text="Returning", width=12, height=3, bg="#C6CFFF",
                                command=lambda: filler())
    oldcustomer_button.grid(row=1, column=1, padx=10, pady=10)
    # --------------------------------------

    welcomelabel = Label(titleFrame, text="Welcome to Mincrete")
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
        a = strftime('%x')
        lbl.config(text=string)
        lbl.after(1000,time)
        lbl.grid(column=0,row=1,sticky="S")
    time()

    welcomelabel = Label(center_frame, text="Todays Orders:")
    welcomelabel.config(font=("Ariel", 10))
    welcomelabel.config(bg="#728c8d")
    welcomelabel.grid(row=0, column=0,sticky="N", pady=10, padx=10)


    home.mainloop()


order_details()



