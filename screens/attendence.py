from tkinter import *
from screens.stud_attendance import *
from screens.teach_attendance import *
class Attendence:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Attendence")
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
      
        photo = PhotoImage(file = "images/v1.png")
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")
        # Setting the font
        self.fnt = ('latin modern typewriter',50,'bold')
        
        # Setting the text
        self.c.create_text((700, 400), text="ATTENDANCE LOGIN", fill="white", anchor="nw"
                           ,font=('newcenturyschlbk',30,'bold'))

        self.b1 = Button(self.c,text='STUDENT',bg='light blue',fg='blue',activebackground='black',activeforeground='white',width=20,height=5, font=("Times",30,'bold'),command=lambda:buttonClick1())
        self.b1.place(x=800,y=550,width=300,height=80)
        self.b1 = Button(self.c,text='TEACHER',bg='light blue',fg='blue',activebackground='black',activeforeground='white',width=20,height=5, font=("Times",30,'bold'),command=lambda:buttonClick2())
        self.b1.place(x=800,y=700,width=300,height=80)
        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",15,'bold'),command=lambda:back())
        self.back.place(x=1000,y=900,width=200,height=30)

        def back():
            self.root.destroy() 
        def buttonClick1():
            stud=Stud_attendance()
        def buttonClick2():
            teach = Teach_attendance()


        

        self.c.pack()
        self.root.mainloop()