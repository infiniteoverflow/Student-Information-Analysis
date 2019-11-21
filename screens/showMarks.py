from tkinter import *

class ShowMarks:
    def __init__(self):
        self.usn = usn.upper()
        self.root = Tk()
        self.root.geometry("2000x1024")
        self.root.title("{} Marks".format(self.usn))

        
        self.root.mainloop()