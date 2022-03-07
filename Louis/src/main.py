from csv import list_dialects
from distutils.filelist import findall
from email.headerregistry import ParameterizedMIMEHeader
from operator import index
from turtle import position
import pdftotext
import myClass as mc
import re
import complet as c

tmp = c.dossier()
dire = tmp[0]
listFile = tmp[1]

for nomFichier in listFile :
	print(nomFichier)

	#______________________________________________________________________________________________________________
	header = mc.Header()

	header.nomFichier = nomFichier

	with open("../Corpus_2021/"+header.nomFichier,"rb") as f :
		fichierComplet = pdftotext.PDF(f)
		#fichierComplet est un tableau où chaque éléments est une string du contenu d'une page du pdf


	premierePage = fichierComplet[0].split("\n") #besoin premiere page pas du reste ici

	#______________________________________________________________________________________________________________
	#RECHERCHE AUTEUR
	tabEntete = premierePage[:10] #permet de n'avoir que l'entête sous forme de tableau
	entete = "\n".join(tabEntete) #idem sous forme de str


	#Recherche du/des auteur(s) et du titre si les fichiers sont nommés selon l'un de leurs auteurs
	tabEnteteMajuscule = entete.upper().split('\n')

	#Boucle permettant de trouver l'auteur
	auteurFind=False #l'auteur n'a pas été trouvé
	indexAuteur = 0

	for ligne in tabEnteteMajuscule : #recherhce de l'auteur
		if ligne.find(header.nomFichier.upper()[:4]) !=-1 and not auteurFind :
			auteurs = tabEntete[tabEnteteMajuscule.index(ligne)]
			indexAuteur = tabEnteteMajuscule.index(ligne)
			auteurFind = True
		

	if isinstance(auteurs,str) : #mise en forme de la liste du ou des auteurs si cette liste est sous forme de string

		#on remplace tout les symboles entre crochet ci dessous par un symbole unique inusité dans un nom ou un prénom
		#puis on split en fonction de ce symbole
		for i in [',','and','∗','\\','[','(',')','1st','2nd','3rd','4rd','1','2','\n','*'] :
			while auteurs.find(i)!=-1 :
				auteurs = auteurs[:auteurs.find(i)] + "¤" + auteurs[auteurs.find(i)+len(i):]
		auteurs = auteurs.split('¤')

		#si jamais la séparation précédente se faisait par une série d'espaces
		if len(auteurs)==1 and auteurs[0].find('     ') != -1 :
			auteurs = auteurs[0].split('     ')
		
		#On enlève les espaces superflux entre les noms et prénoms
		parcours = 0
		for parcours in range(len(auteurs)):
			tmpInt = auteurs[parcours].find('  ')
			while tmpInt != -1 :
				auteurs[parcours] = auteurs[parcours][:tmpInt] + auteurs[parcours][tmpInt+1:]
				tmpInt = auteurs[parcours].find('  ')
			parcours+=1
		

		parcours = 0
		while parcours < len(auteurs) :
			if len(auteurs[parcours]) < 3 or auteurs[parcours] == ' '*len(auteurs[parcours]):
				del auteurs[parcours]
				parcours = parcours-1
			else : 
				while auteurs[parcours][0] == ' ' :
					auteurs[parcours] = auteurs[parcours][1:]
			parcours+=1
	if auteurs[0].count(' ') > 6 :
		tmpStr, tmpChar, tmpBool, auteurs, i = auteurs[0], '', False, [], 0
		while i in range(len(tmpStr)) :
			tmpChar = tmpStr[i]
			if ( tmpChar == ' ' and tmpBool ) or i == tmpStr[-1]:
				if len(auteurs) == 0 or len(auteurs[-1]) > 2 :
					
					auteurs.append(tmpStr[:i])
					i,tmpStr = i-len(tmpStr[:i]) , tmpStr[i+1:]
					tmpBool = False
			elif tmpChar == ' ' : 
				tmpBool = True
			i+=1

	header.auteur=auteurs

	#______________________________________________________________________________________________________________
	#SEPARATION DES COLONNES
	for i in range(len(premierePage)) :
		if premierePage[i].find(" "*4)!=-1 : #on cherche 4 espaces et l'on considère qu'il y a 2 colonnes a ce moment
			a = premierePage[i].count(' ')
			space=""
			j = premierePage[i].find(" "*4) 
			while premierePage[i][j+1] == " " : #tant que le caractère suivant est un espaces
				space+=" " #ajoute un espace à une string ne contenant que des espaces
				j+=1
			premierePage[i] = premierePage[i].split(space) 
			
			if a - premierePage[i][-1].count(' ') > 10 and i > 5: #pour garde l'entète à sa place
				premierePage[i][-1] = "§" + premierePage[i][-1] #ajout d'un caractère splécial pour détecter la colonne de droite
			elif i>5 : 
				premierePage[i] = ' '.join(premierePage[i])

		elif premierePage[i].find("   ") != -1:
			premierePage[i] = premierePage[i].split("   ")
			premierePage[i][-1] = "§" + premierePage[i][-1]

		elif premierePage[i].find("  ") != -1:
			premierePage[i] = premierePage[i].split("  ")
			premierePage[i][-1] = "§" + premierePage[i][-1]
		

	#-------------
	#replacer l'entete correctement
	i = 0
	while i<len(premierePage) :
		element = premierePage[i]
		if not isinstance(element,str) :
			while element.count('')!=0 :#enlever les elements vides de la liste
				del element[element.index('')]
		i+=1

	for j in range(len(premierePage)-1) : #cas un peu trop particulier de Nasr
		i=premierePage[j]
		if not isinstance(i,str) and len(i)==3 and i[-1][0]=='§' and len(i[0])-len(i[-1]) >= len(i[2]) :
			premierePage[j][1] = i[-2] + i[-1][1:]
			del premierePage[j][-1]

	#______________________________________________________________________________________________________________
	#TRAITEMENT POUR EXTRAIRE LA COLONNE DE GAUCHE
	tmpG = []
	for i in premierePage:
		if isinstance(i,str) : #si c'est une string pure
			if len(i)>=1 and i[0]!="§" :
				tmpG.append(i)
		else : 
			if i[0][0]!="§" and len(i)!=3: #si l'élément en question n'est pas dans la colonne de droite et ...
				tmpG.append(i[0])
			elif i[0][0]!="§" :
				tmpG.append(i[0]+i[1])

	#______________________________________________________________________________________________________________
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


	premierePage = "\n".join(tmpG) + '\n' + "\n".join(tmpD) #Création d'une string contenant la colonne de gauche puis celle de droite
	#print(premierePage)

	#______________________________________________________________________________________________________________
	#RECHERCHE AVEC LES REGEX DE LA PARTIE INTRODUCTION 
	x = re.search("\n *(I|1)\.* *(Introduction|INTRODUCTION|I NTRODUCTION)",premierePage)
	if x :
		premierePage = premierePage.split(premierePage[x.span()[0]:x.span()[1]])
	else :
		print("erreur pas trouvé")


	#______________________________________________________________________________________________________________
	#RECHERCHE TITRE

	tabEntete =  premierePage[0].split("\n") #permet d'avoir que l'entête sous forme de tableau
	entete = premierePage[0] #permet de n'avoir que l'entête sous forme de str
	tabEnteteMajuscule = entete.upper().split('\n')
	
	#for i in premierePage :
	#	print(i)

	header.titreArticle = "\n\t".join(tabEntete[:indexAuteur])


	#______________________________________________________________________________________________________________
	#RECHERHCE DE L'ABSTRACT PUIS AJOUT À L'INSTANCE DE L'OBJET DE TYPE HEADER
	index = 0
	for i in range(len(tabEnteteMajuscule)) :
		if tabEnteteMajuscule[i].find("ABSTRACT") != -1 :
			index = i+1
			break
	if len(tabEntete[i]) > 9 :
		ligneAbstract = tabEntete[i][10:]
		while ligneAbstract[0] == '.' or ligneAbstract[0] == ' ' or ligneAbstract[0] == '-' :
			ligneAbstract = ligneAbstract [1:]
		header.abstract = '  ' + ligneAbstract + '\n\t' + '\n\t'.join(tabEntete[index:])
	else : 
		header.abstract = '\n\t'.join(tabEntete[index:])


	c.Sortie(dire,nomFichier,header.to_string())
