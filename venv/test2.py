from tkinter import *
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
    fact2 = """There is a calculator on the homescreen in the       taskbar to calculate the voume of the concrete. you  can also view edit or delete your orders through the task bar in the order section. you can also add edit or remove accounts in the account section of the taskbar. To Edit or remove orders you will need your     customer ID so keep hold of it once you create an    account                                          2/2"""
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

