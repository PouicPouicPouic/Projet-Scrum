from turtle import position
import pdftotext
import myClass as mc
import re

nomFichier = "Nasr"

header = mc.Header(nomFichier+".pdf")

with open("../Corpus_2021/"+header.nomFichier,"rb") as f :
	fichierComplet = pdftotext.PDF(f)
	#fichier complet est un tableau où chaque éléments est une string du contenu d'une page du pdf


#MISE EN PAGE DU DEBUT DU PDF (cf. Sprint 2)
premierePageComplete = fichierComplet[0] #besoin premiere page pas du reste ici

premierePageEntete = premierePageComplete.split("Abstract")[0]
premierePage = premierePageComplete.split("Abstract")[1]


#SEPARATION DES COLONNES
premierePage=premierePage.split("\n")


for i in range(len(premierePage)) :
	if premierePage[i].find("    ")!=-1 : 
		space=""
		j = premierePage[i].find("    ") 
		while premierePage[i][j+1] == " " :
			space+=" "
			j+=1
		premierePage[i] = premierePage[i].split(space)
		premierePage[i][-1] = "§" + premierePage[i][-1] #ajout d'un caractère splécial pour détecter la colonne de droite


#TRAITEMENT POUR EXTRAIRE LA COLONNE DE GAUCHE
tmpG = []
for i in premierePage:
	if isinstance(i,str) : #si c'est une string pure
		if len(i)>=1 and i[0]!="§" :
			tmpG.append(i)
	else :
		while i.count('')!=0 :#enlever les elements de la liste qui sont vides
			del i[i.index('')] 
		if i[0][0]!="§" and len(i)!=3: #si l'élément en question n'est pas dans la colonne de droite et ...
			tmpG.append(i[0])
		elif i[0][0]!="§" :
			tmpG.append(i[0]+i[1])

#TRAITEMENT POUR EXTRAIRE LA COLONNE DE DROITE
tmpD = []
for i in premierePage:
	if isinstance(i,str) : #si c'est une string pure
		if len(i)>=1 and i[0]=="§" :
			tmpD.append(i[2:])
	else :
		while i.count('')!=0 :#enlever les elements de la liste qui sont vides
			del i[i.index('')] 
		if i[-1][0]=="§": #si l'élément en question est dans la colonne de droite
			tmpD.append(i[-1][2:])


premierePage = "\n".join(tmpG) + '\n' + "\n".join(tmpD)

print(premierePage)

#RECHERCHE AVEC LES REGEX DE LA PARTIE INTRODUCTION 
x = re.search("\n(I|1)\.*( |I|V|X)*(Introduction|INTRODUCTION|I NTRODUCTION)",premierePage)
if x :
	premierePage = premierePage.split(premierePage[x.span()[0]:x.span()[1]])
else :
	print(x)

header.abstract = premierePage[0]

titreAuteur = premierePageEntete.split('\n')[0:3]
for i in range(len(titreAuteur)):
	while titreAuteur[i][0] == ' ':
		titreAuteur[i] = titreAuteur[i][1:]

print("\n\n--------\n\n")
print(header.toStringTxt())