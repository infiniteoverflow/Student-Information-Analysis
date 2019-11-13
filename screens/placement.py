from tkinter import *

class Placement:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Placement ")
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
     
        photo = PhotoImage(file = "images/electives12.png")
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")



        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",20,'bold'),command=lambda:back())
        self.back.place(x=1400,y=900,width=100,height=40)



        def back():
            self.root.destroy() 

        self.c.pack()
        self.root.mainloop()