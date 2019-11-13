from tkinter import *
#from PIL import Image, ImageTk
from screens.student import StudentData

class StudentDetails:
    def __init__(self):
        self.root = Toplevel()
        self.root.geometry("2000x1024")
        self.root.title("Student Details")
        


        self.c = Canvas(self.root,bg = 'pink',height=2000,width=2024,cursor='pencil')

        
       # image = Image.open("images/login_bg.jpg")
       # photo = ImageTk.PhotoImage(image)
        photo = PhotoImage(file = "images/bigg.png")
       
        self.c.create_image((0,0), image=photo, anchor="nw")

       
        

        # Setting the background
        self.c.create_text((800, 150), text="Enter the USN: ", fill="black", anchor="nw"
                           ,font=('Times',50,'italic bold'))
        
        self.button1 = Entry(self.c,font=('Times',20,'bold'))
        self.button1.configure(width = 40,relief = FLAT)  
        button1_window = self.c.create_window(750, 300, anchor=NW, window=self.button1)

        self.b1 = Button(self.c,text='Cick here!',bg='blue',fg='white',activebackground='black',activeforeground='white',width=15,height=2, font=("Times",15,'bold'),command=self.onClick1)
        self.b1.place(x=900,y=400,width=150,height=50)
        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",15,'bold'),command=lambda:back())
        self.back.place(x=1000,y=900,width=200,height=30)

        def back():
            self.root.destroy() 
    

        self.c.pack()
        self.root.mainloop()
        

    def onClick1(self):
        stu_data = StudentData(self.button1.get())
        


