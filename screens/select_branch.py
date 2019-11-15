from tkinter import *
from screens.show_elective import *

class Select_branch:
    def __init__(self,branch):
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Electives")
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
      
        photo = PhotoImage(file = "images/la.png")
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")

        if branch == "cse":
            e1 = "ARTIFICIAL INTELLIGENCE"
            e2 = "CLOUD COMPUTING"
            e3 = "ADVANCED ALGORITHMS"
            e4 = "ADVANCED JAVA AND J2EE"
        else:
            e1 = "DOT NET"
            e2 = "EMBEDDED SYSTEMS"
            e3 = "SOCIAL NETWORK ANALYSIS"
            e4 = "PROGRAMMING LANGUAGES"


        self.b1 = Button(self.c,text=e1,bg='light blue',fg='blue',activebackground='black',activeforeground='white',width=20,height=5, font=("Times",15,'bold'),command=lambda:buttonClick())
        self.b1.place(x=800,y=400,width=300,height=80)
        self.b1 = Button(self.c,text=e2,bg='light blue',fg='blue',activebackground='black',activeforeground='white',width=20,height=5, font=("Times",15,'bold'),command=lambda:buttonClick())
        self.b1.place(x=800,y=550,width=300,height=80)

        self.b1 = Button(self.c,text=e3,bg='light blue',fg='blue',activebackground='black',activeforeground='white',width=20,height=5, font=("Times",15,'bold'),command=lambda:buttonClick())
        self.b1.place(x=800,y=700,width=300,height=80)
        self.b1 = Button(self.c,text=e4,bg='light blue',fg='blue',activebackground='black',activeforeground='white',width=20,height=5, font=("Times",15,'bold'),command=lambda:buttonClick())
        self.b1.place(x=800,y=850,width=300,height=80)









        self.c.create_text((500, 300), text="CHOOSE YOUR ELECTIVE: ", fill="black", anchor="nw"
                           ,font=('Times',50,'italic bold'))
       # self.f=Frame(self.root,height=300,width=300,bg="yellow",cursor="cross")
        

        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",15,'bold'),command=lambda:back())
        self.back.place(x=1300,y=900,width=200,height=30)

        def back():
            self.root.destroy() 

        def buttonClick():
            cc = Show_elective()
        
        self.c.pack()
        self.root.mainloop()