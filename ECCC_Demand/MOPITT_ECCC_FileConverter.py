# -*- coding: utf-8 -*-
"""
Copyrights / Droit d'auteurs
(C) 2018 The HDF Group 
(C) 2020 Government of Canada

---
This example code was written for an ECCC demand (November 2020).

It illustrates how to access the MOPITT MOP03JM version 8 data base on OpenDap 
and convert them into csv file in Python for the year 2018

---
Ce code d'exemple a été écris pourune demande de ECCC (novembre 2020).

Il montre comment accéder au fichier MOPITT MOP03JM version 8 dans la base de donn.es Open
format csv en python et sélectionner les données autour du Canada.

Il donne aussi un exemple de visualization pour les données sélectionnées.
 
---
Tested under / Testé sous: Python 3.7
Last updated / Modifié le: 2020-11-25
By / Par : Camille Roy, Canadian Space Agency / Agence Spatiale Canadienne 

"""

import requests
from bs4 import BeautifulSoup
import urllib
from urllib.request import urlretrieve
import h5py
import time
import multiprocessing
import os
import numpy as np

#.... Convert to csv
def convert(url,FILE_NAME,path):
    
    fullfilename = os.path.join(path, FILE_NAME)

    urlretrieve(url+'//'+FILE_NAME,FILE_NAME)
    
    #... end convert


def get_url_paths(url, ext='', params={}):
    response = requests.get(url, params=params)
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    soup = BeautifulSoup(response_text, 'html.parser')
    parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
    return parent


#DATA TO CHECK : 
latlim = [40,90] #longitude [min,max]
longlim=[-145,-50] #latitude [min,max] 
year = '2018'

# 1 : Get date list
url_J = 'https://l0dup05.larc.nasa.gov/opendap/MOPITT/MOP03JM.008/'

ext = 'html'
result = get_url_paths(url_J,ext)

url_files = np.zeros_like(result)
file_names = np.zeros_like(url_files)

for i, res in enumerate(result) :
    date = res.strip().split('/')[-2]
    url_files[i] = url_J+date+'/'
    
    date = '.'.join(date.strip().split('.')[0:2])
    file_date = ''.join(date.strip().split('.'))
    file_names[i] = 'MOP03JM-'+file_date+'-L3V95.6.3.he5'


files_yr = []
url_files_yr = []
for i in range(len(file_names)):
    if year in file_names[i]:
        files_yr.append(file_names[i])
        url_files_yr.append(url_files[i])


mypath = r'PATH\TO\FOLDER'


for i in range(len(files_yr[0:1])):
    
    FILE_NAME = files_yr[i]
    url = url_files_yr[i]
    fullfilename = os.path.join(mypath, FILE_NAME)
#    urlretrieve(url+'//'+FILE_NAME,FILE_NAME)
    
    
    with h5py.File(FILE_NAME, mode='r') as f:
        
        #Lecture des données. Code écris par HDF Group
        group = f['/HDFEOS/GRIDS/MOP03/Data Fields']
        
        #On peut voir les noms des variables avec : 
        #print(f['/HDFEOS/GRIDS/MOP03/Data Fields'].keys())
        dsname1 = 'RetrievedCOTotalColumnDay'    #Variable à observer. on peut la changer
        data1 = group[dsname1][:].T #Tableau des données voulues
      #  longname = group[dsname].attrs['long_name'].decode() #Nom de la variable
      #  units = group[dsname].attrs['units'].decode() #Unités
        fillvalue1 = group[dsname1].attrs['_FillValue'] #Valeur mise lorqu'il n'y a pas de données
        data1[data1 == fillvalue1] = np.nan #Remplace les -9999 par des nans.
        
        #RetrievedCOMixingRatioProfileDay
        dsname2 = 'RetrievedCOSurfaceMixingRatioDay'  
        data2 = group[dsname2][:].T
        fillvalue2 = group[dsname2].attrs['_FillValue'] 
        data2[data2 == fillvalue2] = np.nan 
    
        #RetrievedCOSurfaceMixingRatio
        dsname3 = 'RetrievedCOMixingRatioProfileDay'      
        data3 = group[dsname3][:].T
        fillvalue3 = group[dsname3].attrs['_FillValue'] 
        data3[data3 == fillvalue3] = np.nan 
    
        #RetrievedCOSurfaceMixingRatio
        dsname4 = 'RetrievedSurfaceTemperatureDay'      
        data4 = group[dsname4][:].T 
        fillvalue4 = group[dsname4].attrs['_FillValue'] 
        data4[data4 == fillvalue4] = np.nan 
    
        # Info de géolocalisation / Geolocalisation information  
        # We could query the string dataset
        # '/HDFEOS INFORMATION/StructMetadata.0' for the geolocation
        # information, but in this case we also have lat and lon datasets.
        y = f['/HDFEOS/GRIDS/MOP03/Data Fields/Latitude'][:]
        x = f['/HDFEOS/GRIDS/MOP03/Data Fields/Longitude'][:]
        longitude, latitude = np.meshgrid(x, y) #Tableaux 360x180 des coordonnées
        
        
        #Restructure coordonnées pour le tableau
        long = longitude.reshape(180*360) 
        lat = latitude.reshape(180*360)
        
        #DATA FORMAT FOR CSV TABLE / FORMAT DES DONNÉES POUR METTRE EN CSV.
        n = 14 #Nombre de colonnes / Number of columns
        Tab = np.zeros((lat.size,n)) #Tableau vide à remplir / Empty table to fil
        # Remplissage avec les données / Filling table with data
        Tab[:,0]=lat    #Latitude
        Tab[:,1]=long   #Longitude
        Tab[:,2]=data1.reshape(180*360) #COTotalColumn
        Tab[:,3]=data2.reshape(180*360) #RetrievedCOSurfaceMixingRatio
        for i in range(9): #Loop on RetrievedCOMixingRatioProfile
            Tab[:,4+i]=data3[i].reshape(180*360)
            #End loop on RetrievedCOMixingRatioProfile
        Tab[:,13]=data4.reshape(180*360) #RetrievedSurfaceTemperature
    
        #Sauvegarde du fichier en type .csv / Save csv file 
        np.savetxt(FILE_NAME.replace('.he5','.csv'), Tab,'%g',delimiter=',',
                    header='Latitude, Longitude, COTotalColumn,COMixingRatio surface,COMixingRatio 900hPa,COMixingRatio 800hPa,COMixingRatio 700hPa,COMixingRatio 600hPa, COMixingRatio 500hPa,COMixingRatio 400hPa,COMixingRatio 300hPa,COMixingRatio 200hPa,COMixingRatio 100hPa,RetrievedSurfaceTemperature ')
        print('CSV Total File downloaded')
    
    # os.remove(FILE_NAME)
    # print('HDF_EOS File Removed: ',FILE_NAME)
        
