from tkinter import *

class Teach_attendance:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Attendence")
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024)
      
        photo = PhotoImage(file = "images/v1.png")
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")


        self.fnt = ('latin modern typewriter',50,'bold')
        
        # Setting the text
        self.c.create_text((300, 150),text="Enter the attendance for respective courses", fill="white", anchor="nw"
                           ,font=('newcenturyschlbk',40,'bold'))
        
        self.c.create_text((650, 410), text="1CS51: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button1 = Entry(self.c,font=('Times',20,'bold'))
        self.button1.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 415, anchor=NW, window=self.button1)




        self.c.create_text((650, 510), text="1CS52: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button2 = Entry(self.c,font=('Times',20,'bold'))
        self.button2.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 515, anchor=NW, window=self.button2)



        self.c.create_text((650, 610), text="1CS53: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button3 = Entry(self.c,font=('Times',20,'bold'))
        self.button3.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 615, anchor=NW, window=self.button3)



        self.c.create_text((650, 710), text="1CS54: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button4 = Entry(self.c,font=('Times',20,'bold'))
        self.button4.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 715, anchor=NW, window=self.button4)



        self.c.create_text((90, 810), text="PROFESSIONAL ELECTIVE1/ELECTIVE2: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button5 = Entry(self.c,font=('Times',20,'bold'))
        self.button5.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 815, anchor=NW, window=self.button5)



        self.c.create_text((250, 910), text="OPEN ELECTIVE1/ELECTIVE2: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button6 = Entry(self.c,font=('Times',20,'bold'))
        self.button6.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 915, anchor=NW, window=self.button6)


        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",20,'bold'),command=lambda:back())
        self.back.place(x=1400,y=900,width=100,height=40)

        self.back = Button(self.c,text='Submit',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",20,'bold'),command=lambda:back())
        self.back.place(x=1300,y=900,width=100,height=40)


        def back():
            self.root.destroy()












        self.c.pack()

        self.root.mainloop()