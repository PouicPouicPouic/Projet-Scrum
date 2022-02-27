# Parseur d'articles scientifiques en format texte
																								 
## Antoine ARIBARD, Matthias BRZUSTOWSKI, Louis CART-GRANDJEAN, Arthur CASANOVA

### Fonctionnement :

Dans un terminal, se placer dans le répertoire contenant le programme python avec la commande suivante :
'cd ~/repertoire'

Taper ensuite la commande 'chmod a+x script.py'. Celle-ci indique que le programme est un fichier exécutable, et que tous les utilisateurs ont les droits d'exécution.

Puis, taper la commande 'python3 script.py <chemin>'. L'argument <chemin> est l'adresse à laquelle se trouve le répertoire contenant les fichiers PDF.
	
Le programme efface puis remplace dans ce répertoire le sous-dossier nommé 'txt' s'il existe déjà, ou le crée sinon. Il va ensuite créer les fichiers txt dans ce sous-dossier.
