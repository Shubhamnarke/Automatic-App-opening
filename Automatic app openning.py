from tkinter import *
import os
from tkinter import filedialog,Text

root = Tk()
app = []

#============for opening the file=================#
def openfile():
    for widgets in frame.winfo_children():
        widgets.destroy()
    file = filedialog.askopenfilename(initialdir = "/",title = "select file",
                               filetype = (("executable",".exe"),("All files","*.*")))

    app.append(file)
    print(app)
    for db in app:
        lable = Label(frame,text=db,bg = "sky blue")
        lable.pack()

#==============for running the app====================#
def runapp():
    for db in app:
        os.startfile(db)


root["bg"] = "light gray"
root.geometry("1350x700+0+0")
Can =Canvas(height = 500 ,width = 1000,bg = "pale goldenrod",bd = 3,relief = SUNKEN)
Can.place(x = 100,y = 50)

frame = Frame(Can,bg ="white")
frame.place(relheight = 0.8,relwidth = 0.8,relx = 0.1,rely =0.1)

open_file = Button(root,text = "Open File",command = openfile)
open_file.place(x = 550, y = 590)

Run_Apps = Button(root,text = "Run Apps",command = runapp)
Run_Apps.place(x = 550, y = 620)
root.mainloop()