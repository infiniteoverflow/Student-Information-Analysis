from tkinter import *
import sqlite3

class StudentData:
    def __init__(self,usn):
        self.usn = usn.upper()
        self.root = Tk()
        self.root.geometry("2000x1024")
        self.root.title("{} Details".format(self.usn))
        
        self.c = Canvas(self.root,bg = "white",height=2000,width=2024,cursor='pencil')
        
        
        attributes = ['USN','Name','Gender','Branch','Year','Email','Address','Mobile']
        
        connection = sqlite3.connect('databases/student.db')
            
        cursor = connection.cursor()
            
        sql_command = '''SELECT * FROM STUDENT_DETAILS WHERE USN='{}';'''.format(self.usn)
            
        cursor.execute(sql_command)
            
        row = cursor.fetchall()
            
        print(row)
        
        
        height = 5
        width = 5
        for i in range(len(attributes)): #Rows
            b = Label(self.c,text=attributes[i],bg="white",width=40,height=2,font=('palatino',30,'bold'))
            b.grid(row=i, column=0)
        for i in range(len(row[0])): #Rows
            b = Label(self.c,text=row[0][i],bg="white",width=40,height=2,font=('Times',30,'bold'))
            b.grid(row=i, column=2)
                
        self.c.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        self.back = Button(self.c,text='Back',bg='red',fg='white',activebackground='black',activeforeground='white',width=10,height=2, font=("Times",15,'bold'),command=lambda:back())
        self.back.grid(row=10,column=2)
        
        def back():
            self.root.destroy()

        
        #self.c.pack()
        self.root.mainloop()
        
        def disp_details(self):
            pass
        
