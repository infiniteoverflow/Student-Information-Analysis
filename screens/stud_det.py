from tkinter import *
from PIL import Image, ImageTk

class StudentDetails:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Student Details")
        self.c = Canvas(self.root,bg = "gray",height=500,width=500)
        image = Image.open("./images/login_bg.jpg")
        photo = ImageTk.PhotoImage(image)

        # Setting the background
        self.c.create_text((130, 150), text="Enter the USN: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button1 = Entry(self.c,font=('Times',20,'bold'))
        self.button1.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(150, 250, anchor=NW, window=self.button1)

        self.c.create_image((0,0), image=photo, anchor="nw")

        self.c.pack()

        self.root.mainloop()

