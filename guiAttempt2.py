# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:29:55 2017

@author: herri
"""

#-----------------------------------------------------------ALL IMPORTS-------------------------------------------------------
import numpy as np
from os import path
from tkinter import *
import matplotlib.pyplot as plt
import pandas as pd
from numpy import genfromtxt

#---------------------------------------------------------END OF ALL IMPORTS-------------------------------------------------


#----------------------------------------------------DEFINING GLOBAL VARIABLES---------------------------------------------
global dimensionOneSize
global dimensionTwoSize
global arrIntensity
global arrKineticEnergy
global arrDegrees
#---------------------------------------------------END OF DEFINING GLOBAL VARIABLES----------------------------------------


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
        
        global entryFileSource
        global entryMomCentre
        global entryMomRange
        global buttonMakePlot

        labelFileSource = Label(frame, text="File Source:", bg="white")
        entryFileSource = Entry(frame,)
        buttonFileSource = Button(frame, text="Extract Data", command=clickExtractData)
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

        #SET FILE USED FOR TESTING
        entryFileSource.insert(0,"C:/Users/herri/Documents/Thesis/Soleil_selected_data - TEST/RbFeSeS5AsGrown_0003.txt")
        
def clickExtractData():
    path = entryFileSource.get()
    extractData(path)
    #entryFileSource.delete(0,END)
    #entryFileSource.insert(0,"")

def extractData(path):
    
    #Determine size of Dimension 1 (Kinetic Energy eV) and Dimension 2 (Degrees) respectively and output to dimensionOneSize and dimensionTwoSize
    for i in range(0, 20):
        with open(path,"r") as f:
            workString = f.readlines()[i]
        if "Dimension 1 size=" in workString:
            dimensionOneSize=workString[17:]
            dimensionOneSize=int(dimensionOneSize)
            break

    for i in range(10,30):
        with open(path,"r") as f:
            workString = f.readlines()[i]
        if "Dimension 2 size=" in workString:
            dimensionTwoSize=workString[17:]
            dimensionTwoSize=int(dimensionTwoSize)
            break
    
    #Make blank np arrays to store Dimension 1 and Dimension 2 using dimensionOneSize and dimensionTwoSize. NB Now counting from 0.
    arrIntensity = np.empty([dimensionOneSize,dimensionTwoSize])
    arrKineticEnergy = np.empty([dimensionOneSize])
    arrDegrees = np.empty([dimensionTwoSize])
    
    #Extracts data from Dimension 1 into arrKineticEnergy
    for i in range(0, 20):
        with open(path,"r") as f:
            workString = f.readlines()[i]
        if "Dimension 1 scale=" in workString:
            workString=workString[18:]
            arrKineticEnergy = np.fromstring(workString,sep=" ")
            break
        
    #Extracts data from Dimension 1 into arrKineticEnergy
    for i in range(10, 30):
        with open(path,"r") as f:
            workString = f.readlines()[i]
        if "Dimension 2 scale=" in workString:
            workString=workString[18:]
            arrDegrees = np.fromstring(workString,sep=" ")
            break
        
    #Find first line of main data set    
    for i in range(30, 50):
        with open(path,"r") as f:
            workString = f.readlines()[i]
        if "[Data 1]" in workString:
            firstLine=i+1
            break
    
    #Extract main data set to array arrIntensity
    for i in range(0,dimensionOneSize):
        with open(path,"r") as f:
            workString = f.readlines()[firstLine+i]
            workArr = np.empty([dimensionTwoSize])
            workArr = np.fromstring(workString,sep="  ")
            for j in range(0,dimensionTwoSize):
                arrIntensity[i,j]=workArr[j]
    
    print("--------------DATA SUCCESSFULLY EXTRACTED---------------")

    
    #Save arrays to csv files for future extraction
    np.savetxt("KineticEnergies.csv", arrKineticEnergy, delimiter=",")
    np.savetxt("Degrees.csv", arrDegrees, delimiter=",")
    np.savetxt("Intensity.csv",arrIntensity, delimiter=",")

    print("-------------DATA SUCCESSFULLY SAVED---------------")   

def energyDispersiveCutDegrees(degreeCentre, degreeRange): 
    figureOutputName = "OUTPUTEnergyDispersiveCut.png"
    
    #Finds out the closest entered degrees the to input variable degreeCentre
    for i in range(0,dimensionTwoSize):
        print(math.fabs(arrDegrees[i]))

#==============================================================================
#     #shows we wanna sweep across the index at 251 as this is where degrees=0
#     print(degrees[251])
# 
#     i=0
#     while i<601:
#         ys.append(counts[251,i])
#         xs.append(kenergies[i])
#         i += 1
#     
#     #Make array of ys and xs to be used for plotting
#     ys = []
#     xs = []
#     print(xs)   
#     print(ys)
# 
#     plt.plot(xs,ys)
#     plt.ylabel("Counts")
#     plt.xlabel("Kinetic Energy")
#     plt.suptitle("Energy Dispersive Cut at 0 Degrees")
#     plt.savefig(figSaveName)
# 
#     print("---------Completed----------")
#==============================================================================


def energyDispersiveCutMomentum(momentumCentre, momentumRange):
    print("")


def placeholderTestFunction():
    print("PlaceholderFunction has run.")

#----------------------------------------------------END OF FUNCTIONS--------------------------------------------------------


#=====================COMMENTED OUT DURING TESTING=========================================================
# #-------Define window "root"-----
# root = Tk()
# mainPage = PageStructure(root)
# root.mainloop()
#==============================================================================

#USED FOR TESTING
extractData("C:/Users/herri/Documents/Thesis/Soleil_selected_data - TEST/RbFeSeS5AsGrown_0003.txt")


#USED FOR TESTING
#energyDispersiveCutDegrees(0,0)
