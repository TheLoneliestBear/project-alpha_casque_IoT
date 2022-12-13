# Casque Secouriste Alpha

## Description
Le but de ce projet est de concevoir un prototype de casque de secouriste qui va procurer à son utilisateur de nombreuses informations pour diverses situations. Ce casque pourra détecter certaines variables de l'environnement pouvant présenter un danger pour son utilisateur et, ainsi, le notifier lui ainsi que son équipe de ses dangers. À cette fin, le prototype Alpha est mis en place pour tester certaines des fonctionnalitées du casque. 
Alpha utilise les technologies du Raspberrypi ainsi que le kit de capteurs et d'effecteurs devellopé par SunFounder pour RBPi afin de se conformer au principe IOT (se référer à ce lien pour en connaitre d'avantage sur IOT : https://en.wikipedia.org/wiki/Internet_of_things)

## Installation
Se réferer aux liens suivant pour proceder aux branchements des capteurs et effecteurs du Raspberrypi : https://www.sunfounder.com/collections/modules

[Suivre les étapes de l'onglet "Protocole expérimental"]

## Utilisation
Une fois installé en suivant les directives de l'onglet "Protocole experimental", le prototype peut être testé de la manière suivante :

- Rapprocher une source lumineuse du capteur de lumière (Photoresistor), puis observer les données de la prochaine itération
- Eloigner la source de lumière ou la cacher de manière à assombrir la piece, puis observer les données de la prochaine itération
- Rapprocher/eloigner l'objet qui fait face au capteur d'ultrasons | faire pivoter l'objet connecté au complet, puis observer les données de la prochaine itération
- Laisser reposer l'objet connecté sans interférence par rapport au capteur d'ultrasons pendant plus de 50 secondes.

Les données collectées par l'objet connecté sont affichés dans la console de l'IDE à chaque fois qu'une itération est enregistrée dans la base de donnée

## Protocole expérimental
Voici comment reproduire les tests effectués dans le video attaché au projet

Il est important de noter que le comportement du prototype alpha est influencé par la lumière ambiante ainsi que la proximitée des objets aux alentours (qui seraient détectés par le capteur d'ultrasons)

1- Effectuer les branchements des capteurs/effecteurs (se réferer au fichier Fritzing)
2- Proceder à l'installation de sqlite3 (se réferer au lien suivant : https://pimylifeup.com/raspberry-pi-sqlite/)
3- Creer une base de donnée nommée alpha.db
4- Executer le fichier alpha.py à partir de l'IDE natif (Thonny) du Raspberrypi
5- Verifier que chaque Iteration est bien enregistrée dans une seance à l'aide de la console de Thonny.
6- Manipuler l'objet connecté en suivant l'onglet "Utilisation"
7- Verifier que les enregistrement ont bien été effectué dans la base de donnée alpha.db (par invite de commande ou interface graphique)

## Vidéo
Voici une vidéo démontrant le fonctionnement du prototype
URL : 

## Support
Coordonnées : 1750956@crosemont.qc.ca

## À venir
Complexification des objets ainsi que du détail de la base de donnée. Implémentation de fonctionnalitées permettant de monitorer les données en temps reel et ce, à partir d'un ordinateur distant.

## Contribution
Le projet a été effectué dans le cadre du cours 420-G74-RO OBJETS CONNECTÉS, les contributions ne seront ainsi pas nécessaires.

## Auteurs et remerciements
Auteurs : Beauchamps Jefferson, Elies Boudida.
Remerciements spéciaux à Anne-Marie Burns pour avoir proposé un modèle de projet duquel ce projet est basé ainsi que pour l'assistance dont elle nous a fait part.

## Licence
L'utilisation du prototype alpha est libre de droits et gratuite. La modification du code est égallement permise

## Statut du projet
Complété - remis pour évaluation
