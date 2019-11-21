from tkinter import *
from screens.teach_attendance import *


class Authenticate:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Electives")
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
      
        photo = PhotoImage(file = "images/v1.png")
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")


        self.fnt = ('latin modern typewriter',50,'bold')
        
        # Setting the text
        self.c.create_text((700, 400),text="AUTHENTICATION PLEASE!", fill="white", anchor="nw"
                           ,font=('newcenturyschlbk',30,'bold'))
        self.c.create_text((600, 500), text="ENTER THE DETAILS", fill="white", anchor="nw"
                           ,font=self.fnt)
        
        # Setting the login entry boxes
        self.c.create_text((650, 610), text="Username: ", fill="white", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button1 = Entry(self.c,font=('Times',20,'bold'))
        self.button1.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 615, anchor=NW, window=self.button1)
        
        
        self.c.create_text((650, 710), text="Password: ", fill="white", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button2 = Entry(self.c,font=('Times',20,'bold'),show="*")
        self.button2.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 715, anchor=NW, window=self.button2)
        
        
        self.loginButton = Button(self.c,text="Submit",width=15,height=2,bg='red',fg='white',command=lambda:authenticate(),

                                  font=("Times",15,'bold'))
        self.loginButton.configure(width=15,relief=FLAT)
        login_button_window = self.c.create_window(800,860,anchor=NW,window=self.loginButton)
        
        
        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",15,'bold'),command=lambda:back())
        self.back.place(x=1300,y=900,width=200,height=30)

        def back():
            self.root.destroy() 

        def authenticate():
            username = self.button1.get()
            password = self.button2.get()
            
            if username.upper() == password.upper() and username.upper() == "ADMIN": 
                a = Teach_attendance()

        
        self.c.pack()
        self.root.mainloop()