# [commet game](https://github.com/flavien-hugs/commet)
Mini jeu en 2D avec le module Pygame : commet game est un mini jeu inspiré du tutoriel de la plateforme youtube graven. Un jeu de guerre qui consiste à tuer les envahisseurs.

![[commet](https://github.com/flavien-hugs/commet)](https://img.shields.io/badge/unsta-live--demo-orange.svg?style=flat)
![The MIT License](http://img.shields.io/badge/License-MIT-green.svg?style=flat)

### Tester
------------

Avant toutes choses assurer vous que vous avez installer le module suivant sous votre machine. Le code a été écrit sous python 3.

	- créer un environnement virtuel et install le module pygame

Télécharger ou cloner le projet ensuite rendez vous dans le dossier
du projet et ouvrer votre invite de commande et faites :

	- python start.py pour lancer le jeu.

### Contribuer
------------

Faites un fork du projet. Ajouter vos modifications et faites moi un
pull request.

### DOCUMENTATION DU JEU
------------
    - PARAMETRES DU JEU :
        - Les dimensions en pixels de la fenêtre du jeu sont définies par les valeurs  des variables WIDTH et HEIGHT.
            - La variable 'VTS' définit le nombre de fois que l'affichage est
                redessiné chaque seconde.
            - Les variables 'BACKGROUNG_IMG et USER_IMG' stockent les images ajoutées dans le jeu.
            - La chaîne de caractères de la variable TITLE représente la barre de titre de
                la fenêtre du jeu.
              
        - INITIALISATION DU JEU
            - Pygame est initialisé en utilisant les paramètres du jeu définis ci-avant.
            
        - BOUCLE DU JEU
            Les instructions qui figurent dans la boucle while sont répétées (au maximum) VTS fois par seconde, et
            incluent obligatoirement :
            - La gestion de l'événement pour fermer le jeu quand l'utilisateur ferme la fenêtre,
            - la mise à jour de l'affichage du jeu

### Credit
------------

Code repris de graven - le compte youtube graven.

Twitter : [flavien-hugs](https://twitter.com/flavien_hugs)