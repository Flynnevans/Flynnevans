from tkinter import *
import sqlite3
from tkinter import messagebox
from Mainpage import *

#def cubic_calculations():





def windowswap(close, open):
    close
    open


def concrete_calculator():
    calculator = Tk()
    calculator.title("Calculator")
    calculator.geometry("285x300")

    calculator.config(bg="#728c8d")


    textFrame = Frame(calculator, bg="#728c8d", width="250", height="250")
    textFrame.grid(column=0, row=0)

    buttonFrame = Frame(calculator, bg="#728c8d", width="250", height="50")
    buttonFrame.grid(column=0, row=1)



    widthlabel = Label(textFrame, text="Width(M):")
    widthlabel.config(font=("arial", 9), bg="#728c8d")
    widthlabel.grid(row=1, column=0, columnspan=1, sticky="E", pady=10, padx=10)

    width_input = StringVar()
    widthinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=width_input)
    widthinput.grid(row=1, column=1, padx=10, pady=10, sticky="SE")
####################################################################################
    lengthlabel = Label(textFrame, text="Length(M):")
    lengthlabel.config(font=("arial", 9), bg="#728c8d")
    lengthlabel.grid(row=2, column=0, columnspan=1, sticky="E", pady=10, padx=10)

    length_input = StringVar()
    lengthinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=length_input)
    lengthinput.grid(row=2, column=1, padx=10, pady=10, sticky="SE")
######################################################################################

    depthlabel = Label(textFrame, text="Depth(M):")
    depthlabel.config(font=("arial", 9), bg="#728c8d")
    depthlabel.grid(row=3, column=0, columnspan=1, sticky="E", pady=10, padx=10)

    depth_input = StringVar()
    depthinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=depth_input)
    depthinput.grid(row=3, column=1, padx=10, pady=10, sticky="SE")
###############################################################################################



    calculate_button = Button(buttonFrame, text="Calculate", width=12, height=3, bg="#C6CFFF",
                           command=lambda: cubic_calculations() )
    calculate_button.grid(row=1, column=1, padx=25, pady=10)

    home_button = Button(buttonFrame, text="Return", width=12, height=3, bg="#C6CFFF",
                         command=lambda: windowswap(calculator.destroy(),homepage()))
    home_button.grid(row=1, column=0, padx=25, pady=10)


    accountMenu_label = Label(textFrame, text="Concrete Calculator")
    accountMenu_label.config(font=("arial", 12))
    accountMenu_label.config(bg="#728c8d")
    accountMenu_label.grid(row=0, column=0, columnspan=2, sticky="NSEW", pady=10, padx=10)


    calculator.mainloop()

concrete_calculator()