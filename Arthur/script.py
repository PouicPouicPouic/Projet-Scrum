#!usr/bin/python

import sys
print(sys.argv) #sys.argv donne une liste d'arguments de type chaine de caractères par défaut
#à ajouter au début du programme
import os
import os.path
import shutil

#############################################################################################

#variables de type STR :

a = sys.argv[0] #peu importe l'entrée, renvoie le nom de ce fichier
print(a)

a = sys.argv[1] #renvoie l'entrée numéro 1
print(a)

a = sys.argv[2] #renvoie l'entrée numéro 2
print(a)

#variable de type autre que STR (int par exemple) :
    
a = int(sys.argv[3])
print(a)

#############################################################################################

#utilisation de main (pas obligatoire):
    
def main() :
    print("main")
    
#obligatoire :
if __name__ == "__main__":
    main()
    
#############################################################################################

#détection de l'entrée (qui doit être un répertoire contenant les fichiers PDF) :
arg = sys.argv[1]
if os.path.isdir(arg):
    print ("entrée ok")
    #code
    #détection puis destruction/création du répertoire contenant les fichiers txt :
    dire = os.path.join(arg, "txt") #chemin du dossier à détecter (chemin défini en argument, auquel on ajoute le sous-dossier txt)
    if os.path.isdir(dire):
        print("Le dossier '%s' existant a été remplacé." %dire)
        shutil.rmtree(dire) #efface le répertoire et son contenu
        os.makedirs(dire) #crée un répertoire vide
    else:
       print("Le dossier '%s' a été crée." %dire)
       os.makedirs(dire)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            