from tkinter import *

class Electives:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Electives")
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
      
        photo = PhotoImage(file = "images/la.png")
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")


        self.c.create_text((500, 300), text="CHOOSE YOUR BRANCH: ", fill="black", anchor="nw"
                           ,font=('Times',50,'italic bold'))
       # self.f=Frame(self.root,height=300,width=300,bg="yellow",cursor="cross")
        

        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",15,'bold'),command=lambda:back())
        self.back.place(x=1000,y=900,width=200,height=30)


        self.b1 = Button(self.c,text='CSE',bg='light blue',fg='blue',activebackground='black',activeforeground='white',width=20,height=5, font=("Times",30,'bold'),command=lambda:buttonClick1())
        self.b1.place(x=800,y=550,width=300,height=80)
        self.b1 = Button(self.c,text='ISE',bg='light blue',fg='blue',activebackground='black',activeforeground='white',width=20,height=5, font=("Times",30,'bold'),command=lambda:buttonClick2())
        self.b1.place(x=800,y=700,width=300,height=80)

        def back():
            self.root.destroy() 

        def buttonClick1():
            f=Frame(self.root,height=300,width=300,bg="grey",cursor="cross")
          #  f.place(x=800,y=550)
           # c = Canvas(self.root,bg = "gray",height=300,width=300)
            b1=Button(f,text='submit',bg='blue',fg='white',activebackground='black',width=20,height=5,font=("Times",15,'bold'),command=lambda:submit())
            b1.place(x=100,y=200,width=80,height=30)
            f.place(x=800,y=550)
            #c.place(x=800,y=550)
       # self.f.place(x=1000,y=600)


        def buttonClick2():
            f=Frame(self.root,height=300,width=300,bg="grey",cursor="cross")
          #  f.place(x=800,y=550)
           # c = Canvas(self.root,bg = "gray",height=300,width=300)
            b1=Button(f,text='submit',bg='blue',fg='white',activebackground='black',width=20,height=5,font=("Times",15,'bold'),command=lambda:submit())
            b1.place(x=100,y=200,width=80,height=30)
            f.place(x=800,y=550)
            #c.place(x=800,y=550)
       # self.f.place(x=1000,y=600)
        




        def submit():
            f.place_forget()
            f.destroy()
        self.c.pack()
        self.root.mainloop()