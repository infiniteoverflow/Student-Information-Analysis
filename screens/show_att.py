from tkinter import *

import sqlite3

class ShowAttendence:
    def __init__(self,usn):
        self.usn = usn
        
        self.root = Tk()
        self.root.geometry("2000x1024")
        self.root.title("Attendence")
        
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024,cursor='pencil')
        
        
        