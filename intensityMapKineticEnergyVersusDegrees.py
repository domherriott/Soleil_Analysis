# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 17:43:19 2017

@author: herri
"""

#----------------------BEGINNING OF IMPORTS--------------------------
from os import path
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import genfromtxt
import math
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
from numpy import genfromtxt

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
    
    #Select number of bins
    numberOfColourBins=15
    # Create data
    xs = arrDegrees
    ys = arrKineticEnergies
    zs = arrIntensity
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
    plt.xlabel("Degrees")
    fig.tight_layout()
    plt.show()


intensityMapKineticEnergyVersusDegrees()

