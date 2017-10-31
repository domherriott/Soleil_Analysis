# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:29:55 2017

@author: herri
"""

#-----------------------------------------------------------ALL IMPORTS-------------------------------------------------------
import numpy as np
from os import path
from tkinter import *

#---------------------------------------------------------END OF ALL IMPORTS-------------------------------------------------

#------------------------------------------------DEFINING ALL FUNCTIONS AND CLASSES----------------------------------------
   
class PageStructure:
    
    def __init__(self, master):
        
        master.winfo_toplevel().title("Soleil Data Analysis App")
        
        #-------Create root Main Menu-----
        menu = Menu(root)
        root.config(menu=menu, bg="#5FFFE0")
        
        master.minsize(width=350,height=300)

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
        toolbar = Frame(root, bg="#5FFFE0")
        insertButt = Button(toolbar, text="//Insert Image", command=placeholderTestFunction)
        insertButt.pack(side=LEFT, padx=2, pady=2)
        printButt = Button(toolbar, text="//Print", command=placeholderTestFunction)
        printButt.pack(side=LEFT, padx=2, pady=2)
        toolbar.pack(side=TOP, fill=X)


        #-------Status Bar------
        status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)
        
        
        #-----Make Frame and Buttons
        
        frame = Frame(master, width=500, height=500, bg="white")
        frame.pack(fill=BOTH)
        

        labelFileSource = Label(frame, text="File Source:", bg="white")
        entryFileSource = Entry(frame)
        buttonFileSource = Button(frame, text="Extract Data", command=placeholderTestFunction)
        labelMomCentre = Label(frame, text="Momentum Centre:", bg="white")
        entryMomCentre = Entry(frame)
        labelMomRange = Label(frame, text="Momentum Range:", bg="white")
        entryMomRange = Entry(frame)
        buttonMakePlot = Button(frame, text="Make Plot", command=placeholderTestFunction)

        labelFileSource.grid(row=0, sticky=E, padx=30, pady=10)
        entryFileSource.grid(row=0, column=1, padx=0, pady=10)
        buttonFileSource.grid(row=1, sticky=E, columnspan=2, padx=0, pady=10)
        labelMomCentre.grid(row=2, sticky=E, padx=30, pady=10)
        entryMomCentre.grid(row=2, column=1, padx=0, pady=10)
        labelMomRange.grid(row=3, sticky=E, padx=30, pady=10)
        entryMomRange.grid(row=3, column=1, padx=0, pady=10)
        buttonMakePlot.grid(row=4, sticky=E, columnspan=2, padx=0, pady=10)

        
def placeholderTestFunction():
    print("PlaceholderFunction has run.")
    
def extractData():
    fname = path.expanduser(r"RbFeSeS5AsGrown_0003.txt")

    #Make empty matrix for all the data points and empty vectors for KE and Deg
    arr = np.empty([570,601])
    vKE = np.empty([601])
    vDeg = np.empty([570])

    #Read Kinetic Energies into vector vKE
    wkString = ""

    with open(fname,"r") as f:
        wkString = f.readlines()[8]
    
    dataStart = wkString.index("=")
    wkString = wkString[(dataStart+1):]

    wkString = wkString + " "
    iMax = wkString.count(" ")
    i=0
    while i < iMax:
        pos = wkString.index(" ")
        vKE[i] = wkString[:pos]
        wkString = wkString[pos+1:]
        i=i+1

    #Read Degress into vector VDeg
    wkString = ""
    
    with open(fname,"r") as f:
        wkString = f.readlines()[11]
    
    dataStart = wkString.index("=")
    wkString = wkString[(dataStart+1):]

    wkString = wkString + " "
    iMax = wkString.count(" ")
    i=0
    while i < iMax:
        pos = wkString.index(" ")
        vDeg[i] = wkString[:pos]
        wkString = wkString[pos+1:]
        i = i + 1
        
    #Read main data set
    arr = np.empty([570,601])
    wkString = ""
        
    j=0
    while j < 601:
    
        with open(fname,"r") as f:
            wkString = f.readlines()[j+47]
        
        wkString = wkString + "  "
        i=0
        
        while i < 570:
            pos = wkString.index("  ")
            arr[i,j] = wkString[:pos]
            wkString = wkString[pos+1:]
            i = i + 1
            
        j = j + 1

    #Save arrays to csv files for future extraction
    np.savetxt("KineticEnergies.csv", vKE, delimiter=",")
    np.savetxt("Degrees.csv", vDeg, delimiter=",")
    np.savetxt("Counts.csv",arr, delimiter=",")

    print("-----Completed-----")

#----------------------------------------------------END OF FUNCTIONS--------------------------------------------------------


#-------Define window "root"-----
root = Tk()
mainPage = PageStructure(root)
root.mainloop()
