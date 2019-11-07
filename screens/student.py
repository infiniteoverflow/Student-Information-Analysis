from tkinter import *

class StudentData:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.title("{} Details".format("usn"))
        
        self.c = Canvas(self.root,bg = "gray",height=800,width=800,cursor='pencil')
        
        attributes = ['Name','Branch','Semester','Email','Address','Mobile']
        values = ['Aswin','CSE','5','aswingopinathan1871@gmail.com','msmdksmdksmdkmfkdmvkd\njnfknfks','9072215663']
        
        height = 5
        width = 5
        for i in range(len(attributes)): #Rows
            b = Label(self.c,text=attributes[i],bg="white",width=20,height=2,font=('Times',30,'bold'))
            b.grid(row=i, column=0)
        for i in range(len(values)): #Rows
            b = Label(self.c,text=values[i],bg="white",width=20,height=2,font=('Times',30,'bold'))
            b.grid(row=i, column=2)
                
        self.c.place(relx=0.5, rely=0.5, anchor=CENTER)
        #self.c.pack
        self.root.mainloop()
        
a = StudentData()