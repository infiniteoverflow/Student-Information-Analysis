from tkinter import *
import sqlite3

class StudentData:
    def __init__(self,usn):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.title("{} Details".format(usn))
        
        self.c = Canvas(self.root,bg = "gray",height=800,width=800,cursor='pencil')
        
        attributes = ['Name','Branch','Semester','Email','Address','Mobile']
        
        connection = sqlite3.connect('databases/student.db')
            
        cursor = connection.cursor()
            
        sql_command = '''SELECT * FROM STUDENT_DETAILS WHERE USN='{}';'''.format(usn)
            
        cursor.execute(sql_command)
            
        row = cursor.fetchall()
            
        print(row)
        
        height = 5
        width = 5
        for i in range(len(attributes)): #Rows
            b = Label(self.c,text=attributes[i],bg="white",width=20,height=2,font=('Times',30,'bold'))
            b.grid(row=i, column=0)
        for i in range(len(row)): #Rows
            if len(str(i)) > 10:
                b = Label(self.c,text=row[0][i],bg="white",width=20,height=2,font=('Times',20,'bold'))
            else:
                b = Label(self.c,text=row[0][i],bg="white",width=20,height=2,font=('Times',30,'bold'))
            b.grid(row=i, column=2)
                
        self.c.place(relx=0.5, rely=0.5, anchor=CENTER)

        
        #self.c.pack()
        self.root.mainloop()
        
        def disp_details(self):
            pass
        
