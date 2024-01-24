# -*- coding: utf-8 -*-
"""
Copyrights / Droit d'auteurs
(C) 2018 The HDF Group 
(C) 2024 Government of Canada

---
This example code was written for the CSA Open Data website. 

It illustrates how to access a MOPITT MOP02J version 8 
CSV file in Python. and gives a visualization example for the 
Retrieved CO Total Column data using Basemap.

The CSV file must be in your current working directory.

More information can be found in the readme.txt

---
Ce code d'exemple a été écrit pour le portail de données ouvertes de l'ASC.

Il montre comment accéder au fichier MOPITT MOP02J version 8
format CSV en python et donne un exemple de visualization pour les données de
"Retrieved CO Total Column" utilisant Basemap.

Le fichier CSV doit être dans le même dossier que le code en Python. 

Plus d'information peut être trouvée sur le readme.txt

---
Tested under / Testé sous: Python 3.8
Last updated / Modifié le: 2020-05-13 
By / Par : Camille Roy, Canadian Space Agency / Agence Spatiale Canadienne 
"""

import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

#Nom du fichier csv à lire / Name of the csv file to read
FILE_NAME = 'C:\\Developpement\\GitRepos\\MOPITT\\HDFEOS Converter\\MOP02J-20181206-L2V18.0.3.csv'

#lecture des données / Read data
print ("Loading the CSV file...")
data = np.loadtxt(FILE_NAME,delimiter=',',skiprows=0).T 

lat,long = data[0:2]    #Latitude + Longitude
COTotalColumn = data[2] #CO total
COMR_Surface = data[3]  #CO Mixing Ratio Surface
COMR_Profile = data[4:-1]   #CO Mixing Ratio profile (900hPa-100hPa)
RetrievedSurfaceTemperature = data[-1]  #Retrieved Surface Temperature

# VISUALISATION GRAPHIQUE DE LA COLONNE TOTALE DU CO SUR CARTE DU MONDE AVEC BASEMAP
# DATA VISUALIZATION OF CO TOTAL COLUMN ON WORLD MAP USING BASEMAP
m = Basemap(projection='cyl', resolution='l',
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines(linewidth=0.5)
m.drawparallels(np.arange(-90, 91, 45))
m.drawmeridians(np.arange(-180, 180, 45), labels=[True,False,False,True])
sc = m.scatter(long, lat, c=COTotalColumn, s=1, cmap=plt.cm.jet,
                edgecolors=None, linewidth=0)
#cb = m.colorbar()
cb.set_label('mol/cm^2') #Unités, voir readme.txt / Units, see readme.txt
                        

basename = os.path.basename(FILE_NAME)
plt.title('{0}\n{1}'.format(basename, 'CO TOTAL COLUMN'))
fig = plt.gcf()
plt.show()
pngfile = "{0}.png".format(basename)
fig.savefig(pngfile)

# Fin du programme / End of script
print("\nThe script ended successfully")
print("Have a nice day!\n")