from tkinter import *
from tkinter import messagebox
from screens.stud_det import *
from screens.attendence import *
from screens.electives import *
from screens.login import *
from screens.marks import *
from screens.placement import *
from PIL import Image, ImageTk

class Menu:
    def __init__(self):

        self.root = Tk()
        self.root.geometry("800x800")
        self.root.title("Menu")
        self.c = Canvas(self.root,bg = "gray",height=800,width=800)
        image = Image.open("images/login_bg.jpg")
        photo = ImageTk.PhotoImage(image)

        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")

        
        # Setting the font
        self.fnt = ('latin modern typewriter',50,'bold')
        
        # Setting the text
        self.c.create_text((300, 150), text="MENU", fill="black", anchor="nw"
                           ,font=('newcenturyschlbk',50,'bold'))


        self.c.pack()

        self.b1 = Button(self.c,text='Student-Details',bg='yellow',fg='blue',activebackground='black',activeforeground='white',width=15,height=2, font=("Times",15,'bold'),command=lambda:buttonClick1())
        self.b2 = Button(self.c,text='Attendance',bg='yellow',fg='blue',activebackground='black',activeforeground='white',width=15,height=2,font=("Times",15,'bold'),command=lambda:buttonClick2())
        self.b3 = Button(self.c,text='Marks',bg='yellow',fg='blue',activebackground='black',activeforeground='white',width=15,height=2,font=("Times",15,'bold'),command=lambda:buttonClick3())
        self.b4 = Button(self.c,text='Electives',bg='yellow',fg='blue',activebackground='black',activeforeground='white',width=15,height=2, font=("Times",15,'bold'),command=lambda:buttonClick4())
        self.b5 = Button(self.c,text='Placements-Details',bg='yellow',fg='blue',activebackground='black',activeforeground='white',width=15,height=2, font=("Times",15,'bold'),command=lambda:buttonClick5())

        
        self.b1.place(x=300,y=300,width=200,height=50)
        self.b2.place(x=300,y=380,width=200,height=50)
        self.b3.place(x=300,y=460,width=200,height=50)
        self.b4.place(x=300,y=540,width=200,height=50)
        self.b5.place(x=300,y=620,width=200,height=50)

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