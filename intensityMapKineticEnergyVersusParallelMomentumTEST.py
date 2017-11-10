# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:43:19 2017

@author: herri
"""

#----------------------BEGINNING OF IMPORTS--------------------------
from os import path
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from numpy import genfromtxt
from scipy.constants import *
from scipy.interpolate import griddata



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


def intensityMapKineticEnergyVersusDegrees(): 
    figureOutputName = "OUTPUTIntensityMapKKineticEnergyVersusDegrees.png"

    arrKParallel = np.empty([dimensionOneSize,dimensionTwoSize])
    #Calculate the parrallel momentum for each intensity
    #KParallel=(SQRT(2*Me*Ekin)*sin(Theta))/HBAR
    for i in range(0, dimensionOneSize):
        for j in range(0, dimensionTwoSize):
            arrKParallel[i,j]=(((2*electron_mass*arrKineticEnergies[i]*e)**0.5)*(np.sin(arrDegrees[j]))/(hbar))



    #Select number of bins
    numberOfColourBins=15
    # Create data
    xs = arrKParallel
    ys = arrKineticEnergies
    zs = arrIntensity
    
#    plt.scatter(xs,ys,marker="o",c="b",s=5)
    
    #As the data set has become distorted by converting degrees into kparallel
    #we must now interploate to create an intensity map.
    #To do this we must define a grid
    #Define the number of points in the grid
#    npts=200
    #Define grid
#    xi=np.linspace(np.amin(arrKParallel),np.amax(arrKParallel),npts)
#    yi=np.linspace(arrDegrees[0],arrDegrees[569],npts)
#    zi = griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')

    
    
    #Number of colour levels
    levels = MaxNLocator(nbins=numberOfColourBins).tick_values(zs.min(), zs.max())
    #Pick the desired colormap, sensible levels, and define a normalization instance which takes data values and translates those into levels.
    cmap = plt.get_cmap('PiYG')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)
    #Create a figure containing ax0
    fig, (ax0) = plt.subplots(nrows=1)
    #Plot ax0 to the figure and format
    im = ax0.pcolormesh(xs, ys, zs, cmap=cmap, norm=norm)
    fig.colorbar(im, ax=ax0)
    ax0.set_title("Intensity Map (Energy versus Degrees) ["+str(numberOfColourBins)+" colour bins]")
    plt.ylabel("Kinetic Energy /eV")
    plt.xlabel("K Parallel")
    fig.tight_layout()
    plt.show()


intensityMapKineticEnergyVersusDegrees()

