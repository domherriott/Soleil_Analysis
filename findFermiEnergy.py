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
from scipy.constants import *

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
dimensionOneStep = arrKineticEnergies[1] - arrKineticEnergies[0]

#-----------------------------END OF DATA IMPORT-----------------------------

#Calculates the average intensity across all angles and then plots this as a function of emitted KE
def energyDispersiveCutAllDegrees(): 
    figureOutputName = "OUTPUTEnergyDispersiveCutAllDegrees.png"
    ys=[]
    xs=[]
    #Loops round for every kinetic energy
    for i in range(0,dimensionOneSize):
        #Calculates the average intensity in the degree range inputted at each kinetic energy
        sumOfIntensity=0
        for j in range(0,dimensionTwoSize):
            sumOfIntensity+=arrIntensity[i,j]
        averageIntensity=sumOfIntensity/(dimensionTwoSize)
        #Stores the kinetic energy its associated average intensity in the ys and xs arrays. These will be used later for plotting the graph.
        ys.append(averageIntensity)
        xs.append(arrKineticEnergies[i])
        
    #Plots ys vs xs to give an energy dispersive cut.    
    plt.plot(xs,ys)
    plt.ylabel("Average Intensity")
    plt.xlabel("Kinetic Energy /eV")
    plt.suptitle("Energy Dispersive Cut across all degrees")
    
    #Saves plot using the desired file save name
    #plt.savefig(figureOutputName)

#Plots the energyDispersiveCutAllDegrees but within a specific KE range so that the Fermi Dirac distribution can be seen. It is also shifted to be within the ranges of 0-1
def energyDispersiveCutFermiDirac(energyLowerBound):
    figureOutputName = "OUTPUTFermiDirac"
    ys=[]
    xs=[]
    
    #Calculates the closest energy to the inputted lowerEnergyBound and then finds the position of it
    workInt=0
    for i in range(0,dimensionOneSize):
        if i==0:
            workInt=i
        elif (math.fabs(energyLowerBound-arrKineticEnergies[i]))<(math.fabs(energyLowerBound-arrKineticEnergies[workInt])):
            workInt=i
    energyLowerBound = workInt
    
    energyLowerBoundIntensity=0
    #Loops round for every kinetic energy
    for i in range(energyLowerBound,dimensionOneSize):
        #Calculates the average intensity in the degree range inputted at each kinetic energy.
        sumOfIntensity=0
        for j in range(0,dimensionTwoSize):
            sumOfIntensity+=arrIntensity[i,j]
        averageIntensity=sumOfIntensity/(dimensionTwoSize)
        #Stores the kinetic energy its associated average intensity in the ys and xs arrays. These will be used later for plotting the graph.
        ys.append(averageIntensity)
        xs.append(arrKineticEnergies[i])
    #Plots ys vs xs to give an energy dispersive cut.    
    plt.plot(xs,ys)    

    plt.ylabel("Average Intensity")
    plt.xlabel("Kinetic Eneryg /eV")
    plt.suptitle("Energy Dispersive Cut across selected energies")

    #Saves plot using the desired file save name
    #plt.savefig(figureOutputName)

