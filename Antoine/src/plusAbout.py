import pdftotext
import re

nomFichier = "jing-cutepaste"
with open("../Corpus_2021/"+nomFichier+".pdf","rb") as f :
    pdf = pdftotext.PDF(f)

#EXTRACTION ENTETE
if pdf[0].find("Abstract") != -1 :
    page1 = pdf[0].split("Abstract")

    #TRAITEMENT ENTETE
    page1[0] = page1[0].split("\n")
    for i in range(len(page1[0])) :
        while page1[0][i][0]==" " :
            if len(page1[0][i])==1 :
                break
            page1[0][i] = page1[0][i][1:]
    for i in range(len(page1[0])) :
        if page1[0][i] == " " :
            del page1[0][i]

    #RESULTAT ENTETE
    page1[0] = "\n".join(page1[0])

#TRAITEMENT PREMIERE PAGE
    a = page1[1].split("\n")

    for i in range(len(a)) :
        if a[i].find("    ")!=-1 : 
            space=""
            j = a[i].find("    ") 
            
            while a[i][j+1] == " " :
                space+=" "
                j+=1
            a[i] = a[i].split(space)

    #TRAITEMENT COLONNE GAUCHE
    b = []
    for i in a :
        if len(i)>=2 and i[0] != '':
            if isinstance(i,str) :
                b.append(i)
            elif len(i[0])==1 :
                b.append("\n"+i[0]+" "+i[1][1:]+"\n")
            else :
                b.append(i[0])

    page1[1] = "\n".join(b)

    #TRAITEMENT COLONNE DROITE
    b=[]
    for i in a :
        if len(i)>2 and re.search("[0-9]",i[0]) :
            j=0
            while j < len(i) :
                if j > len(i) : break
                elif i[j] == '' : del i[j]
                else : j+=1
            i[0] = ''.join(i[0:2])
            del i[1]
        elif len(i)>2 : print(i)
        if len(i)>=2 and i[1] != '':
            if isinstance(i,str) :
                b.append(i)
            elif len(i[1])==1 :
                b.append("\n"+i[1]+" "+i[2][1:]+"\n")
            else :
                b.append(i[1])

    page1[1] +="\n" + "\n".join(b)

#RECHERCHE AVEC LES REGEX DES PARTIE ("INTRODUCTION")
    for i in page1 :
        x = re.search("\.\n+ *[0-9]+ +[A-Z]",i)
        if x :
            print(x.span())
            y = x.span()
            print(i[y[0]+2:y[1]])

#SAUVEGARDE DANS FICHIER TEXTE
    with open("../result/"+nomFichier+".txt","w") as fichier :
        sortie = "\n\n\n".join(page1)
        fichier.write(sortie)