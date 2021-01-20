import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import sys
import os


HEADING_FONT = ("Helvetica", 25)
LARGE_FONT = ("Verdana", 18)
NAME = None
#ROW = None

conn = sqlite3.connect('tryy1.db')
c = conn.cursor()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def create_area_table():
    c.execute('CREATE TABLE IF NOT EXISTS Area(Id INTEGER PRIMARY KEY, Name VARCHAR NOT NULL, Temperature INTEGER NOT NULL, CropID VARCHAR ) ')

def create_crop_table():
    c.execute('CREATE TABLE IF NOT EXISTS Crop(Id INTEGER PRIMARY KEY, IdCode VARCHAR NOT NULL,Rainfall INTEGER NOT NULL, Pesticide VARCHAR NOT NULL, Cost INTEGER NOT NULL) ')

def insert_area(name,temperature,cropid):
    create_area_table()
    c.execute('INSERT INTO AREA(Name, Temperature, CropID) VALUES(?,?,?)',(name, temperature, cropid))
    conn.commit()
    messagebox.showinfo(title = "Success", message = "Area was successfuly added")
    restart_program()

def insert_crop(idcode, rainfall, pesticide, cost):
    create_crop_table()
    c.execute('INSERT INTO Crop(IdCode, Rainfall, Pesticide, Cost) VALUES(?,?,?,?)',(idcode, rainfall, pesticide, cost))
    conn.commit()
    messagebox.showinfo(title = "Success", message = "crop was successfuly added")
    restart_program()