#Same function as energyDispersiveCutFermiDirac yet it iterates for the inputted range of TKelvin and fermiEnergyEV to help solve these variables for the user. The user must set the inputted ranges of TKelvin and fermiEnergyEV.
def findFermiDirac(energyLowerBound,numberOfTempSteps):
    figureOutputName = "OUTPUTFermiDirac"
    
    fermiEnergyPosition=0
    closestProbability=0
    ys=[]
    xs=[]
    realYs=[]
    
    #Calculates the closest energy to the inputted lowerEnergyBound and then finds the position of it
    workInt=0
    for i in range(0,dimensionOneSize):
        if i==0:
            workInt=i
        elif (math.fabs(energyLowerBound-arrKineticEnergies[i]))<(math.fabs(energyLowerBound-arrKineticEnergies[workInt])):
            workInt=i
    energyLowerBoundPosition = workInt
    energyLowerBoundIntensity=0
    
    #Loops round for every kinetic energy, calculating the average intensity and converting it into a probability
    for i in range(energyLowerBoundPosition,dimensionOneSize):
        #Calculates the average intensity in the degree range inputted at each kinetic energy. Then divides this by the first average intensity calculated as this can be considered as probability of 1, to scale everything to a Fermi Dirac distribution.
        sumOfIntensity=0
        for j in range(0,dimensionTwoSize):
            sumOfIntensity+=arrIntensity[i,j]
        averageIntensity=sumOfIntensity/(dimensionTwoSize)
        #Then divides this by the first average intensity calculated as this can be considered as probability of 1, to scale everything to a Fermi Dirac distribution. This is ued to find the fermi energy by finding the position where the probability is closest to 0.5
        if i==energyLowerBoundPosition:
            energyLowerBoundIntensity=averageIntensity
        probability=averageIntensity/energyLowerBoundIntensity
        if (math.fabs(0.5-probability)<math.fabs(0.5-closestProbability)):
            closestProbability=probability
            fermiEnergyPosition=i
        #Stores the kinetic energy its associated probability in the ys and xs arrays. These will be used later for plotting the graph.
        ys.append(probability)
        realYs.append(probability)
        xs.append(arrKineticEnergies[i])
    
    #Stores and prints the found fermi energy
    fermiEnergyEV=arrKineticEnergies[fermiEnergyPosition]
    print("Fermi Energy = " + str(fermiEnergyEV))
    
    #Plots ys vs xs to give an energy dispersive cut.    
    plt.plot(xs,ys)    

    #Defines an array of numberOfTempSteps points between lowTKelvin and highTKelvin, the desired bounds that we are testing the temperature between.
    tempRange=np.arange(lowTKelvin,highTKelvin,((highTKelvin-lowTKelvin)/numberOfTempSteps))

    #Used to keep track of the optimum Fermi Energy and Temperature when looping
    bestDeltaYsSquared=1
    bestTemp=1
    bestTempPos=0
    

    for i in range(0,numberOfTempSteps):
        xs=np.arange(arrKineticEnergies[energyLowerBoundPosition],arrKineticEnergies[dimensionOneSize-1],dimensionOneStep)
        ys=1/(1+np.exp((xs-fermiEnergyEV)/((Boltzmann/e)*tempRange[i])))
        #Calculates the average of the squares of the differences between the experimental data and the theoretical fermi dirac distribution. By doing this we can have a metric for the fit of the curves and therefore try to maximise the fit.
        deltaYs=ys-realYs
        deltaYsSquared=deltaYs*deltaYs
        meanDeltaYsSquared = np.mean(deltaYsSquared)
        if meanDeltaYsSquared < bestDeltaYsSquared:
            bestDeltaYsSquared=meanDeltaYsSquared
            bestTemp=tempRange[i]
            bestTempPos=i


    xs=np.arange(arrKineticEnergies[energyLowerBoundPosition],arrKineticEnergies[dimensionOneSize-1],dimensionOneStep)
    TKelvin=540
    ys=1/(1+np.exp((xs-fermiEnergyEV)/((Boltzmann/e)*bestTemp)))
    plt.plot(xs,ys)
    plt.ylabel("probabiliy")
    plt.xlabel("energy")
    plt.suptitle("fermi dirac")
    
    print("Best temp: "+ str(tempRange[bestTempPos]))
    print("Best temperature range: "+str(tempRange[bestTempPos-1])+" - "+str(tempRange[bestTempPos+1])+" Kelvin")

    #Saves plot using the desired file save name
    #plt.savefig(figureOutputName)


#------------------------------------------------------------------------

#This polots the energy dispersive cut across all degrees for all energies
#energyDispersiveCutAllDegrees()

#This plots the energy dispersive cut across all degreees for a selected range of energies.
#The lower bound of the energy is defined below and this allows the tail of the energy
#dispersive cut (which shows the fermi dirac distribtuion) to be extracted
energyLowerBound=95.53
#energyDispersiveCutFermiDirac(energyLowerBound)

#By using the previous function the energyLowerBound can be successfully determined
#as correctly showing the Fermi Dirac distribution.
#The following function uses this determined energyLowerBound to then map a fermi dirac
#distribution onto it. This can be used to find the fermi energy as where the probability
#equals 0.5. This can then be used again to find the temperature which causes the fermi
#dirac function to fit best with the experimental data
lowTKelvin=1
highTKelvin=1000
numberOfTempSteps=10000
findFermiDirac(energyLowerBound,numberOfTempSteps)

