##Seoul Bike Prediction ESILV Project - Python for data analysis course 2020

Theo ZANGATO , Youssef ZEMALI

## Objectif/Résumé

Le but de ce projet est de prédire le nombre de vélos loués à Séoul pendant un certain jours. 
Pour cela, un jeu de données contenant le nombre de vélos publics loués à chaque heure à Séoul nous est fourni. 
Le dataset est disponible ici : https://archive.ics.uci.edu/ml/datasets/Seoul+Bike+Sharing+Demand

Il s'agit d'un problème de régression. Nous avons d'abord explorer les données puis nous 
les avons visualiser afin de distinguer des comportements particuliers.
Nous avons ensuite préparer les datas en les nettoyant et ajoutant certains features.
Ensuite, nous avons pu utiliser différents modèles que nous avons optimisé.
Enfin, nous avons exposé notre modèle via une API Rest Django.

Pour avoir, les détails de notre démarche, merci de vous référer au fichier Project.ipynb .

## Technologies

Python 3.8
Django, Jupyter Notebook
pandas, numpy, scikit-learn, keras, matplotlib, joblib

## Utilisation de l'API: 

Tout d'abord, il faut lancer l'API Django : 

❯ cd /pathtoproject/SeoulAPI

❯ python manage.py runserver

Maintenant, vous pouvez vous rendre sur Postman Agent pour requeter l'API : 

Récupérer les données rentrée par des utilisateurs :
GET  avec http://127.0.0.1:8000/locations/

Récupérer une location précise:
GET  avec http://127.0.0.1:8000/location/1/   

Prédire le nombre de location avec des données d'entrée:

POST avec http://127.0.0.1:8000/predict/  et le JSON suivant par exemple que vous pouvez modifier :

{"Date":"01-12-2017","RentedBike":null,"Hour":4,"Temperature":-6.0,"Humidity":36,"Windspeed":2.3,"Visibility":2000,"DewPointTemperature":-18.6,"SolarRadiation":0.0,"Rainfall":0.0,"Snowfall":0.0,"Season":"Winter","Holiday":"No Holiday"}

License
