# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 18:04:26 2017

@author: herri
"""
#----------------------BEGINNING OF IMPORTS--------------------------
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import genfromtxt
import math
#--------------------------END OF IMPORTS-----------------------------

#---------------------BEGINNING OF VARIABLE DEFINITIONS---------------
global dimensionOneSize
global dimensionTwoSize
#---------------------------END OF VARIABLE DEFINITIONS-----------------

#---------------------------IMPORT OF DATA------------------------------------
arrIntensity = genfromtxt("Intensity.csv", delimiter=",")
arrKineticEnergies = genfromtxt("KineticEnergies.csv", delimiter=",")
arrDegrees = genfromtxt("Degrees.csv", delimiter=",")

dimensionOneSize = len(arrKineticEnergies)
dimensionTwoSize = len(arrDegrees)

#-----------------------------END OF DATA IMPORT-----------------------------

def energyDispersiveCutDegrees(degreeCentre, degreeRange): 
    figureOutputName = "OUTPUTEnergyDispersiveCut.png"
    ys=[]
    xs=[]
    
    #Finds out the position of the measured degree (degreeCentrePosition) closest to the desired inputted central degree (degreeCentre)
    workInt=0
    for i in range(0,dimensionTwoSize):
        if i==0:
            wokrInt=i
        elif (math.fabs(degreeCentre-arrDegrees[i]))<(math.fabs(degreeCentre-arrDegrees[workInt])):
            workInt=i
    degreeCentrePosition = workInt
    
    #Finds out the position of the left-most degree taken into account for the integration, considering the range of values desired (degreeRange)
    workInt=0
    leftMostDegree=degreeCentre-degreeRange
    for i in range(0,dimensionTwoSize):
        if i==0:
            workInt=i
        elif (math.fabs(leftMostDegree-arrDegrees[i]))<(math.fabs(leftMostDegree-arrDegrees[workInt])):
            workInt=i
    degreeLeftMostPosition = workInt
    print(arrDegrees[degreeLeftMostPosition])
  
    #Finds out the position of the right-most degree taken into account for the integration, considering the range of values desired (degreeRange)
    workInt=0
    rightMostDegree=degreeCentre+degreeRange
    for i in range(0,dimensionTwoSize):
        if i==0:
            workInt=i
        elif (math.fabs(rightMostDegree-arrDegrees[i]))<(math.fabs(rightMostDegree-arrDegrees[workInt])):
            workInt=i
    degreeRightMostPosition = workInt
    print(arrDegrees[degreeRightMostPosition])
    
    #Loops round for every kinetic energy
    for i in range(0,dimensionOneSize):
        #Calculates the average intensity in the degree range inputted at each kinetic energy
        sumOfIntensity=0
        for j in range(degreeLeftMostPosition,degreeRightMostPosition+1):
            sumOfIntensity+=arrIntensity[i,j]
        averageIntensity=sumOfIntensity/(degreeRightMostPosition-degreeLeftMostPosition)
        #Stores the kinetic energy its associated average intensity in the ys and xs arrays. These will be used later for plotting the graph.
        ys.append(averageIntensity)
        xs.append(arrKineticEnergies[i])
        
    #Plots ys vs xs to give an energy dispersive cut.    
    plt.plot(xs,ys)
    plt.ylabel("Average Intensity")
    plt.xlabel("Kinetic Energy /eV")
    plt.suptitle("Energy Dispersive Cut at "+str(degreeCentre) +" degrees with an angle range of +=" + str(degreeRange) +" degrees")
    
    #Saves plot using the desired file save name
    #plt.savefig(figureOutputName)

    
energyDispersiveCutDegrees(0,5)