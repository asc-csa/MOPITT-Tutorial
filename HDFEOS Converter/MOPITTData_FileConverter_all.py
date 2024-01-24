# -*- coding: utf-8 -*-
"""
Copyrights / Droit d'auteurs
(C) 2018 The HDF Group 
(C) 2024 Government of Canada

----
This example code was written for the Canadian Space Agency Open Data site

It illustrates how to access the MOPITT MOP02J version 8 
HDF-EOS5 NASA database in Python. and convert all files into CSV format.


----
Ce code d'exemple a été écrit pour le portail de données ouvertes de 
l'Agence Spatiale Canadienne

Il montre comment accéder à la base de données de la NASA des fichiers
MOPITT MOP02J version 8 HDF_EOS5 en python et de les convertir en Python.

----
Tested under / Testé sous: Python 3.8
Last updated / Modifié le: 2020-08-10 
By / Par : Camille Roy, Canadian Space Agency / Agence Spatiale Canadienne 
"""

'''Load the ftplib package '''
import ftplib
import h5py
import numpy as np
import os
import time
import multiprocessing

T1 = time.time()

'''Connect to FTP NASA site'''
ftp = ftplib.FTP('l5ftl01.larc.nasa.gov')
ftp.login()

ftp.cwd('MOPITT/MOP02J.008')


dirlist=[]
ftp.dir(dirlist.append)
#%%

def convert (year) :   
    """
    This function gets data from the NASA FTP link, selcets wanted variables
    and converts it to a CSV table

    Parameters
    ----------
    year : String
        Year to get data from, saved in string format

    Returns
    -------
    None.

    """
    files=[]
    for d in dirlist[1:]:
        if year in d:
            name = d.strip().split(' ')[-1]
            for i in ftp.nlst(name):
                if i.endswith('.he5'):
                    files.append(i)
                    
    #files.reverse()
    T2 = time.time()
    
    dt1 = T2-T1
    print('Temps pour liste de fichiers: ',dt1 )

    for fi in files:
        T2 = time.time()
        day = fi.strip().split('/')[0]
        FILE_NAME = fi.strip().split('/')[1]
        print(FILE_NAME)
        
        ftp.cwd(day)
        ftp.retrbinary('RETR ' + FILE_NAME, open(FILE_NAME, 'wb').write)[:]
          
        with h5py.File(FILE_NAME, mode='r') as f:
            #Lecture des données hdf / reading hdf data
            #Pour voir toutes les variables dipsonible / to see all available data : 
            #print(f['/HDFEOS/SWATHS/MOP02/Data Fields'].keys())
    
            group = f['HDFEOS/SWATHS/MOP02/Data Fields'] #location of data 
        
            #RetrievedCOTotalColumn
            dsname1 = 'RetrievedCOTotalColumn'   
            
            data1 = group[dsname1][:].T 
            # units1 = group[dsname1].attrs['units'].decode() #Units / Unités
            fillvalue1 = group[dsname1].attrs['_FillValue'] 
            data1[data1 == fillvalue1] = np.nan 
        
            #RetrievedCOMixingRatioProfile
            dsname2 = 'RetrievedCOSurfaceMixingRatio'  
            data2 = group[dsname2][:].T
            # units2 = group[dsname2].attrs['units'].decode() #Units / Unités
            fillvalue2 = group[dsname2].attrs['_FillValue'] 
            data2[data2 == fillvalue2] = np.nan 
        
            #RetrievedCOSurfaceMixingRatio
            dsname3 = 'RetrievedCOMixingRatioProfile'      
            data3 = group[dsname3][:].T[0] 
            # units3 = group[dsname3].attrs['units'].decode() #Units / Unités
            fillvalue3 = group[dsname3].attrs['_FillValue'] 
            data3[data3 == fillvalue3] = np.nan 
        
            #RetrievedCOSurfaceMixingRatio
            dsname4 = 'RetrievedSurfaceTemperature'      
            data4 = group[dsname4][:].T 
            # units4 = group[dsname4].attrs['units'].decode() #Units / Unités
            fillvalue4 = group[dsname4].attrs['_FillValue'] 
            data4[data4 == fillvalue4] = np.nan 
        
            # Info de géolocalisation / Geolocalisation information at:
            # '/HDFEOS INFORMATION/StructMetadata.0' 
            lat = f['HDFEOS/SWATHS/MOP02/Geolocation Fields/Latitude'][()]
            long = f['HDFEOS/SWATHS/MOP02/Geolocation Fields/Longitude'][()]
        
            #DATA FORMAT FOR CSV TABLE / FORMAT DES DONNÉES POUR METTRE EN CSV.
            n = 14 #Nombre de colonnes / Number of columns
            Tab = np.zeros((lat.size,n)) #Tableau vide à remplir / Empty table to fil
            # Remplissage avec les données / Filling table with data
            Tab[:,0]=lat    #Latitude
            Tab[:,1]=long   #Longitude
            Tab[:,2]=data1[0] #COTotalColumn
            Tab[:,3]=data2[0] #RetrievedCOSurfaceMixingRatio
            for i in range(data3.shape[0]): #Loop on RetrievedCOMixingRatioProfile
                Tab[:,4+i]=data3[i]
                #End loop on RetrievedCOMixingRatioProfile
            Tab[:,13]=data4[0] #RetrievedSurfaceTemperature
        
            #Sauvegarde du fichier en type CSV / Save CSV file 
            np.savetxt(FILE_NAME.replace('.he5','.csv'), Tab,'%g',delimiter=',',
                        header='Latitude, Longitude, COTotalColumn,COMixingRatio surface,COMixingRatio 900hPa,COMixingRatio 800hPa,COMixingRatio 700hPa,COMixingRatio 600hPa, COMixingRatio 500hPa,COMixingRatio 400hPa,COMixingRatio 300hPa,COMixingRatio 200hPa,COMixingRatio 100hPa,RetrievedSurfaceTemperature ')
            print('CSV File downloaded')
            
            ftp.cwd('../') # Returns to preceeding folder in FTP / Revient dans le dossier précédent dans le FTP

        #END OPEN
        
        #Delete .he5 temp file / Suprime le fichier temporaire .he5
        os.remove(FILE_NAME)
        print('HDF_EOS File Removed: ',FILE_NAME)
        #Print time it takes to convert 1 file / imprime le temps que ça prend pour convertir 1 fichier
        T3 = time.time()
        dt2 = T3-T2
        print('Temps 1 fichier: ',dt2) 
    #END FILE LOOP
    return

# List of years to get data from / Listes des années à aller chercher
years = [str(x) for x in range(2000,2020)]
years.reverse()

for year in years:  #Boucle sur toutes les années
    convert(year)

