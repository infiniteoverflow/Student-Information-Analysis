from tkinter import *
from PIL import Image, ImageTk


import screens.menu_page as menu

import sqlite3

class Login:
    def __init__(self):
        # Defining the root window
        self.root = Tk()
        self.root.geometry("2000x1024")
        self.root.title("Login")
                
        # Defining the canvas on which the widgets has to be placed
        self.c = Canvas(self.root,bg = "gray",height=2000,width=2024,cursor='pencil')
        
        # Setting the background image
        image = Image.open("images/b1.jpg")
        photo = ImageTk.PhotoImage(image)
        
        # Setting the background
        self.c.create_image((0,0), image=photo, anchor="nw")
        
        
        # Setting the font
        self.fnt = ('latin modern typewriter',50,'bold')
        
        # Setting the text
        self.c.create_text((600, 300),text="Student Information Analysis", fill="black", anchor="nw"
                           ,font=('newcenturyschlbk',30,'bold'))
        self.c.create_text((800, 400), text="Login", fill="black", anchor="nw"
                           ,font=self.fnt)
        
        # Setting the login entry boxes
        self.c.create_text((650, 610), text="Username: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button1 = Entry(self.c,font=('Times',20,'bold'))
        self.button1.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 615, anchor=NW, window=self.button1)
        
        
        self.c.create_text((650, 710), text="Password: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button2 = Entry(self.c,font=('Times',20,'bold'),show="*")
        self.button2.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 715, anchor=NW, window=self.button2)
        
        
        self.loginButton = Button(self.c,text="Login",width=15,height=2,bg='red',fg='white',command=self.credentials,
                                  font=("Times",15,'bold'))
        self.loginButton.configure(width=15,relief=FLAT)
        login_button_window = self.c.create_window(800,860,anchor=NW,window=self.loginButton)
        
        
        # Defining the window
        self.c.pack()
        self.root.mainloop()
        
    def credentials(self):
        username = self.button1.get()
        password = self.button2.get()
        
        print(username)
        print(password)
        
        username = username.upper()
        password = password.upper()

        
        
        if username==password:
            if username.startswith("1mv"):
               # self.root.destroy()
                m = menu.Menu()
            else:
                r = Tk()
                r.title('Error!')
                r.geometry('300x80')
            
                lbl = Label(r,text = 'Incorrect username or password!',font=('Times',13,'bold'))
                b1 = Button(r,text='OK',bg='white',fg='black',activebackground='black',activeforeground='white',width=5,height=2, font=("Times",8,'bold'),command=lambda:destroy())
                b1.place(x=140,y=35,width=30,height=30)
                lbl.pack()
                
                def destroy():
                    r.destroy() 
                

                r.mainloop()      
                
        connection = sqlite3.connect('databases/student.db')
        
        crsr = connection.cursor()
        
        sql_command = '''SELECT * FROM STUDENT_DETAILS WHERE USN='{}'; '''.format(username)
        
        crsr.execute(sql_command)
        
        row = crsr.fetchall()
        
        if len(row)!=0 and row[0][0] == username and username==password:
            a = menu.Menu()
        else:
            r = Tk()
            r.title('Error!')
            r.geometry('300x80')
            
            lbl = Label(r,text = 'Incorrect username or password!',font=('Times',13,'bold'))
            b1 = Button(r,text='OK',bg='white',fg='black',activebackground='black',activeforeground='white',width=5,height=2, font=("Times",8,'bold'),command=lambda:destroy())
            b1.place(x=140,y=35,width=30,height=30)
            lbl.pack()
                
            def destroy():
                r.destroy() 
                

            r.mainloop()      
    