from tkinter import *
import sqlite3
from tkinter import messagebox


def cubic_calculations(length,width,depth):
    print(length)
    print(width)
    print(depth)
    volume = (length) * (width) * (depth) / 1000000
    message = (volume,"M cube")
    messagebox.showinfo("Output", message)




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



    widthlabel = Label(textFrame, text="Width(CM):")
    widthlabel.config(font=("arial", 9), bg="#728c8d")
    widthlabel.grid(row=1, column=0, columnspan=1, sticky="E", pady=10, padx=10)

    width_input = IntVar()
    widthinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=width_input)
    widthinput.grid(row=1, column=1, padx=10, pady=10, sticky="SE")
####################################################################################
    lengthlabel = Label(textFrame, text="Length(CM):")
    lengthlabel.config(font=("arial", 9), bg="#728c8d")
    lengthlabel.grid(row=2, column=0, columnspan=1, sticky="E", pady=10, padx=10)

    length_input = IntVar()
    lengthinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=length_input)
    lengthinput.grid(row=2, column=1, padx=10, pady=10, sticky="SE")
######################################################################################

    depthlabel = Label(textFrame, text="Depth(CM):")
    depthlabel.config(font=("arial", 9), bg="#728c8d")
    depthlabel.grid(row=3, column=0, columnspan=1, sticky="E", pady=10, padx=10)

    depth_input = IntVar()
    depthinput = Entry(textFrame, width=15, bg="#aaaaaa", textvariable=depth_input)
    depthinput.grid(row=3, column=1, padx=10, pady=10, sticky="SE")
###############################################################################################



    calculate_button = Button(buttonFrame, text="Calculate", width=12, height=3, bg="#C6CFFF",
                           command=lambda: cubic_calculations(length_input.get(),width_input.get(),depth_input.get()))
    calculate_button.grid(row=1, column=1, padx=25, pady=10)

    home_button = Button(buttonFrame, text="Return", width=12, height=3, bg="#C6CFFF",
                         command=lambda: windowswap(calculator.destroy(),homepage()))
    home_button.grid(row=1, column=0, padx=25, pady=10)


    accountMenu_label = Label(textFrame, text="Concrete Calculator")
    accountMenu_label.config(font=("arial", 12))
    accountMenu_label.config(bg="#728c8d")
    accountMenu_label.grid(row=0, column=0, columnspan=2, sticky="NSEW", pady=10, padx=10)


    calculator.mainloop()

if __name__ == '__main__':
    pass