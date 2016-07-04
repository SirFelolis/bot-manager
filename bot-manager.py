from tkinter import *
from tkinter.filedialog import askopenfilename
from subprocess import Popen, PIPE, STDOUT, CREATE_NEW_CONSOLE

import os
import getpass

user = getpass.getuser()

saveFile = 'savefile.bms'

class Window(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.master = master

        self.InitWindow()

    def InitWindow(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        # Browse button
        buttonBrowse = Button(self.master, text="Browse", command=self.ChooseFile)
        buttonBrowse.place(x=400,y=10, anchor=NE)

        # Run button
        buttonRun = Button(self.master, text="Run", command=lambda: self.RunFile())
        buttonRun.place(x=440,y=10, anchor=NE)

        labelPath = Label(self.master, relief=SUNKEN, )
        labelPath.pack()
        labelPath.place(x=10, y=15, width=320)

        # Quit button
        buttonQuit = Button(self.master, text="Quit", command=self.ClientExit)
        buttonQuit.pack(side=BOTTOM)

        # Tool menu
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # Put these in the order that they are supposed to appear!
        file = Menu(menu, tearoff=0)
        file.add_command(label='Open File', command=self.ChooseFile)

        file.add_separator()

        file.add_command(label='Exit', command=self.ClientExit)

        menu.add_cascade(label='File', menu=file)

    def ChooseFile(self):
        fname = askopenfilename(initialdir="C:/",
                                filetypes=(("Batch script", "*.bat"), ("All files", "*.*")),
                                title="Choose a file")
        file = open(saveFile, "a")
        file.write('\n' + fname)
        file.close()

        try:
            self.RunFile(fname)
        except:
            print("Failed to open a file")

    def RunFile(self, fname: StringVar):
        fdir = os.path.split(fname)[0]
        p=Popen(fname, cwd=fdir, creationflags=CREATE_NEW_CONSOLE)

    def ClientExit(self):
        exit()

root = Tk()
root.geometry("450x300")

app = Window(root)

root.mainloop()