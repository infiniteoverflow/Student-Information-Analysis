from tkinter import *

class StudentData:
    def __init__(self,usn):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.title("{} Details".format(usn))
        self.root.mainloop()