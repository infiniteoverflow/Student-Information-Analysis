from tkinter import *

class Placement:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("800x800")
        self.root.title("Placement ")
        self.c = Canvas(self.root,bg = "gray",height=800,width=800)
     
        photo = PhotoImage(file = "images/epic1.png")
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")
        self.c.pack()
        self.root.mainloop()