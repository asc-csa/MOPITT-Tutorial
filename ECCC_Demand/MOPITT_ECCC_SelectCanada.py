# -*- coding: utf-8 -*-
"""
Copyrights / Droit d'auteurs
(C) 2018 The HDF Group 
(C) 2020 Government of Canada

---
This example code was written for an ECCC demand (November 2020).

It illustrates how to access a MOPITT MOP03JM version 8 
csv file in Python and select latitudes and longitudes of Canada.
It also gives a visualization example  of the portion selected

---
Ce code d'exemple a été écris pourune demande de ECCC (novembre 2020).

Il montre comment accéder au fichier MOPITT MOP03JM version 8
format csv en python et sélectionner les données autour du Canada.

Il donne aussi un exemple de visualization pour les données sélectionnées.
 
---
Tested under / Testé sous: Python 3.7
Last updated / Modifié le: 2020-11-25
By / Par : Camille Roy, Canadian Space Agency / Agence Spatiale Canadienne 


"""

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

path_to_folder = r'PATH\TO\FOLDER'
#Nom du fichier csv à lire / Name of the csv file to read
FILE_NAME = 'MOP03JM-201804-L3V95.6.3.csv'

#lecture des données / Read data
data = np.loadtxt(path_to_folder+'//'+FILE_NAME,delimiter=',',skiprows=0).T 

lat,long = data[0:2]    #Latitude + Longitude
COMR_tot = data[2]
COMR_Profile = data[3:]   #CO Mixing Ratio profile (Surface+900hPa-100hPa)

#%% SELECT LONGITUDE AND LATITUDE TO OBSERVE
latlim = [40,90] #longitude [min,max]
longlim=[-145,-50] #latitude [min,max]

#SELECT DATA IN LATITUDE LIMITS / SELECTIONNE LES DONNÉES DANS LES LIMITES DE LATITUDE
newlat = lat[np.logical_and(lat<latlim[1],lat>latlim[0])]
newlong = long[np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_tot = COMR_tot[np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Surface = COMR_Profile[0][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile900 = COMR_Profile[1][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile800 = COMR_Profile[2][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile700 = COMR_Profile[3][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile600 = COMR_Profile[4][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile500 = COMR_Profile[5][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile400 = COMR_Profile[6][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile300 = COMR_Profile[7][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile200 = COMR_Profile[8][np.logical_and(lat<latlim[1],lat>latlim[0])]
newCOMR_Profile100 = COMR_Profile[9][np.logical_and(lat<latlim[1],lat>latlim[0])]

#SELECT DATA IN LONGITUDE LIMITS / SELECTIONNE LES DONNÉES DANS LES LIMITES DE LONGITUDE
newCOMR_tot = newCOMR_tot[np.logical_and(newlong<longlim[1],newlong>longlim[0])]
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

#CREATES ARRAY OF PROFILE / CRÉE VECTEUR DU PROFILE
newCOMR_Profile = np.array((newCOMR_Surface,newCOMR_Profile900,newCOMR_Profile800,newCOMR_Profile700,newCOMR_Profile600,newCOMR_Profile500,newCOMR_Profile400,newCOMR_Profile300,newCOMR_Profile200,newCOMR_Profile100))
Tab = np.array((newlat,newlong,newCOMR_tot,newCOMR_Surface,newCOMR_Profile900,newCOMR_Profile800,newCOMR_Profile700,newCOMR_Profile600,newCOMR_Profile500,newCOMR_Profile400,newCOMR_Profile300,newCOMR_Profile200,newCOMR_Profile100)).T

#SAVE AS CSV FILE / ENREGISTRE EN FICHIER CSV
newFILENAME = 'Canada_'+FILE_NAME.replace('.he5','.csv')
np.savetxt(path_to_folder+'//'+newFILENAME, Tab,'%g',delimiter=',',
            header='Latitude, Longitude, COTotalColumn,COMixingRatio surface,COMixingRatio 900hPa,COMixingRatio 800hPa,COMixingRatio 700hPa,COMixingRatio 600hPa, COMixingRatio 500hPa,COMixingRatio 400hPa,COMixingRatio 300hPa,COMixingRatio 200hPa,COMixingRatio 100hPa,RetrievedSurfaceTemperature ')
print('CSV Total File downloaded')

# VISUALIZATION ON BASEMAP / VISUALISATION GRAPHIQUE SUR CARTE DU MONDE DE BASEMAP
m = Basemap(projection='cyl', resolution='l',
            llcrnrlat=20, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=-30)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90, 91, 45))
m.drawmeridians(np.arange(-180, 180, 45), labels=[True,False,False,True])
sc = m.scatter(newlong, newlat, c=newCOMR_Surface, s=2, cmap=plt.cm.jet,
                edgecolors=None, linewidth=0)
cb = m.colorbar()
cb.set_label('mol/cm^2') #Unités, voir readme.txt / Units, see readme.txt

basename = os.path.basename(FILE_NAME)
plt.title('Visualisation pour le Canada de \n{0}'.format(basename))
fig = plt.gcf()
pngfile = "{0}.py.png".format(basename)
fig.savefig(pngfile,dpi=400) #SAVE FILE / ENREGISTRE IMAGE
