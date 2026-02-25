# -*- coding: utf-8 -*-
"""
Copyrights / Droit d'auteurs
(C) 2018 The HDF Group 
(C) 2026 Government of Canada

----
This example code was written for the CSA Open Data website.

It illustrates how to access a MOPITT MOP02J version 8 
HDF-EOS5 Grid file in Python. and convert it into a CSV file.

The HDF file must be in your current working directory.

----
Ce code d'exemple a été écrit pour le portail de données ouvertes de l'ASC.

Il montre comment accéder à un fichier MOPITT MOP02J version 8
HDF_EOS5 en python et le convertir en fichier CSV.
Le fichier HDF doit être dans le même dossier que le code en Python. 

----
Tested under / Testé sous: Python 3.11
Last updated / Modifié le: 2026-02-20
By / Par : Camille Roy    - Canadian Space Agency / Agence Spatiale Canadienne 
           Emiline Filion - Canadian Space Agency / Agence Spatiale Canadienne 
"""

import os
import re
import h5py
import numpy as np
import pandas as pd
import sys


# Constants
NB_COLUMNS = 14
COMMA_DELIMITER = ','
HDF_EOS5_FILE = ".he5"
INPUT_FOLDER = "C:\\development\\GitRepos\\MOPITT-Tutorial\\HDFEOS Converter"
DATA_LOCATION = 'HDFEOS/SWATHS/MOP02/Data Fields'
LATITUDE_LOCATION = 'HDFEOS/SWATHS/MOP02/Geolocation Fields/Latitude'
LONGITUDE_LOCATION = 'HDFEOS/SWATHS/MOP02/Geolocation Fields/Longitude'


def he5_to_csv(file_name: str):
    with h5py.File(file_name, mode='r') as f:

        # Read the HDFEOS (.he5) file
        # Uncomment the next line to see all available data
        # print(f[DATA_LOCATION].keys())
        group = f[DATA_LOCATION]
        
        # RetrievedCOTotalColumn
        dsname1 = 'RetrievedCOTotalColumn'   
        data1 = group[dsname1][:].T 
        units1 = group[dsname1].attrs['units'].decode() #Units
        fillvalue1 = group[dsname1].attrs['_FillValue'] 
        data1[data1 == fillvalue1] = np.nan 
        
        # RetrievedCOMixingRatioProfile
        dsname2 = 'RetrievedCOSurfaceMixingRatio'  
        data2 = group[dsname2][:].T
        units2 = group[dsname2].attrs['units'].decode() #Units
        fillvalue2 = group[dsname2].attrs['_FillValue'] 
        data2[data2 == fillvalue2] = np.nan 
        
        # RetrievedCOSurfaceMixingRatio
        dsname3 = 'RetrievedCOMixingRatioProfile'      
        data3 = group[dsname3][:].T[0] 
        units3 = group[dsname3].attrs['units'].decode() #Units
        fillvalue3 = group[dsname3].attrs['_FillValue'] 
        data3[data3 == fillvalue3] = np.nan 
        
        # RetrievedCOSurfaceMixingRatio
        dsname4 = 'RetrievedSurfaceTemperature'      
        data4 = group[dsname4][:].T 
        units4 = group[dsname4].attrs['units'].decode() #Units
        fillvalue4 = group[dsname4].attrs['_FillValue'] 
        data4[data4 == fillvalue4] = np.nan 
        
        # Geolocalisation information at:
        # '/HDFEOS INFORMATION/StructMetadata.0' 
        latitude = f[LATITUDE_LOCATION][()]
        longitude = f[LONGITUDE_LOCATION][()]

        # Disable scientific notation globally
        np.set_printoptions(suppress=True, precision=6)

        # Fill data
        converted_data = np.zeros((latitude.size, NB_COLUMNS))
        converted_data[:,0] = latitude
        converted_data[:,1] = longitude
        converted_data[:,2] = data1[0] #COTotalColumn
        converted_data[:,3] = data2[0] #RetrievedCOSurfaceMixingRatio
        for i in range(data3.shape[0]): #Loop on RetrievedCOMixingRatioProfile
            converted_data[:,4+i] = data3[i]

        converted_data[:,13] = data4[0] #RetrievedSurfaceTemperature

        # Save data to CSV
        np.savetxt(file_name.replace('.he5','.csv'), converted_data, fmt="%.6f", delimiter=COMMA_DELIMITER, header='Latitude, Longitude, COTotalColumn,COMixingRatio surface,COMixingRatio 900hPa,COMixingRatio 800hPa,COMixingRatio 700hPa,COMixingRatio 600hPa, COMixingRatio 500hPa,COMixingRatio 400hPa,COMixingRatio 300hPa,COMixingRatio 200hPa,COMixingRatio 100hPa,RetrievedSurfaceTemperature ')


def list_he5_files(input_folder):
    he5_files = []

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(HDF_EOS5_FILE):
                full_path = os.path.join(root, file)
                he5_files.append(full_path)

    return he5_files


if __name__ == "__main__":

    print("\nMOPITT Space Data")
    print("Converting HDF-EOS5 (he5) to CSV")

    # Get all He5 files from the input folder + sub-folders
    he5_files = list_he5_files(INPUT_FOLDER)
    print(f"\nFound {len(he5_files)} HDF-EOS5 file(s):\n")
    for he5_file in he5_files:
        print(he5_file)
        he5_to_csv(he5_file)

    # End of script
    print("\nThe script ended successfully")
    print("Have a good day!\n")