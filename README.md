<p align="center">
    <a href="https://www.asc-csa.gc.ca/eng/satellites/mopitt.asp">
        <img alt="MOPITT" src="https://www.asc-csa.gc.ca/images/satellites/ban-mopitt-span6.jpg" height="300">
    </a>
</p>

- [En Français](#MOPITT-Tutoriel)
- [In English](#MOPITT-Tutorial)

# MOPITT-Tutoriel

## Contexte

MOPITT est un des cinq instruments lancés le 18 décembre 1999 à bord de Terra, un satellite de la National Aeronautics and Space Administration (NASA) qui orbite à 705 km au-dessus de la Terre. C'est Jim Drummond, de l'Université de Toronto (en anglais seulement), qui a conçu MOPITT. Grâce à son équipe scientifique et à l'Agence spatiale canadienne (ASC), M. Drummond a proposé cet instrument à la NASA. La durée initiale de cinq ans de l'expérience a été prolongée en raison de la qualité des informations amassées et du bon fonctionnement du satellite. MOPITT, pour measurements of pollution in the troposphere (instrument de mesure de la pollution dans la troposphère), a été fabriqué par COM DEV International, une entreprise de Cambridge, en Ontario.

Le but de ce tutoriel est de démontrer le processus d'accès à ces données, de les préparer pour l'utilisation, et de montrer quelques analyses et visualisations de données de base en utilisant les données SCISAT. Le tutoriel présente également quelques filtres simples que nous pouvons appliquer aux données pour une exploration plus approfondie.

Ce tutoriel utilise les mesures du monoxyde de carbone dans la troposphère pour analyse.


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
3. Commencez le tutoriel trouvé dans le fichier _mopitt_tutorial.ipynb_. Veuillez noter que les graphiques ne s'affichent pas dans Github, et que vous devrez configurer le projet localement pour les visualiser.

## Modèle de prévision de la concentration d'ozone de MOPITT

En complément à ce tutoriel, vous pouvez trouver une implémentation simple d'un modèle de réseau neuronal prédictif qui utilise les données SCISAT. Le fichier _scisat_mlp.ipynb_ présente un guide, étape par étape, de la création et de l'analyse initiale du modèle.

Veuillez noter que les prédictions et les résultats statistiques contenus dans ce tutoriel n'ont pas fait l'objet d'un examen scientifique par les pairs et ne doivent pas être utilisés à l'appui d'une analyse ou d'une publication scientifique.


# MOPITT-Tutorial

## About

MOPITT is one of five instruments launched December 18, 1999, aboard Terra, a National Aeronautics and Space Administration (NASA) satellite orbiting 705 km above the Earth. It was designed by Jim Drummond of the University of Toronto and, with the help of his science team and the Canadian Space Agency (CSA), prepared for NASA. Initially planned for a five-year term, the experiment has been prolonged because the data collected is still of high quality and the satellite is in good health. MOPITT was manufactured by COM DEV International, of Cambridge, Ontario.

The purpose of this tutorial is to help demonstrate the process of accessing the SCISAT data, preparing it for use, and to show some basic data analysis and visualisation using the SCISAT data. The tutorial also demonstrates some simple filters we can apply to the data for further exploration.

This tutorial uses measurements of carbon monoxide in the troposphere as analysis data.

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
3. Run the tutorial found in the _mopitt_tutorial.ipynb_ file. Please note that the plots do not display in Github, and you will have to set up the project locally in order to view them.

## MOPITT Ozone Concentration Prediction Model

As an addition to this tutorial, you can find a simple implementation of a predictive neural network model that uses SCISAT data. The notebook found in _scisat_mlp.ipynb_ contains a step by step guide of the creation and initial analysis of the model.

Please be advised that the predictions and statistical results contained in this tutorial have not been scientifically peer-reviewed and should not be used to support any scientific analysis or publication.
