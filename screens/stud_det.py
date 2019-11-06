from tkinter import *
from PIL import Image, ImageTk

class StudentDetails:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Student Details")
        


        self.c = Canvas(self.root,bg = 'pink',height=500,width=500,cursor='pencil')

        
       # image = Image.open("images/login_bg.jpg")
       # photo = ImageTk.PhotoImage(image)
        photo = PhotoImage(file = "images/epic.png")
       # w = Label(self.root, image=photo)
       # w.pack(
        self.c.create_image((0,0), image=photo, anchor="nw")

       
        

        # Setting the background
        self.c.create_text((130, 150), text="Enter the USN: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button1 = Entry(self.c,font=('Times',20,'bold'))
        self.button1.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(120, 250, anchor=NW, window=self.button1)

        self.b1 = Button(self.c,text='Cick here!',bg='blue',fg='white',activebackground='black',activeforeground='white',width=15,height=2, font=("Times",15,'bold'),command=lambda:onClick1())
        self.b1.place(x=180,y=300,width=150,height=50)

    

        self.c.pack()
        

        def onClick1():
            bh = click()
        self.root.mainloop()


