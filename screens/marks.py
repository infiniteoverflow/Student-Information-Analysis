from tkinter import *
from PIL import Image, ImageTk

class Marks:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.title("Marks")

        self.c = Canvas(self.root,bg = "gray",height=800,width=800)
        image = Image.open("images/login_bg.jpg")
        photo = ImageTk.PhotoImage(image)

        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")



        self.root.mainloop()