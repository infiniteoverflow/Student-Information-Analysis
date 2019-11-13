from tkinter import *

class Teach_marks():
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Marks")
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
      
        photo = PhotoImage(file = "images/mk.png")
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")


        
        self.c.pack()

        self.root.mainloop()