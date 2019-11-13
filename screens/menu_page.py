from tkinter import *
from tkinter import messagebox
from screens.stud_det import *
from screens.attendence import *
from screens.electives import *
from screens.to_login import ToLogin
from screens.marks import *
from screens.placement import *
from PIL import Image, ImageTk
#import screens.login as log


class Menu:
    def __init__(self):

        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Menu")
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
      #  image = Image.open("images/epic1.png")
      #  photo = ImageTk.PhotoImage(image)
        photo = PhotoImage(file = "images/bigg.png")

        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")

        
        # Setting the font
        self.fnt = ('latin modern typewriter',50,'bold')
        
        # Setting the text

        self.c.create_text((800, 150), text="MENU", fill="black", anchor="nw"
                           ,font=('newcenturyschlbk',50,'bold'))


        self.c.pack()
        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",15,'bold'),command=lambda:back())


        self.b1 = Button(self.c,text='Student-Details',bg='yellow',fg='blue',activebackground='black',activeforeground='white',width=20,height=5, font=("Times",20,'bold'),command=lambda:buttonClick1())
        self.b2 = Button(self.c,text='Attendance',bg='yellow',fg='blue',activebackground='black',activeforeground='white',width=20,height=5,font=("Times",20,'bold'),command=lambda:buttonClick2())
        self.b3 = Button(self.c,text='Marks',bg='yellow',fg='blue',activebackground='black',activeforeground='white',width=20,height=5,font=("Times",20,'bold'),command=lambda:buttonClick3())
        self.b4 = Button(self.c,text='Electives',bg='yellow',fg='blue',activebackground='black',activeforeground='white',width=20,height=5, font=("Times",20,'bold'),command=lambda:buttonClick4())

        self.b5 = Button(self.c,text='Placements-Details',bg='yellow',fg='blue',activebackground='black',activeforeground='white',width=20,height=5, font=("Times",20,'bold'),command=lambda:buttonClick5())

        
        self.back.place(x=20,y=20,width=200,height=30)
        self.b1.place(x=800,y=300,width=300,height=50)
        self.b2.place(x=800,y=380,width=300,height=50)
        self.b3.place(x=800,y=460,width=300,height=50)
        self.b4.place(x=800,y=540,width=300,height=50)
        self.b5.place(x=800,y=620,width=300,height=50)
        
        def back():
            self.root.destroy()
         #   b = log.Login()
    

        def buttonClick1():
            stud=StudentDetails()

        def buttonClick2():
            att = Attendence()

        def buttonClick3():
            #self.root.destroy()
            marks = Marks()

        def buttonClick4():
            #self.root.destroy()
            ele = Electives()

        def buttonClick5():
            #self.root.destroy()
            plac = Placement()       

        self.root.mainloop()
        
#a = Menu()
