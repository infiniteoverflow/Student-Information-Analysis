from tkinter import *
root = Tk()
root.geometry("500x500+0+0")

startbutton = Button(root, text="Start",height=1,width=4)
startbutton.place(relx=0.5, rely=0.5, anchor=CENTER)

startbutton1 = Button(root, text="Stop",height=1,width=4)
startbutton1.place(relx=2, rely=2, anchor=NW)
#Configure the row/col of our frame and root window to be resizable and fill all available space


root.mainloop()
