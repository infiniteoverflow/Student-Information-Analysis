from tkinter import *
from screens.showMarks import *

class Stud_marks():
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Marks")
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
      
        photo = PhotoImage(file = "images/v1.png")
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")

        self.c.create_text((700, 400), text="Enter the USN: ", fill="white", anchor="nw"
                           ,font=('Times',50,'italic bold'))
        
        self.button1 = Entry(self.c,font=('Times',20,'bold'))
        self.button1.configure(width = 40,relief = FLAT)  
        button1_window = self.c.create_window(700, 550, anchor=NW, window=self.button1)


        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",20,'bold'),command=lambda:back())
        self.back.place(x=1400,y=900,width=100,height=40)


        self.back = Button(self.c,text='Submit',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",20,'bold'),command=lambda:submit())
        self.back.place(x=1250,y=900,width=100,height=40)


        def back():
            self.root.destroy()


        def submit():
            usn = self.button1.get()
            
            usn = usn.upper()
            
            s = ShowMarks(usn)


        self.c.pack()

        self.root.mainloop()