#!usr/bin/python

import sys
#sys.argv donne une liste d'arguments de type chaine de caractères par défaut
import os
import os.path
import shutil

##########################################################################################################################################################################################
##########################################################################################################################################################################################

arg2 = '' #format
try :
    arg2 = sys.argv[2]
except IndexError :
    arg2 = '-t'

arg3 ='' #format
try :
    arg3 = sys.argv[3]
except IndexError :
    if arg2 == '-t' :       arg3 = '-t'
    elif arg2 == '-x' :     arg3 = '-x'
    else :                  arg3 = arg3
	
arg4 ='' #index de l'interface contenant une liste de textes
try :
    arg4 = sys.argv[4]
    arg4 = arg4.split(',') #arg4[i] avec une boucle for-each ne fonctionne pas
except IndexError :
    arg4 = 'all'
    #arg4 = 'all' : le programme s'exécute pour tout le contenu du répertoire
    #sinon, on liste le numéro des fichiers présents dans le répertoire, et que l'on veut convertir en .pdf / .xml (séparés par des virgules et sans espaces)

if not ( arg2 in ['-t','-x'] and arg3 in ['-t','-x'] ):
	#renvoie une exception + un message
    print('Exception :\n\tLes arguments doivent être "-t" et/ou "-x". Les arguments étaient : {}'.format(arg2),format(arg3))
else :

    #détection de l'entrée (qui doit être un répertoire contenant les fichiers PDF) :
    arg1 = sys.argv[1] #argument qui contient le chemin du répertoire contenant les fichiers PDF

    if os.path.isdir(arg1):
        print ("entrée ok")
        textes = os.listdir(arg1) #liste contenant les noms des fichiers contenus dans le répertoire passé en argument 1
        if arg4 != 'all' : #filtre les fichiers à convertir selon ce qui est indiqué par arg4
            n = 0 
            while n < len(arg4-1) : #indique le nombre d'éléments à analyser (si on considère qu'il n'y a pas de doublons dans arg4)
##########################################################################################################################################################################################
		#si le programme écrase le répertoire passé en arg1, tous les fichiers non inclus dans arg4 (et donc que l'on ne souhaite pas parser) seront déruits.
		#si le programme crée un sous-dossier/sur-dossier dans lequel on copie le répertoire dans arg1, alors tout va bien. 
##########################################################################################################################################################################################

                filtre = []
                filtre.append(textes[arg4[n]]) #fonctionne si arg4 est considéré comme un int, pas si il est considéré comme une str /!\
                textes = filtre
		n = n+1
##########################################################################################################################################################################################
		#fin de la partie à tester (liste filtre + si besoin modifier les lignes 111 à 118)
##########################################################################################################################################################################################

        #détection de l'entrée, qui doit être le chemin d'un répertoire :
        dire = os.path.join(arg1, "../result")
        #destruction/création du répertoire contenant les fichiers .txt et/ou .xml :
        if os.path.isdir(dire):
            print("Le dossier '%s' existant a été remplacé." %dire)
            shutil.rmtree(dire) #efface le répertoire et son contenu
            os.makedirs(dire) #crée un répertoire vide
        else:
            print("Le dossier '%s' a été crée." %dire)
            os.makedirs(dire)
        
##########################################################################################################################################################################################

    #détection de l'entrée (dans le cas où il s'agit d'un fichier PDF) :
    elif os.path.isfile(arg1) and arg1[-4:] == '.pdf' :
        print("entrée pdf")
        i = -1
        while arg1[i] != '/' :
            i-=1
        textes = arg1[i+1:] #textes doit contenir le nom du fichier, pas son chemin
        
        #détection du répertoire contenant arg1 :
        dire = os.path.join(arg1[:i+1], "../result")
        #destruction/création du répertoire contenant les fichiers .txt et/ou .xml :
        if os.path.isdir(dire):
            print("Le dossier '%s' existant a été remplacé." %dire)
            shutil.rmtree(dire) #efface le répertoire et son contenu
            os.makedirs(dire) #crée un répertoire vide
        else:
            print("Le dossier '%s' a été crée." %dire)
            os.makedirs(dire)

##########################################################################################################################################################################################
 #nous rendons possible la création d'un fichier de chaque type (.txt et .xml), si les formats spécifiés en entrée le demandent
##########################################################################################################################################################################################

    #détection du format texte spécifié en entrée (-t) :


    #par défaut si aucun paramètre n'est défini par l'utilisateur, le retour sera un fichier .txt
    if arg2 == '-t' or arg3 == '-t' :
        #une chaîne de caractères vide est considérée comme False
        #par défaut, si aucun paramètre définissant le format n'est spécifié, le format de sortie sera en .txt

##########################################################################################################################################################################################

    #création des fichiers txt (si arg2 ou arg3 prend la valeur '-t') :
        for fic in textes : #on parcourt la liste des fichiers pdf
        
            if fic[-4:] == '.pdf' : #équivalent fonction glob
                file = open(os.path.join(dire, fic[:-4]+'.txt'), "w+") #création du fichier .txt
                #on enlève '.pdf' à la fin du nom du fichier puis on ajoute '.txt'
                #"w+" signifie que l'on remplace le fichier ayant le même nom s'il existe, et le crée le cas échéant
                
                #traitement
                file.write("""texte traité""")
                file.close()
            
            
##########################################################################################################################################################################################
##########################################################################################################################################################################################

    #détection du format texte spécifié en entrée (-x) :
    if arg2 == '-x' or arg3 == '-x' :
        #aucune nécessité de mettre un ou-exclusif, si l'utilisateur saisit deux fois le même format en entrée il ne créera qu'un seul document
            
##########################################################################################################################################################################################

    #création des fichiers XML (si arg2 ou arg3 prend la valeur '-x') :
        for fic in textes :
            if fic[-4:] == '.pdf' :
                file = open(os.path.join(dire, fic[:-4]+'.xml'), "w+") #création du fichier .xml
                
                #traitement
                file.write("""texte traité""")
                file.close()

##########################################################################################################################################################################################
##########################################################################################################################################################################################
