from tkinter import *
from PIL import Image, ImageTk

import screens.menu_page as menu

class Login:
    def __init__(self):
        # Defining the root window
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.title("Login")
        
        # Defining the canvas on which the widgets has to be placed
        self.c = Canvas(self.root,bg = "gray",height=800,width=800,cursor='pencil')
        
        # Setting the background image
        image = Image.open("images/login_bg.jpg")
        photo = ImageTk.PhotoImage(image)
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")
        self.f = Frame(self.root,height=800,width=800)
        
        # Setting the font
        self.fnt = ('latin modern typewriter',50,'bold')
        
        # Setting the text
        self.c.create_text((100, 150), text="Student Information Analysis", fill="black", anchor="nw"
                           ,font=('newcenturyschlbk',30,'bold'))
        self.c.create_text((280, 270), text="Login", fill="black", anchor="nw"
                           ,font=self.fnt)
        
        # Setting the login entry boxes
        self.c.create_text((190, 390), text="Username: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button1 = Entry(self.c,font=('Times',20,'bold'))
        self.button1.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(380, 400, anchor=NW, window=self.button1)
        
        
        self.c.create_text((190, 480), text="Password: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button2 = Entry(self.c,font=('Times',20,'bold'),show="*")
        self.button2.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(380, 490, anchor=NW, window=self.button2)
        
        
        self.loginButton = Button(self.c,text="Login",width=15,height=2,bg='red',fg='white',command=self.credentials,
                                  font=("Times",15,'bold'))
        self.loginButton.configure(width=15,relief=FLAT)
        login_button_window = self.c.create_window(380,560,anchor=NW,window=self.loginButton)
        
        
        # Defining the window
        self.c.pack()
        self.root.mainloop()
        
    def credentials(self):
        username = self.button1.get()
        password = self.button2.get()
        
        print(username)
        print(password)
        
        self.root.destroy()
        m = menu.Menu()
        

