------------------------------ FRANÇAIS (English follows) ------------------------------

# Codes pour filtrer et convertir en fichier .csv les fichier HDFEOS (.he5), et visualiser les données MOPITT, développés pour le site de données ouvertes de l'ASC.

Le script python "MOPITTData_FileConverter.py" traite les données et sélectionne les variables voulues dans le tableau, pour ensuite les convertir en fichiers de type csv. 
Le script "MOPITTData_ReaderAndVisualization.py" lit les fichiers .csv et sort un exemple de visualisation.

Droit d'auteur (C) Mai 2020 Gouvernement du Canada 
Créé par Camille Roy, Agence Spatiale Canadienne
Dernière modification le 2020-08-10

## Données MOPITT 

Les données originales ont été prises en format HDFEOS (.he5) à partir de la base de données ftp://l5ftl01.larc.nasa.gov/MOPITT/MOP03J.008
Il est à noter que le satellite MOPITT prend entre 3 et 4 jours pour obtenir une mesure globale des données.
 - Les données Joint Products (TIR + NIR) ont été utilisées car la qualité est supérieure pour le profil atmosphérique jusqu'à la surface. 
 - Les données de niveau 2 ont été utilisées pour maintenir la précision spatiale de 22km x 22km.
 - Les données TIR (Thermal Infrared Radiances) sont recommandées pour des études troposphériques. 
 - Les niveaux 1 et 3, ainsi que NIR (Near Infrared Radiances) et TIR (Thermal Infrared Radiances) sont aussi disponibles sur ftp://l5ftl01.larc.nasa.gov/MOPITT
Les données sont prises pour tous les jours disponibles de mars 2004 à avril 2020.
Le fichier contient 14 colonnes. Les deux premières sont les coordonnées latitude-longitude [deg]. Les 12 autres contiennent: 

 - COTotalColumn(1 column): Mesure du CO (Monoxide de Carbone) sur la colonne totale de l'atmosphère [mol/cm^2]
 - COMixingRatio (10 columns): "Mixing Ratio" du CO à 10 niveaux de pression différents (surface + 900 hPa-100 hPa par bonds de 100hPa) [ppbv].
 - RetrievedSurfaceTemperature (last column): Mesure de la température à la surface [K]

D'autres variables sont disponibles dans les fichiers HDFEOS originaux tel que des propriétés de la surface, des nuages, de l'atmosphère et du rayonnement, qui pourrait être utilisées dans une analyse plus poussée. 
Les informations sur toutes les variables des fichiers .he5 se trouvent dans les appendices A et B du document: https://www2.acom.ucar.edu/sites/default/files/mopitt/v8_users_guide_201812.pdf

## Scripts Python

Copyright (C) 2018 The HDF Group 
Les deux scripts se basent sur le code de l'équipe HDF : http://hdfeos.org/zoo/LaRC/MOP02J-20131129-L2V17.8.3.he5.py
D’autres exemples et explications sur la lecture/visualisation pour les données de MOPITT sont disponibles sur : http://hdfeos.org/zoo/index_openLaRC_Examples.php#MOPITT

## Prérequis pour exécuter le code : 

Pour "MOPITTData_FileConverter.py": 
 - Pour lire les données du type HDF (.he5), il faut installer la librairie h5py :  conda install h5py
 - Les fichiers HDF doivent être téléchargées dans le même dossier que le script python.

Pour "MOPITTData_ReaderAndVisualization.py" : 
 - Les fichiers .csv doivent être dans le même dossier que le script python.
 - Pour visualiser les données avec ce script, il faut installer la librairie python Basemap, un module de Matplotlib qui permet de faire de la visualisation sur une carte du monde:  conda install basemap



------------------------------ ENGLISH (Français précède) ------------------------------

# Short codes to filter and convert MOPITT data from HDFEOS (.he5) to .csv, as well as visualize them, written for the CSA Open Data website. 

The python script "MOPITTData_FileConverter.py" filters the data to select the needed variables, and converts it in .csv files.
The script "MOPITTData_ReaderAndVisualization.py" reads the .csv files and outputs an exemple of data visualization.

Copyright (C) May 2020 Government of Canada 
Created by Camille Roy, Canadian Space Agency
Last modified on 2020-05-21

## MOPITT Data 

The original data was taken in HDFEOS format (.he5) from the database ftp://l5ftl01.larc.nasa.gov/MOPITT/MOP03J.008
It should be noted that the MOPITT satellite takes between 3 to 4 days to aquire the global data. 
 - The Joint Products data (TIR + NIR) has been used for its measurement quality of the entire atmospheric profile, including the surface.
 - Level 2 data has been used to maintain the spatial resolution of 22km x 22km.
 - TIR (Thermal Infrared Radiances) data is recommended for tropospheric studies.
 - Level 1 and 3 data, as well as NIR (Near Infrared Radiances) and TIR (Thermal Infrared Radiances) can be found at ftp://l5ftl01.larc.nasa.gov/MOPITT

The data is provided for days from March 2004 to April 2020. 
The files contain 14 columns. The first two are the coordinates (latitude and longitude [deg]). The other 12 contain:

 - COTotalColumn(1 column): Measured CO levels on the total atmospheric column [mol/cm^2]. 
 - COMixingRatio (10 columns): Mixing Ratio of CO for 10 pressure profiles (surface + 900hPa-100hPa) [ppbv]
 - RetrievedSurfaceTemperature (last column): Temperature measurements at the surface [K].

Other variables are available in the original HDFEOS files such as information on the surface properties, clouds, atmospheric profiles and radiances, that can be used for further analysis.
Information on all the data available in the .he5 files can be found in appendices A and B of the document: https://www2.acom.ucar.edu/sites/default/files/mopitt/v8_users_guide_201812.pdf

## Python Scripts

Copyright (C) 2018 The HDF Group 
Both scripts are based on the HDF Group example code: http://hdfeos.org/zoo/LaRC/MOP02J-20131129-L2V17.8.3.he5.py
More examples and descriptions on the MOPITT data reading/visualization are available at : http://hdfeos.org/zoo/index_openLaRC_Examples.php#MOPITT

## Requirements for running the scripts : 

For "MOPITTData_FileConverter.py":
 - To read HDFEOS files (.he5), the h5py library is needed : conda install h5py
 - The HDF files must be in the same directory as the python file. 

For "MOPITTData_ReaderAndVisualization.py":
 - The .csv files must be in the same directory as the python file
 - To visualize the data with this code, the Basemap python library is needed : conda install basemap. This Matplotlib module is used to visualize the data on a world map. 






