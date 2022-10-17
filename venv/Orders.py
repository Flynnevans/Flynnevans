


from tkinter import *
import tkinter.messagebox
root=Tk()
result=tkinter.messagebox.askquestion('Installation','Do you want to install this anyway?')
if result=='yes':
    theLabel=Label(root,text="Enjoy this software.") #To insert a text
    theLabel.pack()
else:
    root.destroy() #Closing Tkinter window forcefully.
root.mainloop()