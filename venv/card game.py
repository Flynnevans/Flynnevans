from tkinter import *
import tkinter.font as font


def usingFrame():

    win = Tk()
    win.geometry("450x300")
    win.title("Tkinter Frame")
    win.configure(bg="DarkOliveGreen1")  # background colour

    win.resizable(width=False, height=False)  # fix the size of the window

    # setting font for labels: You may set more than one fonts
    myFont1 = font.Font(family='Helvetica', size=16, weight='bold')
    myFont2 = font.Font(family="Arial", size=20)

    # create Frames
    f1 = Frame(win, width=430, height=100, background="DarkOliveGreen2")
    f2 = Frame(win, width=430, height=160, background="DarkOliveGreen3")

    f1.grid_propagate(False)  # to make frame's size fixed
    f2.grid_propagate(False)  # to make the frame's size fixed

    f1.grid(row=0, column=0, padx="10", pady="5")
    f2.grid(row=1, column=0, padx="10", pady="5")

    # creating a title

    title = Label(f1, text="Welocome to Demo on tkinter Frame", bg="DarkOliveGreen2")

    title.config(bg="DarkOliveGreen2", fg="Green")  # change colours

    title.grid(row=0, column=0, padx="20", pady="20", sticky="SEWN")

    title['font'] = myFont1  # applying the font on a label text

    # creating three columns in the other frame
    labelList = ["right", "middle", "Left"]  # list of text titles

    T = ["", "", ""]  # empy list to use for storing different objects (e.g. labels)

    for n in range(0, 3):
        T[n] = Label(f2, text=labelList[n])

        T[n]['font'] = myFont1  # applying fornt you may have different fonts

        T[n].grid(row=0, column=n, padx="30", pady="20", sticky="NSEW")

    # this is only for demo - labels with different fonts and colours

    moreLabels = ["first", "second", "third"]

    for i in range(0, 3):
        T[n] = Label(f2, text=moreLabels[i])
        T[n]['font'] = myFont2
        T[n].grid(row=1, column=i, padx="30", pady="10", sticky="NSEW")

    win.mainloop()

usingFrame()