class try1(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Know crop details")

        container = tk.Frame(self)
        container.pack(side="top", fill ="both", expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        for page in (StartPage, Pageone, Pagetwo, Pagethree, Pagefour, Pagefive):#, Pagesix):
            frame = page(container, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
        
    def dynamic_page(self, page, parent, var):
        if var is not None:
            self.frames[page] = page(parent, self, var)
        
    def show_frame(self, cont):
        for frame in self.frames.values():
            frame.grid_remove()
        frame = self.frames[cont]
        frame.grid()
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="MAIN MENU", font = HEADING_FONT)
        option1 = tk.Label(self, text="Add a area", font = LARGE_FONT)
        option2 = tk.Label(self, text="Add a crop", font = LARGE_FONT)
        option3 = tk.Label(self, text="Display a particular crop", font = LARGE_FONT)
        option4 = tk.Label(self, text="Display All area", font = LARGE_FONT)
        option5 = tk.Label(self, text="Display All crop", font = LARGE_FONT)
        

        label.grid(row=0, columnspan= 3,padx = 20, pady=20)
        option1.grid(row=1,column=1,padx = 20, pady=20)
        option2.grid(row=2,column=1,padx = 20, pady=20)
        option3.grid(row=3,column=1,padx = 20, pady=20)
        option4.grid(row=4,column=1,padx = 20, pady=20)
        option5.grid(row=5,column=1,padx = 20, pady=20)

              
        button1 = ttk.Button(self, text="...",
                            command= lambda: controller.show_frame(Pageone))
        button1.grid(row=1, column=2, sticky = "es",padx = 20, pady=20 )
        button2 = ttk.Button(self, text="...",
                            command= lambda: controller.show_frame(Pagetwo))
        button2.grid(row=2, column=2, sticky = "es",padx = 20, pady=20 )
        button3 = ttk.Button(self, text="...",
                            command= lambda: controller.show_frame(Pagethree))
        button3.grid(row=3, column=2, sticky = "es",padx = 20, pady=20 )
        button4 = ttk.Button(self, text="...",
                            command= lambda: controller.show_frame(Pagefour))
        button4.grid(row=4, column=2, sticky = "es",padx = 20, pady=20 )
        button5 = ttk.Button(self, text="...",
                            command= lambda: controller.show_frame(Pagefive))
        button5.grid(row=5, column=2, sticky = "es",padx = 20, pady=20 )


class Pageone(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text="ADD A AREA", font = HEADING_FONT)
        option1 = tk.Label(self, text="Name : ", font = LARGE_FONT)
        option2 = tk.Label(self, text=" Temperature: ", font = LARGE_FONT)
        option3 = tk.Label(self, text="Crop ID : ", font = LARGE_FONT)

        label.grid(row=1, column=1,columnspan=2, padx = 20, pady=20)
        option1.grid(row=2,column=1,padx = 20, pady=20)
        option2.grid(row=3,column=1,padx = 20, pady=20)
        option3.grid(row=4,column=1,padx = 20, pady=20)

        entry1 = tk.Entry(self)
        entry2 = tk.Entry(self)
        entry3 = tk.Entry(self)

        entry1.grid(row=2,column=2,padx = 20, pady=20)
        entry2.grid(row=3,column=2,padx = 20, pady=20)
        entry3.grid(row=4,column=2,padx = 20, pady=20)
              
        button1 = ttk.Button(self, text="Back",
                            command= lambda: controller.show_frame(StartPage))
        button1.grid(row=0, columnspan = 3, padx = 20, pady=20 )
        button2 = ttk.Button(self, text="Submit",
                            command= lambda: insert_area(entry1.get(), entry2.get(), entry3.get()))
        button2.grid(row=5, columnspan = 3, padx = 20, pady=20 )


class Pagetwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text="ADD A CROP", font = HEADING_FONT)
        option0 = tk.Label(self, text="Crop Unique Id : ", font = LARGE_FONT)
        option1 = tk.Label(self, text="Rainfall : ", font = LARGE_FONT)
        option2 = tk.Label(self, text="Pesticide : ", font = LARGE_FONT)
        option3 = tk.Label(self, text="Crop Cost (in Rs. per sq feet) : ", font = LARGE_FONT)

        label.grid(row=1, column=1,columnspan=2, padx = 20, pady=20)
        option0.grid(row=2,column=1,padx = 20, pady=20)
        option1.grid(row=3,column=1,padx = 20, pady=20)
        option2.grid(row=4,column=1,padx = 20, pady=20)
        option3.grid(row=5,column=1,padx = 20, pady=20)

        entry0 = tk.Entry(self)
        entry1 = tk.Entry(self)
        entry2 = tk.Entry(self)
        entry3 = tk.Entry(self)

        entry0.grid(row=2,column=2,padx = 20, pady=20)
        entry1.grid(row=3,column=2,padx = 20, pady=20)
        entry2.grid(row=4,column=2,padx = 20, pady=20)
        entry3.grid(row=5,column=2,padx = 20, pady=20)
              
        button1 = ttk.Button(self, text="Back",
                            command= lambda: controller.show_frame(StartPage))
        button1.grid(row=0, columnspan = 3, padx = 20, pady=20 )
        button2 = ttk.Button(self, text="Submit",
                            command= lambda:  insert_crop(entry0.get(), entry1.get(), entry2.get(), entry3.get()))
        button2.grid(row=6, columnspan = 3, padx = 20, pady=20 )



class Pagethree(tk.Frame):
    
    def __init__(self, parent, controller):
        #super(Pagethree, self).__init__()
        tk.Frame.__init__(self,parent)

        def wrapper(entry):
            c.execute('SELECT Area.Name, Area.Temperature, Area.CropID, Crop.IdCode, Crop.Pesticide,Crop.Cost FROM Area INNER JOIN Crop ON Area.CropID = Crop.IdCode WHERE Area.Name = ?',(entry.get(),))
            info = c.fetchall()
            if len(info) == 0:
                messagebox.showinfo(title = "Caution", message = "No such area exists")
                controller.show_frame(Pagethree)
            else:
                ROW = info[0]
                #print (ROW)
                controller.dynamic_page(Pagesix, parent, ROW)
                controller.show_frame(Pagesix)


        query = tk.Label(self, text="Enter a Area Name: ", font = LARGE_FONT)
        option2 = tk.Label(self, text="NAME", font = LARGE_FONT)
        option3 = tk.Label(self, text="TEMPERATURE", font = LARGE_FONT)
        option4 = tk.Label(self, text="CROP ID", font = LARGE_FONT)
        option5 = tk.Label(self, text="RAINFALL", font = LARGE_FONT)
        option6 = tk.Label(self, text="PESTICIDE", font = LARGE_FONT)
        option7 = tk.Label(self, text="CROP COST ", font = LARGE_FONT)

        query.grid(row=1,column=1,padx = 20, pady=20)
        option2.grid(row=2,column=1,padx = 20, pady=20)
        option3.grid(row=2,column=2,padx = 20, pady=20)
        option4.grid(row=2,column=3,padx = 20, pady=20)
        option5.grid(row=2,column=4,padx = 20, pady=20)
        option6.grid(row=2,column=5,padx = 20, pady=20)
        option7.grid(row=2,column=6,padx = 20, pady=20)

        entry1 = tk.Entry(self)
        entry1.grid(row=1,column=2,padx = 20, pady=20)
  
        button1 = ttk.Button(self, text="Back",
                            command= lambda: controller.show_frame(StartPage))
        button1.grid(row=0, columnspan = 3, padx = 20, pady=20 )
        button1 = ttk.Button(self, text="Fetch",
                            command= lambda: wrapper(entry1))
        button1.grid(row=1, column = 3, padx = 20, pady=20 )



class Pagesix(tk.Frame):

    row = None
    
    def __init__(self, parent, controller, ROW):
        #super(Pagesix, self).__init__()
        tk.Frame.__init__(self,parent)
        row = ROW
       
        option2 = tk.Label(self, text="NAME", font = LARGE_FONT)
        option3 = tk.Label(self, text="TEMPERATURE", font = LARGE_FONT)
        option4 = tk.Label(self, text="CROP ID", font = LARGE_FONT)
        option5 = tk.Label(self, text="RAINFALL", font = LARGE_FONT)
        option6 = tk.Label(self, text="PESTICIDE", font = LARGE_FONT)
        option7 = tk.Label(self, text="CROP COST ", font = LARGE_FONT)

        option2.grid(row=2,column=1,padx = 20, pady=20)
        option3.grid(row=2,column=2,padx = 20, pady=20)
        option4.grid(row=2,column=3,padx = 20, pady=20)
        option5.grid(row=2,column=4,padx = 20, pady=20)
        option6.grid(row=2,column=5,padx = 20, pady=20)
        option7.grid(row=2,column=6,padx = 20, pady=20)

        index = 3

        if row is not None:
            tk.Label(self, text=row[0], font = LARGE_FONT).grid(row=index, column=1,padx = 20, pady=20)
            tk.Label(self, text=row[1], font = LARGE_FONT).grid(row=index, column=2,padx = 20, pady=20)
            tk.Label(self, text=row[2], font = LARGE_FONT).grid(row=index, column=3,padx = 20, pady=20)
            tk.Label(self, text=row[3], font = LARGE_FONT).grid(row=index, column=4,padx = 20, pady=20)
            tk.Label(self, text=row[4], font = LARGE_FONT).grid(row=index, column=5,padx = 20, pady=20)
            tk.Label(self, text=row[5], font = LARGE_FONT).grid(row=index, column=6,padx = 20, pady=20)
               
        button1 = ttk.Button(self, text="Back",
                            command= lambda: controller.show_frame(StartPage))
        button1.grid(row=0, columnspan = 3, padx = 20, pady=20 )
        

class Pagefour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        option1 = tk.Label(self, text="AREA ID", font = LARGE_FONT)
        option2 = tk.Label(self, text="NAME", font = LARGE_FONT)
        option3 = tk.Label(self, text="TEMPERATURE", font = LARGE_FONT)
        option4 = tk.Label(self, text="CROP ID", font = LARGE_FONT)

        option1.grid(row=1,column=0,padx = 20, pady=20)
        option2.grid(row=1,column=1,padx = 20, pady=20)
        option3.grid(row=1,column=2,padx = 20, pady=20)
        option4.grid(row=1,column=3,padx = 20, pady=20)

        
        c.execute('SELECT * FROM Area')
        index=3
        for row in c.fetchall():
            #print(row) #this works just fine
            tk.Label(self, text=row[0], font = LARGE_FONT).grid(row=index, column=0,padx = 20, pady=20)
            tk.Label(self, text=row[1], font = LARGE_FONT).grid(row=index, column=1,padx = 20, pady=20)
            tk.Label(self, text=row[2], font = LARGE_FONT).grid(row=index, column=2,padx = 20, pady=20)
            tk.Label(self, text=row[3], font = LARGE_FONT).grid(row=index, column=3,padx = 20, pady=20)
            index+=1

        button1 = ttk.Button(self, text="Back",
                            command= lambda: controller.show_frame(StartPage))
        button1.grid(row=0, columnspan = 3, padx = 20, pady=20 )


class Pagefive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        option1 = tk.Label(self, text="CROP ID", font = LARGE_FONT)
        option2 = tk.Label(self, text="RAINFALL", font = LARGE_FONT)
        option3 = tk.Label(self, text="PESTICIDE", font = LARGE_FONT)
        option4 = tk.Label(self, text="CROP COST ", font = LARGE_FONT)

        option1.grid(row=1,column=0,padx = 20, pady=20)
        option2.grid(row=1,column=1,padx = 20, pady=20)
        option3.grid(row=1,column=2,padx = 20, pady=20)
        option4.grid(row=1,column=3,padx = 20, pady=20)

        with conn:
            c = conn.cursor()
            c.execute('SELECT * FROM Crop')
            index=3
            for row in c.fetchall():
                #print(row) #this works just fine
                tk.Label(self, text=row[1], font = LARGE_FONT).grid(row=index, column=0,padx = 20, pady=20)
                tk.Label(self, text=row[2], font = LARGE_FONT).grid(row=index, column=1,padx = 20, pady=20)
                tk.Label(self, text=row[3], font = LARGE_FONT).grid(row=index, column=2,padx = 20, pady=20)
                tk.Label(self, text=row[4], font = LARGE_FONT).grid(row=index, column=3,padx = 20, pady=20)
                index+=1
        
        button1 = ttk.Button(self, text="Back",
                            command= lambda: controller.show_frame(StartPage))
        button1.grid(row=0, columnspan = 3, padx = 20, pady=20 )


        
create_area_table()
create_crop_table()
app = try1()
#app.geometry("640x360")
app.mainloop()
