from tkinter import *
from PIL import Image, ImageTk

class Login:
    def __init__(self):
        # Defining the root window
        self.root = Tk()
        self.root.geometry("800x800")
        
        # Defining the canvas on which the widgets has to be placed
        self.c = Canvas(self.root,bg = "gray",height=800,width=800,cursor='pencil')
        
        # Setting the background image
        image = Image.open("images/login_bg.jpg")
        photo = ImageTk.PhotoImage(image)
        
        self.c.create_image((0,0), image=photo, anchor="nw")
        self.c.create_text((100, 150), text="Student Information Analysis", fill="black", anchor="nw"
                           ,font=('newcenturyschlbk',30,'bold'))
        
        self.c.create_text((280, 270), text="Login", fill="black", anchor="nw"
                           ,font=('latin modern typewriter',50,'bold'))
        
        # Defining the window
        self.c.pack()
        self.root.mainloop()

c = Login()