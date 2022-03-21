#!usr/bin/python

def SeparationColonne(stringModif):
    for i in range(len(stringModif)) :
        space = ''
        if stringModif[i].find(" "*4)!=-1 : #on cherche 4 espaces et l'on considère qu'il y a 2 colonnes a ce moment
            a = stringModif[i].count(' ')
            j = stringModif[i].find(" "*4)
            while stringModif[i][j+1] == " ": #on cherche le nombre d'espaces
                space+=" "
                j+=1
            stringModif[i] = stringModif[i].split(space) 
            

            if a - stringModif[i][-1].count(' ') > 10 and i > 5: #pour garde l'entète à sa place
                stringModif[i][-1] = "§" + stringModif[i][-1] #ajout d'un caractère spécial pour détecter la colonne de droite
            elif i>5 : 
                stringModif[i] = ' '.join(stringModif[i])

        elif stringModif[i].find("   ") != -1:
            stringModif[i] = stringModif[i].split("   ")
            stringModif[i][-1] = "§" + stringModif[i][-1]

        elif stringModif[i].find("  ") != -1:
            stringModif[i] = stringModif[i].split("  ")
            stringModif[i][-1] = "§" + stringModif[i][-1]


    

    #-------------
    #replacer l'entete correctement
    i = 0
    while i<len(stringModif) :
        element = stringModif[i]
        if not isinstance(element,str) :
            while element.count('')!=0 :#enlever les elements vides de la liste
                del element[element.index('')]
        i+=1


    for j in range(len(stringModif)-1) : #cas un peu trop particulier de Nasr
        i=stringModif[j]
        if not isinstance(i,str) and len(i)==3 and i[-1][0]=='§' and len(i[0])-len(i[-1]) >= len(i[2]) :
            stringModif[j][1] = i[-2] + i[-1][1:]
            del stringModif[j][-1]


       #______________________________________________________________________________________________________________
    #TRAITEMENT POUR EXTRAIRE LA COLONNE DE GAUCHE
    tmpG = []
    for i in stringModif:
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
    for i in stringModif:
        if isinstance(i,str) : #si c'est une string pure
            if len(i)>=1 and i[0]=="§" :
                tmpD.append(i[2:])
        else :
            while i.count('')!=0 :#enlever les elements de la liste qui sont vides
                del i[i.index('')] 
            if i[-1][0]=="§": #si l'élément en question est dans la colonne de droite
                tmpD.append(i[-1][2:])

    return "\n".join(tmpG) + '\n' + "\n".join(tmpD) #Création d'une string contenant la colonne de gauche puis celle de droite
