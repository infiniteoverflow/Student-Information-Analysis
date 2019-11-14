from tkinter import *
import sqlite3

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
        
        self.c.create_text((650, 350), text="USN: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button0 = Entry(self.c,font=('Times',20,'bold'))
        self.button0.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 355, anchor=NW, window=self.button0)
        
        self.c.create_text((650, 450), text="17CS51: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button1 = Entry(self.c,font=('Times',20,'bold'))
        self.button1.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 455, anchor=NW, window=self.button1)




        self.c.create_text((650, 550), text="17CS52: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button2 = Entry(self.c,font=('Times',20,'bold'))
        self.button2.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 555, anchor=NW, window=self.button2)



        self.c.create_text((650, 650), text="17CS53: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button3 = Entry(self.c,font=('Times',20,'bold'))
        self.button3.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 655, anchor=NW, window=self.button3)



        self.c.create_text((650, 750), text="17CS54: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button4 = Entry(self.c,font=('Times',20,'bold'))
        self.button4.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 755, anchor=NW, window=self.button4)



        self.c.create_text((90, 850), text="PROFESSIONAL ELECTIVE1/ELECTIVE2: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button5 = Entry(self.c,font=('Times',20,'bold'))
        self.button5.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 855, anchor=NW, window=self.button5)



        self.c.create_text((250, 950), text="OPEN ELECTIVE1/ELECTIVE2: ", fill="black", anchor="nw"
                           ,font=('Times',30,'italic bold'))
        
        self.button6 = Entry(self.c,font=('Times',20,'bold'))
        self.button6.configure(width = 20, relief = FLAT)  
        button1_window = self.c.create_window(900, 955, anchor=NW, window=self.button6)


        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",20,'bold'),command=lambda:back())
        self.back.place(x=1400,y=900,width=100,height=40)

        self.back = Button(self.c,text='Submit',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",20,'bold'),command=lambda:submit())
        self.back.place(x=1300,y=900,width=100,height=40)


        def back():
            self.root.destroy()
            
        def submit():
            usn = self.button0.get()
            cs51 = self.button1.get()
            cs52 = self.button2.get()
            cs53 = self.button3.get()
            cs54 = self.button4.get()
            p = self.button5.get()
            o = self.button6.get()
            
            connection = sqlite3.connect('databases/student.db')
            cursor = connection.cursor()
            
            cursor.execute('''SELECT NAME,BRANCH FROM STUDENT_DETAILS WHERE USN='{}';'''.format(usn.upper()))
            
            row = cursor.fetchall()
            
            name = row[0][0]
            branch = row[0][1]
            
            cursor.close()
            
            cursor = connection.cursor()

            
            #sql_commands = [
            #    '''INSERT INTO ATTENDANCE VALUES('{}','{}','{}','{}','{}');'''.format(usn,name,branch,'17CS51',cs51),
            #    '''INSERT INTO ATTENDANCE VALUES('{}','{}','{}','{}','{}');'''.format(usn,name,branch,'17CS52',cs52),
            #    '''INSERT INTO ATTENDANCE VALUES('{}','{}','{}','{}','{}');'''.format(usn,name,branch,'17CS53',cs53),
            #    '''INSERT INTO ATTENDANCE VALUES('{}','{}','{}','{}','{}');'''.format(usn,name,branch,'17CS54',cs54),
            #    '''INSERT INTO ATTENDANCE VALUES('{}','{}','{}','{}','{}');'''.format(usn,name,branch,'PROF_1',p),
            #    '''INSERT INTO ATTENDANCE VALUES('{}','{}','{}','{}','{}');'''.format(usn,name,branch,'OPEN_1',o)
            #]
            
            sql_commands = [
                '''UPDATE ATTENDANCE SET ATT='{}' WHERE USN='{}' AND SUB_CODE='{}' '''.format(cs51,usn,'17CS51'),
                '''UPDATE ATTENDANCE SET ATT='{}' WHERE USN='{}' AND SUB_CODE='{}' '''.format(cs52,usn,'17CS52'),
                '''UPDATE ATTENDANCE SET ATT='{}' WHERE USN='{}' AND SUB_CODE='{}' '''.format(cs53,usn,'17CS53'),
                '''UPDATE ATTENDANCE SET ATT='{}' WHERE USN='{}' AND SUB_CODE='{}' '''.format(cs54,usn,'17CS54'),
                '''UPDATE ATTENDANCE SET ATT='{}' WHERE USN='{}' AND SUB_CODE='{}' '''.format(p,usn,'PROF_ELE'),
                '''UPDATE ATTENDANCE SET ATT='{}' WHERE USN='{}' AND SUB_CODE='{}' '''.format(o,usn,'OPEN_ELE'),
            ]
            
            
            for commands in sql_commands:
                cursor.execute(commands)
                
            connection.commit()
                
            self.root.destroy()

        self.c.pack()

        self.root.mainloop()
        