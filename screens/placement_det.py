from tkinter import *
import sqlite3

class PlacementDetails:
    def __init__(self,branch):
        self.branch = branch
        self.root = Tk()
        self.root.geometry("2000x1024")
        self.root.title("Placement Details for {}".format(branch))
        
        self.c = Canvas(self.root,bg = "white",height=2000,width=1024,cursor='pencil')

        
        connection = sqlite3.connect("databases/student.db")
        
        cursor = connection.cursor()
        
        sql_command = ''' SELECT COMPANY_NAME,HIGHEST_PACKAGE,TOTAL_APPEARED,TOTAL_PLACED FROM PLACEMENT WHERE BRANCH='{}';'''.format(branch)
        
        cursor.execute(sql_command)
        
        row = cursor.fetchall()
        
        print(row)
        
        companies = []
        highest_package = []
        total_appeared = []
        total_placed = []
        
        for x in row:
            companies.append(x[0])
            
        for x in row:
            highest_package.append(x[1])
        
        for x in row:
            total_appeared.append(x[2])
            
        for x in row:
            total_placed.append(x[3])
            
        print(companies)
            
        b = Label(self.c,text="Companies Visited",bg="red",fg='white',width=25,height=2,font=('palatino',30,'bold'))
        b.grid(row=0,column=0)
        
        b = Label(self.c,text="Highest Package",bg="red",fg='white',width=25,height=2,font=('palatino',30,'bold'))
        b.grid(row=0,column=1)
        
        b = Label(self.c,text="Total Appeared",bg="red",fg='white',width=25,height=2,font=('palatino',30,'bold'))
        b.grid(row=0,column=2)
        
        b = Label(self.c,text="Total Placed",bg="red",fg='white',width=25,height=2,font=('palatino',30,'bold'))
        b.grid(row=0,column=3)
            
        for i in range(1,len(companies)+1): #Rows
            b = Label(self.c,text=companies[i-1],bg="white",width=25,height=2,font=('palatino',30,'bold'))
            b.grid(row=i, column=0)
            
        for i in range(1,len(highest_package)+1): #Rows
            b = Label(self.c,text=highest_package[i-1],bg="white",width=25,height=2,font=('palatino',30,'bold'))
            b.grid(row=i, column=1)
            
        for i in range(1,len(total_appeared)+1): #Rows
            b = Label(self.c,text=total_appeared[i-1],bg="white",width=25,height=2,font=('palatino',30,'bold'))
            b.grid(row=i, column=2)
            
        for i in range(1,len(total_placed)+1): #Rows
            b = Label(self.c,text=total_placed[i-1],bg="white",width=25,height=2,font=('palatino',30,'bold'))
            b.grid(row=i, column=3)
        
        self.c.pack()
        
        