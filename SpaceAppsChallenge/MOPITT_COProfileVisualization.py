# -*- coding: utf-8 -*-
"""
Copyrights / Droit d'auteurs
(C) 2018 The HDF Group 
(C) 2020 Government of Canada

---
This example code was written for the Covid19 Space Apps Challenge  
of May 30-31, 2020. 

It illustrates how to access a MOPITT MOP02J version 8 
csv file in Python. and gives a visualization example for the 
CO MIXING RATIO Profiles for a part Thailand 
(latitude: [16.5,17] degrees, longitude : [96,104] degrees)

The csv file must be in your current working directory.

---
Ce code d'exemple a été écris pour le Space Apps Challenge Covid19 
du 30-31 Mai 2020

Il montre comment accéder au fichier MOPITT MOP02J version 8
format csv en python et donne un exemple de visualization pour les données de
"CO MIXING RATIO Profiles" pour une partie de la Thaïlande 
(latitude: [16.5,17] degrés, longitude : [96,104] degrés)
 
Le fichier csv doit être dans le même dossier que le code .py . 

---
Tested under / Testé sous: Python 3.7
Last updated / Modifié le: 2020-05-29
By / Par : Camille Roy, Canadian Space Agency / Agence Spatiale Canadienne 


"""

import os
os.environ['PROJ_LIB'] = r'c:\Users\Camille\anaconda3\pkgs\proj4-5.2.0-ha925a31_1\Library\share'

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

path_to_folder = r'C:\Users\Camille\Documents\Uni\ASC\MOPITT\Nouveau dossier'
#Nom du fichier csv à lire / Name of the csv file to read
FILE_NAME = 'MOP03JM-201801-L3V95.6.3.csv'

#lecture des données / Read data
data = np.loadtxt(path_to_folder+'//'+FILE_NAME,delimiter=',',skiprows=0).T 

lat,long = data[0:2]    #Latitude + Longitude
COMR_Surface = data[3]  #CO Mixing Ratio Surface
COMR_Profile = data[4:-1]   #CO Mixing Ratio profile (900hPa-100hPa)


#%% SELECT LONGITUDE AND LATITUDE TO OBSERVE
longlim = [41,84] #longitude [min,max]
latlim=[0,53] #latitude [min,max]

#SELECT DATA IN LATITUDE LIMITS / SELECTIONNE LES DONNÉES DANS LES LIMITES DE LATITUDE
newlat = lat[np.logical_and(lat<latlim[1],lat>latlim[0])]
newlong = long[np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Surface = COMR_Surface[np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile900 = COMR_Profile[0][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile800 = COMR_Profile[1][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile700 = COMR_Profile[2][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile600 = COMR_Profile[3][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile500 = COMR_Profile[4][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile400 = COMR_Profile[5][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile300 = COMR_Profile[6][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile200 = COMR_Profile[7][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile100 = COMR_Profile[8][np.logical_and(lat<latlim[1],lat>latlim[0])]

#SELECT DATA IN LONGITUDE LIMITS / SELECTIONNE LES DONNÉES DANS LES LIMITES DE LONGITUDE
newCOMR_Surface = newCOMR_Surface[np.logical_and(newlong<longlim[1],newlong>longlim[0])]
newCOMR_Profile900 = newCOMR_Profile900[np.logical_and(newlong<longlim[1],newlong>longlim[0])]
newCOMR_Profile800 = newCOMR_Profile800[np.logical_and(newlong<longlim[1],newlong>longlim[0])]
newCOMR_Profile700 = newCOMR_Profile700[np.logical_and(newlong<longlim[1],newlong>longlim[0])]
newCOMR_Profile600 = newCOMR_Profile600[np.logical_and(newlong<longlim[1],newlong>longlim[0])]
newCOMR_Profile500 = newCOMR_Profile500[np.logical_and(newlong<longlim[1],newlong>longlim[0])]
newCOMR_Profile400 = newCOMR_Profile400[np.logical_and(newlong<longlim[1],newlong>longlim[0])]
newCOMR_Profile300 = newCOMR_Profile300[np.logical_and(newlong<longlim[1],newlong>longlim[0])]
newCOMR_Profile200 = newCOMR_Profile200[np.logical_and(newlong<longlim[1],newlong>longlim[0])]
newCOMR_Profile100 = newCOMR_Profile100[np.logical_and(newlong<longlim[1],newlong>longlim[0])]
newlat=newlat[np.logical_and(newlong<longlim[1],newlong>longlim[0])]
newlong=newlong[np.logical_and(newlong<longlim[1],newlong>longlim[0])]

#CREATES ARRAY OF PROFILE
newCOMR_Profile = np.array((newCOMR_Surface,newCOMR_Profile900,newCOMR_Profile800,newCOMR_Profile700,newCOMR_Profile600,newCOMR_Profile500,newCOMR_Profile400,newCOMR_Profile300,newCOMR_Profile200,newCOMR_Profile100))


#Altitude = [15.797,11.775,9.164,5.574,4.206,3.012,1.949,0.989,0] #Altitude en km
PLevels=[100,200,300,400,500,600,700,800,900,'Surface']

#MAX AND MIN VALUE OF CO MIXING RATIO/ VALEUR MAX ET MIN DE CO MIXING RATIO
min_ =newCOMR_Profile.min()
max_ = newCOMR_Profile.max()

#FIGURE
plt.figure(figsize=(17,10))
plt.imshow(newCOMR_Profile,origin='lower',cmap='jet',aspect ='auto' ,extent=(newlong.min(),newlong.max(),10,0))

#TICK LABELS 
plt.xticks(fontsize=20)
ticks = np.arange(1,11)
plt.yticks(ticks,PLevels,fontsize=20)
plt.minorticks_on()

#COLORBAR
plt.clim(min_, max_)
cb = plt.colorbar()
cb.set_label('CO Mixing Ratio [ppbv]',fontsize=23) #Unités, voir readme.txt / Units, see readme.txt
cb.ax.tick_params(labelsize=20)

#AXIS LABELS
plt.xlabel('Longitude [deg]',fontsize=24)
plt.ylabel('Pressure Level [hPa]',fontsize=24)
plt.title('{0}\n{1}'.format('22/03/2020 CO Mixing Ratios',' Latitudes between '+str(latlim[0])+' and '+str(latlim[1])+' [deg]'),fontsize=25)
plt.savefig('COProfile_Longitude.png') #SAVE
plt.show()