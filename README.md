# Parseur d'articles scientifiques en format texte
																						
## Antoine ARIBARD, Matthias BRZUSTOWSKI, Louis CART-GRANDJEAN, Arthur CASANOVA

### Fonctionnement du programme :
Le programme analyse le répertoire entré en paramètre, contenant les articles au format PDF à traiter, puis, pour chaque article (demandé en paramètre), génère ce même article, au format TXT ou XML (précisé en ligne de commande).
Pour garder une structure de texte la plus précise selon l'originale,le programme analyse les paragraphes contenues dans le texte, les tabulations, les mot-clés(tel que Abstract par exemple)

### Execution du programme  :

1 - Ouvrir un terminal, puis se placer dans le répertoire contenant le programme python avec la commande suivante : "cd ~/<repertoire>"

2 - Entrer la commande 'chmod a+x script.py'. Celle-ci indique que le programme est un fichier exécutable, et que tous les utilisateurs ont les droits d'exécution.

3 - Entrer la commande 'python3 script.py <chemin d'accès> <-t>/<-x> <articles>. L'argument <chemin d'accès> est l'adresse à laquelle se trouve le répertoire à parser. L'argument <-t>/<-x> permet de spécifier le format des fichiers en sortie : txt ou xml. Le paramètre <articles> permet de spécifier quels sont les articles à sortir au format demandé.
	
Le programme efface puis remplace dans ce répertoire le sous-répertoire nommé 'txt'/'xml' s'il existe déjà, ou le crée sinon. Il va ensuite créer les fichiers txt/xml dans ce sous-dossier. 
	
