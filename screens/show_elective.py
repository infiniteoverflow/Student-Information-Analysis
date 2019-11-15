from tkinter import *

class Show_elective:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Electives")
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
      
        photo = PhotoImage(file = "images/la.png")
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")
        
        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",15,'bold'),command=lambda:back())
        self.back.place(x=1300,y=900,width=200,height=30)

        def back():
            self.root.destroy() 

        
        
        self.c.pack()
        self.root.mainloop()