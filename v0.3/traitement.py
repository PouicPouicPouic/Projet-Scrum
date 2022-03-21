import pdftotext
import myClass as mc
import re
import method as m
from unidecode import unidecode

def Traitement(nomFichier) :
	print(nomFichier)

	#______________________________________________________________________________________________________________
	header = mc.Header(nomFichier)

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
	indexAuteur,indexMail = 0,''

	for currentIndex in range(len(tabEnteteMajuscule)) : #recherhce de l'auteur

		ligneMaj = tabEnteteMajuscule[currentIndex]
		ligneMin = tabEntete[currentIndex]

		if ligneMaj.find(header.nomFichier.upper()[:4]) !=-1 and not auteurFind :
			auteurs = tabEntete[tabEnteteMajuscule.index(ligneMaj)]
			indexAuteur = tabEnteteMajuscule.index(ligneMaj)
			auteurFind = True
		
		#Traitement pour avoir tous les emails en entier et utilisables pour la suite
		if ligneMin.find('@') !=-1: #recherche des emails
			indexMail += ligneMin

			if indexMail[-1] in ['-','.'] : #si email sur 2 lignes
				tmp = tabEntete[currentIndex+1]
				indexMail+=tmp

			while indexMail[0] == ' ' :
				indexMail = indexMail[1:]

			premierElement = indexMail[0]
			
			if premierElement == '@' : #si on à pas le début de l'adresse mail
				tmpStr = tabEntete[currentIndex-1] #prendre ligne precedente

				while tmpStr[0] == ' ' :#enlever els espaces au debut
					tmpStr = tmpStr[1:]

				tmpStr = tmpStr[1:-1].split(',')#split seon les vigules (inexistantes dans les adresses mails)
				arrobase,indexMail = indexMail,[]


				for i in tmpStr :
					indexMail.append(i + arrobase) #on assemble les parties des adresses

			elif premierElement == "{" : #si les débuts des adresses mails sont entre des crochets et que l'@ et après hors des crochet

				indexMail = indexMail.split('@')
				indexMail[1] = '@' + indexMail[1]

				tmpStr = indexMail[0][1:-1].split(',') #on enlève les crochets et on sépare les premieres parties
				arobase = indexMail[1]
				indexMail = []
				for i in tmpStr :
					indexMail.append(i + arrobase) #on assemble les parties des l'adresse
		

	#TRAITEMENT EMAIL	
	if isinstance(indexMail,str) :
		mail = indexMail.split(' ')#beacoup d'éléments vides dans la liste des mails
	else : 
		mail = indexMail
	i = 0
	while i in range(len(mail)) :
		element = mail[i] 
		if element == '' or element.find('@')==-1:
			del mail[i] #enlève ces éléments vides
			i-=1
		i+=1
	header.mail=mail

	#TRAITEMENT AUTEURS
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


	###### Liaison des mails aves les auteurs correspondants (mise au même index que l'auteur correspondant)

	nomAut,prenomAut = [],[] #avoir 2 listes l'un pour les noms et l'autre les prénoms des auteurs

	for i in auteurs : #on met en forme nom et prénom (comme les "Le Roux")
		i = i .split(' ')

		try : #permet d'enelever les éléments vides de la liste
			del i[i.index('')]
		except ValueError : #except obligatoire apres try
			i = i

		if len(i) >= 3 : #on remet les morceaux de nom de famille ensemble (Le Roux)
			i[1] = ' '.join(i[1:]) #on remplace le 2eme élément de la lsite par une string des derniers éléments éléments

		nomAut.append(unidecode(i[1].upper())) #liste des noms des auteurs sous la forme de majuscules avec aucun accent
		prenomAut.append(unidecode(i[0].upper())) #liste des prénoms des auteurs sous la forme de majuscules avec aucun accent

	if len(mail) != 0 : #si les mails ont été trouvés
		mailOrdo = ['']*len(mail) #collections de la même longueur que mail

		for j in range(len(mail)) :
			element = mail[j].upper() #mail sous forme majuscule

			for i in range(len(nomAut)) :

				if element.find(nomAut[i]) != -1 : #si nom trouvé
					mailOrdo[i] = mail[j]
				elif element.find(prenomAut[i]) !=-1 : #si prénom trouvé et pas le nom
					mailOrdo[i] = mail[j]

		header.mail = mailOrdo  #on enregistre les mails ordonnés dans l'objet header
	else :
		print('conditions pas respectées')

	premierePage = m.SeparationColonne(premierePage)



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



	#______________________________________________________________________________________________________________
	#RECHERCHE BIBLIO
	
	
	i,a = -1,[]
	dernierePage = fichierComplet[i]

	x = re.search('\n *References *\n',fichierComplet[-1]) #Recherche partie References

	while not (x) and i > -len(fichierComplet): #remonte les pages jusqu'à trouver le titre de la partie References
		a.append(i)
		i-=1
		x = re.search('\n? *References *\n?',fichierComplet[i])

	a.append(i)
	if len(a) != len(fichierComplet) : #simple colonnes
		sortie=[]

		for i in a : #parcours pour trouver le debut de la partie References
			if i == a[-1]:
				sortie.append(fichierComplet[i].split('References')[-1]) 
			else :
				sortie.append(fichierComplet[i])

		sortie.reverse()#les lignes sont insérer dans l'odre inverse, l'ordre est inversé ici
		final=[]

		############# Supression des éléments vides
		for i in sortie :
			splitedPage = i.split('\n')
			j = 0

			while j < len(splitedPage) :		
				element = splitedPage[j]
				if element == '' :
					del splitedPage[j]
					j-=1
				else :
					splitedPage[j] = '\t' + element
				j+=1
			final.append('\n'.join(splitedPage))
			
		header.biblio = '\n'.join(final) #ajout à l'objet header

	else : #double colonnes
		i,a = -1,[]
		dernierePage = fichierComplet[i]
		x = re.search(' *(R ?eferences|R ?EFERENCES) *',fichierComplet[-1])
		while not (x) and i > -len(fichierComplet):
			a.append(i)
			i-=1
			x = re.search(" *(R ?eferences|R ?EFERENCES) *",fichierComplet[i])
		a.append(i)

	return header