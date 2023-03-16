from tkinter import *
import sqlite3
from time import strftime
from tkinter import messagebox
import validation
from pricing import *
import database_manage
import orderview
import calculatorpage


def windowswap(close, open):
    close
    open

def homepageswap():
    order_Det.destroy()
    homepage()



# Define a function to display the order details window
def order_details(custdet):
    # Use global keyword to access and modify the customerdetails variable
    global customerdetails
    # Assign the customer details passed as an argument to the global variable
    customerdetails = custdet

    # Create a new window for the order details
    orderDet = Tk()
    orderDet.title("Order Details")
    orderDet.geometry("350x525")
    orderDet.config(bg="#728c8d")

    # Create different frames for different sections of the order details window
    titleFrame = Frame(orderDet, bg="#728c8d", width="350", height="50")
    titleFrame.grid(column=0, row=0)
    detailsFrame = Frame(orderDet, bg="#728c8d", width="350", height="350")
    detailsFrame.grid(column=0, row=1)
    dateframe = Frame(orderDet, bg="#728c8d", width="350", height="50")
    dateframe.grid(column=0, row=2)
    buttonFrame = Frame(orderDet, bg="#728c8d", width="350", height="100")
    buttonFrame.grid(column=0, row=3)

    # Add a label to the title frame
    welcomelabel = Label(titleFrame, text="Order Details")
    welcomelabel.config(font=("arial", 20))
    welcomelabel.config(bg="#728c8d", justify='center')
    welcomelabel.grid(row=0, column=0, columnspan=1, sticky="E", pady=30, padx=60)

    # Add a label and entry widget to the details frame for length input
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

    # Create a label widget for 'Concrete'
    concrete_label = Label(detailsFrame, text="Concrete:")
    concrete_label.config(font=("arial", 9), bg="#728c8d")
    concrete_label.grid(row=3, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    # Define the available options for concrete types
    options = ["Gen1",
               "Gen3",
               "C20",
               "C25",
               "C30",
               "C35",
               "C40"]

    # Create a variable to store the selected concrete type and set it to the default value
    Con_type_input = StringVar()
    Con_type_input.set("CEM1 S2 ")

    # Create an option menu widget for the concrete type selection
    Con_typeinput = OptionMenu(detailsFrame, Con_type_input, *options)
    Con_typeinput.config(bg="#aaaaaa")
    Con_typeinput.grid(row=3, column=1, padx=10, pady=10)

    # -------------------------------

    # Create a label widget for 'Date'
    date_label = Label(dateframe, text="Date:")
    date_label.config(font=("arial", 9), bg="#728c8d")
    date_label.grid(row=0, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    # Define the available options for days
    days = ["01", "02", "03", "04", "05", "06", "7", "8", "9", "10",
            "11", "12", "13", "14", "15", "16", "17", "18",
            "19", "20", "21", "22", "23", "24", "25", "26",
            "27", "28", "29", "30", "31"]

    # Create a variable to store the selected day and set it to the default value
    day_input = IntVar()
    day_input.set("DD")

    # Create an option menu widget for the day selection
    dayinput = OptionMenu(dateframe, day_input, *days)
    dayinput.config(bg="#aaaaaa")
    dayinput.grid(row=0, column=1, padx=5, pady=10)

    # Define the available options for months
    month = ["01", "02", "03", "04", "05", "06", "7", "8", "9", "10",
             "11", "12"]

    # Create a variable to store the selected month and set it to the default value
    month_input = IntVar()
    month_input.set("MM")

    # Create an option menu widget for the month selection
    monthinput = OptionMenu(dateframe, month_input, *month)
    monthinput.config(bg="#aaaaaa")
    monthinput.grid(row=0, column=2, padx=5, pady=10)

    # Define the available options for years
    year = ["2023", "2024", "2025"]

    # Create a variable to store the selected year and set it to the default value
    year_input = IntVar()
    year_input.set("YYYY")

    # Create an option menu widget for the year selection
    yearinput = OptionMenu(dateframe, year_input, *year)
    yearinput.config(bg="#aaaaaa")
    yearinput.grid(row=0, column=3, padx=5, pady=10)

    # -------------------------------

    # Create a label widget for 'Time'
    time_label = Label(detailsFrame, text="Time(HH:MM):")
    time_label.config(font=("arial", 9), bg="#728c8d")
    time_label.grid(row=4, column=0, columnspan=1, sticky="N", pady=10, padx=10)
    # Entry for time
    time_input = StringVar()
    timeinput = Entry(detailsFrame, width=15, bg="#aaaaaa", textvariable=time_input)
    timeinput.grid(row=4, column=1, padx=10, pady=10)
    # drop down menu for if the time is AM/PM
    AMPM_input = StringVar()
    AMPM_input.set("AM/PM")
    AMPMinput = OptionMenu(detailsFrame, AMPM_input, "AM", "PM")
    AMPMinput.config(bg="#aaaaaa")
    AMPMinput.grid(row=4, column=2, padx=10, pady=10)



    #-----------------------------------




    def orderlist():
        global orderdetails, price

        if AMPM_input.get() == "AM" and int(time_input.get()[0:2]) < 7:
            messagebox.showinfo("info", "invalid time")
            orderdetails(customerdetails)

        if AMPM_input.get() == "PM":
            if int(time_input.get()[0:1]) >= 5 and int(time_input.get()[0:1]) != 12:
                messagebox.showinfo("info", "invalid time")
                orderdetails(customerdetails)

        if int(time_input.get()[0:1]) > 12:
            messagebox.showinfo("info", "invalid time")
            orderdetails(customerdetails)


        if int(time_input.get()[3:5]) > 59:
            messagebox.showinfo("info", "invalid time")
            orderdetails(customerdetails)





        else:
            price = 0
            volume = (length_input.get() * width_input.get() * depth_input.get()) / 1000000
            if volume <0.5:
                messagebox.showinfo("Warning", "too little concrete ordered")
                windowswap(orderDet.destroy, homepage())
            if volume > 8:
                messagebox.showinfo("Warning", "Additional mixers will be needed")
            if volume > 30:
                messagebox.showinfo("Info","Price reduction due to mass buy")
                price = -150


            if Con_type_input.get() == "CEM1 S2 ":
                messagebox.showinfo("info",
                                    "No concrete type has been entered")
                homepage()
            else:

                AMPM = AMPM_input.get()
                time = time_input.get()
                length = length_input.get()
                width = width_input.get()
                depth = depth_input.get()
                concrete = Con_type_input.get()
                day = day_input.get()
                month = month_input.get()
                year = year_input.get()


                volume = (length * width * depth) / 1000000
                if volume > 8:
                    n = volume // 8
                    n = n * 1050
                    volume = volume // 8
                    preprice = (concrete_price(concrete, volume))
                    loads = volume // 8
                    price = preprice + (loads * 25) + n
                else:
                    price = (concrete_price(concrete, volume))




                a = strftime('%x')
                x = str(year_input.get())
                y = str(month_input.get())
                z = str(day_input.get())



                if int(a[6:8]) < int(x[2:4]):
                    insert_orders(length, width, depth, concrete, day, month, year, time, AMPM, price)
                elif int(a[6:8]) == int(x[2:4]):

                    if int(a[0:2]) < int(y):
                        insert_orders(length, width, depth, concrete, day, month, year, time, AMPM, price)
                    elif int(a[0:2]) == int(y):
                        if int(a[3:5]) < int(z):
                            insert_orders(length, width, depth, concrete, day, month, year, time, AMPM, price)
                        elif int(a[3:5]) == int(z):
                            messagebox.showinfo("Info", "Same day delivery is not available")
                            homepage()
                        else:
                            messagebox.showinfo("Error", "That date is invalid")
                            homepage()
                    else:
                        messagebox.showinfo("Error", "That date is invalid")
                        homepage()
                else:
                    messagebox.showinfo("Error", "That date is invalid")
                    homepage()


    confirm_button = Button(buttonFrame, text="Confirm", width=12, height=3, bg="#C6CFFF",
                          command=lambda: windowswap(orderDet.destroy(), orderlist()))
    confirm_button.grid(row=0, column=0, padx=25, pady=10)

    return_button = Button(buttonFrame, text="Return", width=12, height=3, bg="#C6CFFF",
                           command=lambda: windowswap(orderDet.destroy(), new_customerwindow()))
    return_button.grid(row=0, column=1, padx=25, pady=10)

    orderDet.mainloop()



def insert_orders(length, width, depth, concrete, day, month, year, time, AMPM, price):
    global orderdetails
    global customerdetails
    # from database_manage import customer_insert
    volume = (length * width * depth) / 1000000
    orderdetails = [length, width, depth, concrete,day, month, year, time, AMPM, price]

    messagetext = ((volume), " Cubic meters of ", concrete, " to be delivered on ", (day), "/",
                   (month), "/", (year), " at", (time), (AMPM))

    result = messagebox.askquestion('Confirm', messagetext)
    if result == 'yes':
        database_manage.customer_insert(orderdetails,customerdetails)
        homepage()

    else:
        order_details(customerdetails)


def returning_customerwindow():
    global customerdetails
    oldcustomer = Tk()
    oldcustomer.title("Returning customer")
    oldcustomer.geometry("300x325")
    oldcustomer.config(bg="#728c8d")

    titleFrame = Frame(oldcustomer, bg="#728c8d", width="300", height="50")
    titleFrame.grid(column=0, row=0)
    detailsFrame = Frame(oldcustomer, bg="#728c8d", width="300", height="200")
    detailsFrame.grid(column=0, row=1)
    buttonFrame = Frame(oldcustomer, bg="#728c8d", width="300", height="75")
    buttonFrame.grid(column=0, row=2)

    welcomelabel = Label(titleFrame, text="Customer Details")
    welcomelabel.config(font=("arial", 20))
    welcomelabel.config(bg="#728c8d", justify='center')
    welcomelabel.grid(row=0, column=0, columnspan=1, sticky="W", pady=30, padx=30)



    Id_label = Label(detailsFrame, text="Customer ID:")
    Id_label.config(font=("arial", 9), bg="#728c8d")
    Id_label.grid(row=0, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    Id_input = StringVar()
    Idinput = Entry(detailsFrame, width=15, bg="#aaaaaa", textvariable=Id_input)
    Idinput.grid(row=0, column=1, padx=10, pady=10)

    # -----------------------------

    postcode_label = Label(detailsFrame, text="Postcode:")
    postcode_label.config(font=("arial", 9), bg="#728c8d")
    postcode_label.grid(row=1, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    postcode_input = StringVar()
    postcodeinput = Entry(detailsFrame, width=15, bg="#aaaaaa", textvariable=postcode_input)
    postcodeinput.grid(row=1, column=1, padx=10, pady=10)
    # -------------------------------

    sname_label = Label(detailsFrame, text="Surname Name:")
    sname_label.config(font=("arial", 9), bg="#728c8d")
    sname_label.grid(row=2, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    surname_input = StringVar()
    surnameinput = Entry(detailsFrame, width=15, bg="#aaaaaa", textvariable=surname_input)
    surnameinput.grid(row=2, column=1, padx=10, pady=10)



    order_button = Button(buttonFrame, text="Create Order", width=12, height=3, bg="#C6CFFF",
                          command=lambda: windowswap(oldcustomer.destroy(), order_details([Id_input.get(),
                                                                                           postcode_input.get(),
                                                                                           surname_input.get()])))
    order_button.grid(row=0, column=0, padx=25, pady=10)

    return_button = Button(buttonFrame, text="Return Home", width=12, height=3, bg="#C6CFFF",
                           command=lambda: windowswap(oldcustomer.destroy(), homepage()))
    return_button.grid(row=0, column=1, padx=25, pady=10)



    oldcustomer.mainloop()









def new_customerwindow():
    # create a new window
    newcustomer = Tk()
    # set window properties
    newcustomer.title("New customer")
    newcustomer.geometry("350x450")
    newcustomer.config(bg="#728c8d")

    # create frames to organize widgets in the window
    titleFrame = Frame(newcustomer, bg="#728c8d", width="350", height="50")
    titleFrame.grid(column=0, row=0)
    detailsFrame = Frame(newcustomer, bg="#728c8d", width="350", height="300")
    detailsFrame.grid(column=0, row=1)
    buttonFrame = Frame(newcustomer, bg="#728c8d", width="350", height="100")
    buttonFrame.grid(column=0, row=2)

    # create a label for the title frame
    welcomelabel = Label(titleFrame, text="Customer Details")
    welcomelabel.config(font=("arial", 20))
    welcomelabel.config(bg="#728c8d", justify='center')
    welcomelabel.grid(row=0, column=0, columnspan=1, sticky="E", pady=30, padx=60)

    # create labels and entry widgets for customer details
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

        # Get the user input for first name, surname, and address
        fname = firstName_input.get()
        sname = surname_input.get()
        address = address_input.get()

        # Validate the user input for postcode using the postcodeIsValid function
        if validation.postcodeIsValid(postcode_input.get()) == True:
            postcode = postcode_input.get()

            # Validate the user input for phone number using the len_validation function
            if validation.len_validation(phone_input.get(), 11, 1) == True:
                phonenumber = phone_input.get()

                # Validate the user input for email using the isvalidEmail function
                if validation.isvalidEmail(email_input.get()) == True:
                    email = email_input.get()

                    # Store the customer details in a list
                    customerdetails = [fname, sname, address, postcode, phonenumber, email]

                    # Call the order_details function with customerdetails as an argument
                    windowswap(newcustomer.destroy(), order_details(customerdetails))
                else:
                    # Display a message box if the email input is invalid
                    messagebox.showinfo("info", "Email address was invalid")

            else:
                # Display a message box if the phone number input is invalid
                messagebox.showinfo("info", "Phone number was invalid")
                if validation.isvalidEmail(email_input.get()) != True:
                    messagebox.showinfo("info", "Email address was invalid")

        else:
            # Display a message box if the postcode input is invalid
            messagebox.showinfo("info", "Postcode was invalid / out of range")
            if validation.len_validation(phone_input.get(), 11, 1) != True:
                messagebox.showinfo("info", "Phone number was invalid")
            elif validation.isvalidEmail(email_input.get()) != True:
                    messagebox.showinfo("info", "Email address was invalid")




    # Create a button widget for creating orders
    order_button = Button(buttonFrame, text="Create Order", width=12, height=3, bg="#C6CFFF",
                          command=lambda: customerlist())
    order_button.grid(row=0, column=0, padx=25, pady=10)

    # Create a button widget for returning to the homepage
    return_button = Button(buttonFrame, text="Return Home", width=12, height=3, bg="#C6CFFF",
                           command=lambda: windowswap(newcustomer.destroy(), homepage()))
    return_button.grid(row=0, column=1, padx=25, pady=10)



    newcustomer.mainloop()











# accounts section

# def account_add():
#
#     accounts = Tk()
#     accounts.title("Create account")
#     accounts.geometry("200x150")
#     accounts.config(bg="#728c8d")
#
#     textFrame = Frame(accounts, bg="#728c8d", width="200", height="90")
#     textFrame.grid(column=0, row=0)
#     buttonFrame = Frame(accounts, bg="#728c8d", width="200", height="60")
#     buttonFrame.grid(column=0, row=1)
#
#     User_input = StringVar()
#     Userinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=User_input)
#     Userinput.grid(row=0, column=1, padx=10, pady=10)
#
#     Pass_input = StringVar()
#     Passinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=Pass_input)
#     Passinput.grid(row=1, column=1, padx=10, pady=10)
#
#     username_label = Label(textFrame, text="Username:")
#     username_label.config(font=("arial", 9), bg="#728c8d")
#     username_label.grid(row=0, column=0, columnspan=1, sticky="NE", pady=10, padx=10)
#
#     password_label = Label(textFrame, text="Password:")
#     password_label.config(font=("arial", 9), bg="#728c8d")
#     password_label.grid(row=1, column=0, columnspan=1, sticky="NE", pady=10, padx=10)
#
#     create_button = Button(buttonFrame, text="Create account", width=12, height=3, bg="#C6CFFF",
#                         command= lambda: insertdata(Userinput.get(), Passinput.get()))
#     create_button.grid(row=1, column=2, padx=25, pady=10)
#
#     accounts_add.mainloop()

# def updatepass_user(username, newpass):
#     conn = sqlite3.connect('Mincrete.db')
#     cursor = conn.cursor()
#     cursor.execute("UPDATE Login_details Set Password = ? WHERE Username = ?", newpass, username)
#     conn.commit()
#     messagebox.showinfo("info", "password change was successful")
#     conn.close()
#
#
# def pass_editor(username, password1):
#     pass_edit = Tk()
#     pass_edit.title("Editor")
#     pass_edit.geometry("300x150")
#     pass_edit.config(bg="#728c8d")
#
#     textFrame = Frame(pass_edit, bg="#728c8d", width="200", height="90")
#     textFrame.grid(column=0, row=0)
#     buttonFrame = Frame(pass_edit, bg="#728c8d", width="200", height="60")
#     buttonFrame.grid(column=0, row=1)
#
#     newPass_input = StringVar()
#     newPassinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=newPass_input)
#     newPassinput.grid(row=1, column=1, padx=10, pady=10)
#
#     password_label = Label(textFrame, text="New Password:")
#     password_label.config(font=("arial", 9), bg="#728c8d")
#     password_label.grid(row=1, column=0, columnspan=1, sticky="NE", pady=10, padx=10)
#
#     conn = sqlite3.connect('Mincrete.db')
#     cursor = conn.cursor()
#
#     edit_pass_button = Button(buttonFrame, text="Edit Password", width=12, height=3, bg="#C6CFFF",
#                               command=lambda: updatepass_user(username,newPass_input))
#     edit_pass_button.grid(row=1, column=1, padx=25, pady=10)
#
#
#
#
# def account_edit():
#     accounts_edit = Tk()
#     accounts_edit.title("Edit")
#     accounts_edit.geometry("300x150")
#     accounts_edit.config(bg="#728c8d")
#
#     textFrame = Frame(accounts_edit, bg="#728c8d", width="200", height="90")
#     textFrame.grid(column=0, row=0)
#     buttonFrame = Frame(accounts_edit, bg="#728c8d", width="200", height="60")
#     buttonFrame.grid(column=0, row=1)
#
#     User_input = StringVar()
#     Userinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=User_input)
#     Userinput.grid(row=0, column=1, padx=10, pady=10)
#
#     Pass_input = StringVar()
#     Passinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=Pass_input)
#     Passinput.grid(row=1, column=1, padx=10, pady=10)
#
#     username_label = Label(textFrame, text="Username:")
#     username_label.config(font=("arial", 9), bg="#728c8d")
#     username_label.grid(row=0, column=0, columnspan=1, sticky="NE", pady=10, padx=10)
#
#     password_label = Label(textFrame, text="Password:")
#     password_label.config(font=("arial", 9), bg="#728c8d")
#     password_label.grid(row=1, column=0, columnspan=1, sticky="NE", pady=10, padx=10)
#
#     editpass_button = Button(buttonFrame, text="Edit password", width=12, height=3, bg="#C6CFFF",
#                            command=lambda: (pass_editor(Userinput.get(), Passinput.get())))
#     editpass_button.grid(row=1, column=2, padx=25, pady=10)
#
#     edit_user_button = Button(buttonFrame, text="Edit username", width=12, height=3, bg="#C6CFFF",
#                          command=lambda: (editor(Userinput.get(), Passinput.get())))
#     edit_user_button.grid(row=1, column=1, padx=25, pady=10)
#
#     accounts_edit.mainloop()
#
#















def Remove_orderPage():
    remove_orders = Tk()
    remove_orders.title("Remove_orders")
    remove_orders.geometry("450x250")

    remove_orders.config(bg="#728c8d")
######################################
    textFrame = Frame(remove_orders, bg="#728c8d", width="450", height="100")
    textFrame.grid(column=0, row=0)

    dateframe = Frame(remove_orders, bg="#728c8d", width="450", height="100")
    dateframe.grid(column=0, row=1)

    buttonFrame = Frame(remove_orders, bg="#728c8d", width="450", height="50")
    buttonFrame.grid(column=0, row=2)
#####################################


    remove_orders_label = Label(textFrame, text="Welcome to the order removal page")
    remove_orders_label.config(font=("arial", 12))
    remove_orders_label.config(bg="#728c8d")
    remove_orders_label.grid(row=0, column=0, columnspan=1, sticky="NSEW", pady=10, padx=10)




    Id_label = Label(dateframe, text="Customer ID:")
    Id_label.config(font=("arial", 9), bg="#728c8d")
    Id_label.grid(row=0, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    Id_input = StringVar()
    Idinput = Entry(dateframe, width=15, bg="#aaaaaa", textvariable=Id_input)
    Idinput.grid(row=0, column=1, padx=10, pady=10)


    date_label = Label(dateframe, text="Date:")
    date_label.config(font=("arial", 9), bg="#728c8d")
    date_label.grid(row=1, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    days = ["01", "02", "03", "04", "05", "06", "7", "8", "9", "10",
            "11", "12", "13", "14", "15", "16", "17", "18",
            "19", "20", "21", "22", "23", "24", "25", "26",
            "27", "28", "29", "30", "31"]

    day_input = IntVar()
    day_input.set("DD")
    dayinput = OptionMenu(dateframe, day_input, *days)
    dayinput.config(bg="#aaaaaa")
    dayinput.grid(row=1, column=1, padx=5, pady=10)

    month = ["01", "02", "03", "04", "05", "06", "7", "8", "9", "10",
             "11", "12"]

    month_input = IntVar()
    month_input.set("MM")
    monthinput = OptionMenu(dateframe, month_input, *month)
    monthinput.config(bg="#aaaaaa")
    monthinput.grid(row=1, column=2, padx=5, pady=10)

    year = ["2023", "2024", "2025"]

    year_input = IntVar()
    year_input.set("YYYY")
    yearinput = OptionMenu(dateframe, year_input, *year)
    yearinput.config(bg="#aaaaaa")
    yearinput.grid(row=1, column=3, padx=20, pady=10)

    exit_button = Button(buttonFrame, text="Exit", width=12, height=3, bg="#C6CFFF",
                                command=lambda: windowswap(remove_orders.destroy(), homepage()))
    exit_button.grid(row=0, column=0, padx=10, pady=10)

    delete_button = Button(buttonFrame, text="Delete Order", width=12, height=3, bg="#C6CFFF",
                         command=lambda: database_manage.DeleteRecord(Id_input.get(),day_input.get(), month_input.get(), year_input.get()))
    delete_button.grid(row=0, column=1, padx=10, pady=10)

    remove_orders.mainloop()





global olddetails

def neworderdetails(olddets):
    olddetails = olddets



    orderedit = Tk()
    orderedit.title("Edited Order")
    orderedit.geometry("350x525")
    orderedit.config(bg="#728c8d")

    titleFrame = Frame(orderedit, bg="#728c8d", width="350", height="50")
    titleFrame.grid(column=0, row=0)
    detailsFrame = Frame(orderedit, bg="#728c8d", width="350", height="350")
    detailsFrame.grid(column=0, row=1)
    dateframe = Frame(orderedit, bg="#728c8d", width="350", height="50")
    dateframe.grid(column=0, row=2)
    buttonFrame = Frame(orderedit, bg="#728c8d", width="350", height="100")
    buttonFrame.grid(column=0, row=3)

    welcomelabel = Label(titleFrame, text="Edit Order:")
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

    options = ["Gen1",
               "Gen3",
               "C20",
               "C25",
               "C30",
               "C35",
               "C40"]

    Con_type_input = StringVar()
    Con_type_input.set("CEM1 S2 ")
    Con_typeinput = OptionMenu(detailsFrame, Con_type_input, *options)
    Con_typeinput.config(bg="#aaaaaa")
    Con_typeinput.grid(row=3, column=1, padx=10, pady=10)

    # -------------------------------

    date_label = Label(dateframe, text="Date:")
    date_label.config(font=("arial", 9), bg="#728c8d")
    date_label.grid(row=0, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    days = ["01","02","03","04","05","06","7","8","9","10",
            "11","12","13","14","15","16","17","18",
            "19","20","21","22","23","24","25","26",
            "27","28","29","30","31"]

    day_input = IntVar()
    day_input.set("DD")
    dayinput = OptionMenu(dateframe, day_input, *days)
    dayinput.config(bg="#aaaaaa")
    dayinput.grid(row=0, column=1, padx=5, pady=10)


    month = ["01", "02", "03", "04", "05", "06", "7", "8", "9", "10",
            "11", "12"]

    month_input = IntVar()
    month_input.set("MM")
    monthinput = OptionMenu(dateframe, month_input, *month)
    monthinput.config(bg="#aaaaaa")
    monthinput.grid(row=0, column=2, padx=5, pady=10)



    year = ["2023", "2024", "2025"]

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

    def editlist(olddetails):
        global orderdetails, price  # global variables

        # Check if the time entered is valid
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
            price = 0
            # Calculate the volume of concrete needed
            volume = (length_input.get() * width_input.get() * depth_input.get()) / 1000000
            if volume > 8:
                messagebox.showinfo("Warning", "Additional mixers will be needed")
            if volume > 30:
                messagebox.showinfo("Info", "Price reduction due to mass buy")
                price = -150

            # Check if a concrete type has been entered
            if Con_type_input.get() == "CEM1 ":
                messagebox.showinfo("info", "No concrete type has been entered")
                homepage()
            else:
                # Get the new details of the order
                newAMPM = AMPM_input.get()
                newtime = time_input.get()
                newlength = length_input.get()
                newwidth = width_input.get()
                newdepth = depth_input.get()
                newconcrete = Con_type_input.get()
                newday = day_input.get()
                newmonth = month_input.get()
                newyear = year_input.get()


                volume = (newlength * newwidth * newdepth) / 1000000
                if volume < 0.25:
                    volume = 0.25
                if volume > 8:
                    n = volume // 8
                    n = n * 1050
                    volume = volume // 8
                    preprice = (concrete_price(newconcrete, volume))
                    loads = volume // 8
                    price = preprice + (loads * 25) + n
                    print(price)
                else:
                    price = (concrete_price(newconcrete, volume))




                a = strftime('%x')
                x = str(year_input.get())
                y = str(month_input.get())
                z = str(day_input.get())

                neworder=[newlength, newwidth, newdepth, newconcrete, newday, newmonth, newyear, newtime, newAMPM, price]

                if int(a[6:8]) < int(x[2:4]):
                    database_manage.EditRecord(olddetails,neworder)
                elif int(a[6:8]) == int(x[2:4]):

                    if int(a[0:2]) < int(y):
                        database_manage.EditRecord(olddetails,neworder)
                    elif int(a[0:2]) == int(y):
                        if int(a[3:5]) < int(z):
                            database_manage.EditRecord(olddetails,neworder)
                        elif int(a[3:5]) == int(z):
                            messagebox.showinfo("Info", "Same day delivery is not available")
                            homepage()
                        else:
                            messagebox.showinfo("Error", "That date is invalid")
                            homepage()
                    else:
                        messagebox.showinfo("Error", "That date is invalid")
                        homepage()
                else:
                    messagebox.showinfo("Error", "That date is invalid")
                    homepage()


    confirm_button = Button(buttonFrame, text="Confirm", width=12, height=3, bg="#C6CFFF",
                          command=lambda: windowswap(orderedit.destroy(), editlist(olddetails)))
    confirm_button.grid(row=0, column=0, padx=25, pady=10)

    return_button = Button(buttonFrame, text="Return", width=12, height=3, bg="#C6CFFF",
                           command=lambda: windowswap(orderedit.destroy(), homepage()))
    return_button.grid(row=0, column=1, padx=25, pady=10)

    orderedit.mainloop()


def newfact(delete,newfact):
    delete
    newfact
def helpPage():
    root = Tk()

    # specify size of window.
    root.geometry("450x370")

    # Create text widget and specify size.
    T = Text(root, height=15, width=53)

    # Create label
    l = Label(root, text="Help Page")
    l.config(font=("Courier", 14))

    Fact = """For this system there are 2 ways to create orders,   one being as a new customer, this option is located  on the bottom left of the homescreen, here you can   create a new account however you have to enter all ofthe customer details for this. on the otherhand thereis a returning customer option which is located on   the bottom right of the homepage, here you only have to enter certain customer details as the customers   details are already stored.                     1/2"""
    fact2 = """There is a calculator on the homescreen in the       taskbar to calculate the voume of the concrete. you  can also view edit or delete your orders through the task bar in the order section. To Edit or remove     orders you will need your customer ID so keep hold ofit once you create an account                     2/2"""
    # Create button for next text.
    b1 = Button(root, text="Next", command = lambda: newfact(T.delete('1.0', END), T.insert(END,fact2)))

    b2 = Button(root, text="Previous", command=lambda: newfact(T.delete('1.0', END), T.insert(END, Fact)))

    # Create an Exit button.
    b3 = Button(root, text="Exit",
                command=root.destroy)

    l.pack()
    T.pack()
    b1.pack()
    b2.pack()
    b3.pack()

    # Insert The Fact.
    T.insert(END,Fact)

    root.mainloop()




def editorder():

    edit_order = Tk()
    edit_order.title("Edit Orders")
    edit_order.geometry("450x300")

    edit_order.config(bg="#728c8d")

    textFrame = Frame(edit_order, bg="#728c8d", width="450", height="100")
    textFrame.grid(column=0, row=0)

    dateframe = Frame(edit_order, bg="#728c8d", width="450", height="350")
    dateframe.grid(column=0, row=1)



    buttonFrame = Frame(edit_order, bg="#728c8d", width="450", height="50")
    buttonFrame.grid(column=0, row=3)


    remove_orders_label = Label(textFrame, text="Welcome to the order editing page")
    remove_orders_label.config(font=("arial", 12))
    remove_orders_label.config(bg="#728c8d")
    remove_orders_label.grid(row=0, column=0, columnspan=1, sticky="NSEW", pady=10, padx=10)

    Id_label = Label(dateframe, text="Customer ID:")
    Id_label.config(font=("arial", 9), bg="#728c8d")
    Id_label.grid(row=0, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    Id_input = StringVar()
    Idinput = Entry(dateframe, width=15, bg="#aaaaaa", textvariable=Id_input)
    Idinput.grid(row=0, column=1, padx=10, pady=10)

    date_label = Label(dateframe, text="Date:")
    date_label.config(font=("arial", 9), bg="#728c8d")
    date_label.grid(row=1, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    days = ["01", "02", "03", "04", "05", "06", "7", "8", "9", "10",
            "11", "12", "13", "14", "15", "16", "17", "18",
            "19", "20", "21", "22", "23", "24", "25", "26",
            "27", "28", "29", "30", "31"]

    day_input = IntVar()
    day_input.set("DD")
    dayinput = OptionMenu(dateframe, day_input, *days)
    dayinput.config(bg="#aaaaaa")
    dayinput.grid(row=1, column=1, padx=5, pady=10)

    month = ["01", "02", "03", "04", "05", "06", "7", "8", "9", "10",
             "11", "12"]

    month_input = IntVar()
    month_input.set("MM")
    monthinput = OptionMenu(dateframe, month_input, *month)
    monthinput.config(bg="#aaaaaa")
    monthinput.grid(row=1, column=2, padx=5, pady=10)

    year = ["2023", "2024", "2025"]

    year_input = IntVar()
    year_input.set("YYYY")
    yearinput = OptionMenu(dateframe, year_input, *year)
    yearinput.config(bg="#aaaaaa")
    yearinput.grid(row=1, column=3, padx=20, pady=10)



    time_label = Label(dateframe, text="Time(HH:MM):")
    time_label.config(font=("arial", 9), bg="#728c8d")
    time_label.grid(row=2, column=0, columnspan=1, sticky="N", pady=10, padx=10)

    time_input = StringVar()
    timeinput = Entry(dateframe, width=15, bg="#aaaaaa", textvariable=time_input)
    timeinput.grid(row=2, column=1, padx=10, pady=10)

    AMPM_input = StringVar()
    AMPM_input.set("AM/PM")
    AMPMinput = OptionMenu(dateframe, AMPM_input, "AM", "PM")
    AMPMinput.config(bg="#aaaaaa")
    AMPMinput.grid(row=2, column=2, padx=10, pady=10)






    exit_button = Button(buttonFrame, text="Exit", width=12, height=3, bg="#C6CFFF",
                         command=lambda: windowswap(edit_order.destroy(), homepage()))
    exit_button.grid(row=0, column=0, padx=10, pady=10)

    edit_button = Button(buttonFrame, text="Edit Order", width=12, height=3, bg="#C6CFFF",
                           command=lambda: windowswap(edit_order.destroy(),neworderdetails([Id_input.get(),day_input.get(),
                                                                                           month_input.get(),year_input.get(),
                                                                                           time_input.get(),AMPM_input.get()])))

    edit_button.grid(row=0, column=1, padx=10, pady=10)

    edit_button.mainloop()









# def accountsPage():
#
#
#
#     accounts = Tk()
#     accounts.title("Accounts")
#     accounts.geometry("450x200")
#
#     accounts.config(bg="#728c8d")
#
#     account_menu = Menu(accounts)
#     accounts.config(menu=account_menu)
#
#
#     home_menu = Menu(account_menu)
#     accounts_menu = Menu(account_menu)
#     orders_menu = Menu(account_menu)
#     calculator_menu = Menu(account_menu)
#     help_menu = Menu(account_menu)
#
#     account_menu.add_cascade(label="Home", menu=home_menu)
#     account_menu.add_cascade(label="Accounts", menu=accounts_menu)
#     account_menu.add_cascade(label="Orders", menu=orders_menu)
#     account_menu.add_cascade(label="Calculator", menu=calculator_menu)
#     account_menu.add_cascade(label="Help", menu=help_menu)
#
#     textFrame = Frame(accounts, bg="#728c8d", width="450", height="100")
#     textFrame.grid(column=0, row=0)
#
#     buttonFrame = Frame(accounts, bg="#728c8d", width="450", height="100")
#     buttonFrame.grid(column=0, row=1)
#
#     home_menu.add_command(label="Home", command=lambda: windowswap(accounts.destroy(), homepage()))
#     home_menu.add_command(label="Exit", command=lambda: accounts.destroy())
#
#     accounts_menu.add_command(label="Accounts", command=lambda: windowswap(accounts.destroy(), accountsPage()))
#
#     orders_menu.add_command(label="Remove order", command=lambda: windowswap(accounts.destroy(), Remove_orderPage()))
#     orders_menu.add_command(label="Edit order", command=lambda: windowswap(accounts.destroy(), editorder()))
#     orders_menu.add_command(label="View orders", command=lambda: windowswap(accounts.destroy(), accountsPage()))
#
#     help_menu.add_command(label="Help", command=lambda: helpPage())
#
#     edit_button = Button(buttonFrame, text="Edit account", width=12, height=3, bg="#C6CFFF",
#                            command=lambda: account_edit())
#     edit_button.grid(row=1, column=0, padx=25, pady=10)
#     # ===================================================================================
#     remove_button = Button(buttonFrame, text="Remove account", width=12, height=3, bg="#C6CFFF",
#                          command=lambda: account_delete())
#     remove_button.grid(row=1, column=1, padx=25, pady=10)
#     # ================================================================================
#     add_button = Button(buttonFrame, text="Create account", width=12, height=3, bg="#C6CFFF",
#                          command=lambda: account_add())
#     add_button.grid(row=1, column=2, padx=25, pady=10)
#
#     accountMenu_label = Label(textFrame, text="Welcome to the accounts page")
#     accountMenu_label.config(font=("arial", 12))
#     accountMenu_label.config(bg="#728c8d")
#     accountMenu_label.grid(row=0, column=0, columnspan=1, sticky="NSEW", pady=10, padx=10)
#
#
#
#
#
#
#
#
#     accounts.mainloop()



# main hompage
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
                                command=lambda: windowswap(home.destroy(), returning_customerwindow()))
    oldcustomer_button.grid(row=1, column=1, padx=10, pady=10)
    # --------------------------------------

    welcomelabel = Label(titleFrame, text="Welcome to Mincrete")
    welcomelabel.config(font=("arial", 20))
    welcomelabel.config(bg="#728c8d", justify='center')
    welcomelabel.grid(row=0, column=1, columnspan=1, sticky="N", pady=30, padx=30)

    # Create menus for the main window
    home_menu = Menu(my_menu)
    orders_menu = Menu(my_menu)
    calculator_menu = Menu(my_menu)
    help_menu = Menu(my_menu)

    # Add cascading menus to the main menu
    my_menu.add_cascade(label="Home", menu=home_menu)
    my_menu.add_cascade(label="Orders", menu=orders_menu)
    my_menu.add_cascade(label="Calculator", menu=calculator_menu)
    my_menu.add_cascade(label="Help", menu=help_menu)

    # Add commands to the home menu
    home_menu.add_command(label="Home", command=lambda: windowswap(home.destroy(), homepage()))
    home_menu.add_command(label="Exit", command=lambda: home.destroy())

    # Add commands to the orders menu
    orders_menu.add_command(label="Remove order", command=lambda: windowswap(home.destroy(), Remove_orderPage()))
    orders_menu.add_command(label="Edit order", command=lambda: windowswap(home.destroy(), editorder()))
    orders_menu.add_command(label="View orders", command=lambda: orderview.order_table_view())

    # Add commands to the calculator menu
    calculator_menu.add_command(label="calculator", command=lambda: calculatorpage.concrete_calculator())

    # Add commands to the help menu
    help_menu.add_command(label="Help", command=lambda: helpPage())

    lbl = Label(center_frame, font=("calibri", 15, "bold"),
                background="#728c8d",
                foreground="black")

    # Define a function to display the current time and date on a label
    def time():
        # Use the strftime() method to format the time and date string
        string = strftime('%H:%M:%S %p \n %x')
        # Get the current date using strftime() and save it to a variable
        a = strftime('%x')
        # Update the text of the label with the current time and date string
        lbl.config(text=string)
        # Schedule the function to run again after 1000 milliseconds (1 second)
        lbl.after(1000, time)
        # Place the label in the center frame of the home window
        lbl.grid(column=0, row=1, sticky="S")

    # Call the time() function to start displaying the time and date
    time()

    # Start the main loop of the home window
    home.mainloop()





if __name__ == '__main__':
    pass

homepage()