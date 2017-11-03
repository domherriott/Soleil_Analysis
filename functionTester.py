# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 09:22:24 2017

@author: herri
"""
import numpy as np
from os import path

global dimensionOneSize
global dimensionTwoSize
global arrIntensity
global arrKineticEnergy
global arrDegrees

def findSizeOfDataSet(path):
    
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
    
    
    
    for i in range(0,(dimensionOneSize)):
        with open(path,"r") as f:
            workString = f.readlines()[firstLine+i]
            workArr = np.empty([dimensionTwoSize])
            workArr = np.fromstring(workString,sep="  ")
            for j in range(0,dimensionTwoSize):
                arrIntensity[i,j]=workArr[j]
    


findSizeOfDataSet("C:/Users/herri/Documents/Thesis/Soleil_selected_data - TEST/RbFeSeS5AsGrown_0003.txt")
    
    