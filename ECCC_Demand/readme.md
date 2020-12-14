## ------------------------------ FRANÇAIS (English will follow) -------------------------------

Droit d'auteur (C) Mai 2020 Gouvernement du Canada 
Écrit par Camille Roy, Agence Spatiale Canadienne
Dernière modification le 2020-11-25

# Scipts python qui convertissent les données MOPITT à partir de la base de données OpenDap de la NASA de fichiers HDFEOS vers le format csv. Écrit pour une demande ECCC. 

Le script "MOPITT_ECCC_FileConverter.py" permet d'aller chercher les fichiers dans la base de données OpenDap de la NASA et de convertir les fichiers du format HDFEOS vers le format csv.

Le script "MOPITT_ECCC_SelectCanada.py" permet de sélectionner les latitudes et longitudes entourant le Canada à partir des fichiers csv et ressort les fichiers réduits ainsi qu'une visualization des données.

## Données MOPITT 

Les données originales ont été prises en format HDFEOS (.he5) à partir de la base de données https://l0dup05.larc.nasa.gov/opendap/MOPITT/MOP03JM.008/
Il est à noter que le satellite MOPITT prend entre 3 et 4 jours pour obtenir une mesure globale des données.
 - Les données Joint Products (TIR + NIR) ont été utilisées car la qualité est supérieure pour le profil atmosphérique jusqu'à la surface. 
 - Les données de niveau 2 ont été utilisées pour maintenir la précision spatiale de 22km x 22km.
 - Les données TIR (Thermal Infrared Radiances) sont recommandées pour des études troposphériques. 
 - Les niveaux 1 et 3, ainsi que NIR (Near Infrared Radiances) et TIR (Thermal Infrared Radiances) sont aussi disponibles sur https://l0dup05.larc.nasa.gov/opendap/MOPITT/

Les données pour la demande de ECCC sont des moyennes mensuelles pour l'année 2018.

Le fichier contient 13 colonnes. Les deux premières sont les coordonnées latitude-longitude [deg]. Les 11 autres contiennent: 

 - COTotalColumn(1 column): Mesure du CO (Monoxide de Carbone) sur la colonne totale de l'atmosphère [mol/cm^2]
 - COMixingRatio (10 columns): "Mixing Ratio" du CO à 10 niveaux de pression différents (surface + 900 hPa-100 hPa par bonds de 100hPa) [ppbv].

D'autres variables sont disponibles dans les fichiers HDFEOS originaux tel que des propriétés de la surface, des nuages, de l'atmosphère et du rayonnement, qui pourrait être utilisées dans une analyse plus poussée. 
Les informations sur toutes les variables des fichiers .he5 se trouvent dans les appendices A et B du document: https://www2.acom.ucar.edu/sites/default/files/mopitt/v8_users_guide_201812.pdf

## Scripts Python

Copyright (C) 2018 The HDF Group 
Les deux scripts sont inspiré du le code de l'équipe HDF : http://hdfeos.org/zoo/LaRC/MOP02J-20131129-L2V17.8.3.he5.py
D’autres exemples et explications sur la lecture/visualisation pour les données de MOPITT sont disponibles sur : http://hdfeos.org/zoo/index_openLaRC_Examples.php#MOPITT


## Prérequis pour exécuter le code : 

Pour "MOPITT_ECCC_FileConverter.py": 
 - Pour lire les données du type HDF (.he5), il faut installer la librairie h5py :  conda install h5py
 - Pour accéder à la base de données, la librairie urllib.request est nécessaire

Pour "MOPITT_ECCC_SelectCanada.py" : 
 - Pour visualiser les données avec ce script, il faut installer la librairie python Basemap, un module de Matplotlib qui permet de faire de la visualisation sur une carte du monde:  conda install basemap


## ------------------------------ ENGLISH (Français précède) ------------------------------

# Python scripts to convert MOPITT data of the NASA OpenDap database from HDFEOS files to csv format. 

The python script "MOPITT_ECCC_FileConverter.py" filters the data to select the needed variables, and converts it in .csv files.
The script "MOPITT_ECCC_SelectCanada.py" reads the .csv files and outputs a reduced file including only the data around Canada, as well as an exemple of data visualization.

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

The data provided for the ECCC demand is monthly means of the year 2018. 
The files contain 13 columns. The first two are the coordinates (latitude and longitude [deg]). The other 11 contain:

 - COTotalColumn(1 column): Measured CO levels on the total atmospheric column [mol/cm^2]. 
 - COMixingRatio (10 columns): Mixing Ratio of CO for 10 pressure profiles (surface + 900hPa-100hPa) [ppbv]

Other variables are available in the original HDFEOS files such as information on the surface properties, clouds, atmospheric profiles and radiances, that can be used for further analysis.
Information on all the data available in the .he5 files can be found in appendices A and B of the document: https://www2.acom.ucar.edu/sites/default/files/mopitt/v8_users_guide_201812.pdf

## Python Scripts

Copyright (C) 2018 The HDF Group 
Both scripts are based on the HDF Group example code: http://hdfeos.org/zoo/LaRC/MOP02J-20131129-L2V17.8.3.he5.py
More examples and descriptions on the MOPITT data reading/visualization are available at : http://hdfeos.org/zoo/index_openLaRC_Examples.php#MOPITT

## Requirements for running the scripts : 

For "MOPITT_ECCC_FileConverter.py":
 - To read HDFEOS files (.he5), the h5py library is needed : conda install h5py
 - To access the OpenDap database, the urllib library is needed

For "MOPITT_ECCC_SelectCanada.py":
 - To visualize the data with this code, the Basemap python library is needed : conda install basemap. This Matplotlib module is used to visualize the data on a world map. 






