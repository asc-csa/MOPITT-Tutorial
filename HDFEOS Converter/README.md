- [Français](#MOPITT-Tutoriel)
- [English](#MOPITT-Tutorial)
# MOPITT-Tutorial

## About

This section gives the code to filter and to convert MOPITT data from HDFEOS (.he5) to CSV, as well as visualize the results. The scripts were written for the CSA Open Data website. 

The python script "MOPITTData_FileConverter.py" filters the data to select the needed variables, and converts it in CSV files.
The script "MOPITTData_ReaderAndVisualization.py" reads the CSV files and outputs an exemple of data visualization.

## Quick Start

1.	Setup a virtual environment or conda environment with the following version of python
```
python = 3.8
```
2.  Install requirements from the requirements.txt file 
```
pip install -r requirements.txt
```
or 
```
conda install -c conda-forge --file requirements.txt
```

## Convert MOPITT Data 

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


# MOPITT-Tutoriel

## Contexte

Cette section présente le code pour filtrer et convertir les fichier HDFEOS (.he5) en fichier CSV, et pour visualiser les données MOPITT, développés pour le site de données ouvertes de l'ASC.

Le script python "MOPITTData_FileConverter.py" traite les données et sélectionne les variables voulues dans le tableau, pour ensuite les convertir en fichiers de type CSV. 
Le script "MOPITTData_ReaderAndVisualization.py" lit les fichiers CSV et sort un exemple de visualisation.

## Démarrage rapide

1.	Configurez un environnement virtuel ou un environnement conda avec la version suivante de python
```
python = 3.8
```
2.  Installez les exigences à partir du fichier requirements.txt 
```
pip install -r requirements.txt
```
ou 
```
conda install -c conda-forge --file requirements.txt
```

## Convertor les données MOPITT 

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
