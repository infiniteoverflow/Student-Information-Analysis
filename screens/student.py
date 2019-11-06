from tkinter import *

class StudentData:
    def __init__(self,usn):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.title("{} Details".format(usn))
        
        self.c = Canvas(self.root,bg = "gray",height=800,width=800,cursor='pencil')
        
        self.c.pack()
        self.root.mainloop()