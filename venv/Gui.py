from tkinter import *
def mainpage_GUI():
    page = Tk()
    page.title ("Main Page")
    page.geometry ("800x600")
    page.config(bg="#728c8d")

    welcomelabel = Label(page, text="Welcome to Main")
    welcomelabel.config(font=("arial", 12))
    welcomelabel.config(bg= "#728c8d")
    welcomelabel.grid(row = 0, column = 1, columnspan= 1, sticky = "NSEW", pady =10, padx= 10)

    exit_lable = Button(page, text="Exit", width = 8,height= 2 ,command = quit, bg= "#C6CFFF")
    exit_lable.grid(row=3, column =0 , padx=10 , pady=10, sticky = "S")
    page.mainloop()



    #login_lable = Button(page, text="Login", width=8,height= 2 , bg= "#C6CFFF",command=login_window)
    #login_lable.grid(row=3, column=2, padx=10, pady=10, sticky="SE")


mainpage_GUI()