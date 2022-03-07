#!usr/bin/python

import sys
import os
import os.path
import shutil

dire = ''

def dossier () :
    #détection de l'entrée (qui doit être un répertoire contenant les fichiers PDF) :
    arg = sys.argv[1]
    if os.path.isdir(arg):
        print ("entrée ok")
        #code
        #détection puis destruction/création du répertoire contenant les fichiers txt :
        dire = os.path.join(arg, "../result") #chemin du dossier à détecter (chemin défini en argument, auquel on ajoute le sous-dossier txt)
        if os.path.isdir(dire):
            print("Le dossier '%s' existant a été remplacé." %dire)
            shutil.rmtree(dire) #efface le répertoire et son contenu
            os.makedirs(dire) #crée un répertoire vide
        else:
            print("Le dossier '%s' a été crée." %dire)
            os.makedirs(dire)
            print(dire)
        return [dire,os.listdir(arg)]
    else : return None


#############################################################################################
#création des fichiers txt :
def Sortie (dire,fic,texte) :
    with open(os.path.join(dire, fic[:-4])+'.txt', "w+") as file :#on crée un fichier ayant pour chemin arg/fic, en enlevant le ".pdf"
        #"w+" indique que l'on crée un fichier ou que l'on écrase le fichier portant le même nom
        file.write(texte)
