# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:29:55 2017

@author: herri
"""

from tkinter import *

#-------Define all functions and classes-----
   
class PageStructure:
    
    def __init__(self, master):
        
        #-------Create root Main Menu-----
        menu = Menu(root)
        root.config(menu=menu)
        
        master.minsize(width=500,height=500)

        subMenuFile = Menu(menu)
        menu.add_cascade(label="//File", menu=subMenuFile)
        subMenuFile.add_command(label="//New Project...", command=placeholderTestFunction)
        subMenuFile.add_command(label="//New", command=placeholderTestFunction)
        subMenuFile.add_separator()
        subMenuFile.add_command(label="//Exit", command=placeholderTestFunction)

        subMenuEdit = Menu(menu)
        menu.add_cascade(label="//Edit", menu=subMenuEdit)
        subMenuEdit.add_command(label="//Redo", command=placeholderTestFunction)
        
        #------Create Toolbar-----
        toolbar = Frame(root, bg="blue")
        insertButt = Button(toolbar, text="//Insert Image", command=placeholderTestFunction)
        insertButt.pack(side=LEFT, padx=2, pady=2)
        printButt = Button(toolbar, text="//Print", command=placeholderTestFunction)
        printButt.pack(side=LEFT, padx=2, pady=2)
        toolbar.pack(side=TOP, fill=X)


        #-------Status Bar------
        status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
        
        
        #-----Make Frame and Buttons
        
        frame = Frame(master, width=100, height=100)
        frame.pack()
        
        self.printButton = Button(frame, text="Print Message", command=self.printMessage)
        self.printButton.pack(side=LEFT)
        
        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)
    
    def printMessage(self):
        print("wow, this actually worked")
        
        
def placeholderTestFunction():
    print("PlaceholderFunction has run.")


#-------Define window "root"-----
root = Tk()
mainPage = PageStructure(root)
root.mainloop()
