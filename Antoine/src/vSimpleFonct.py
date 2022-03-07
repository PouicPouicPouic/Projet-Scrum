import string
from tkinter.ttk import Separator
from tokenize import String
import pdftotext

nomFichier = "Torres"
with open("../Corpus_2021/"+nomFichier+".pdf","rb") as f :
    pdf = pdftotext.PDF(f)

a = pdf[0].split("\n")

#SEPARATION DES COLONNES

for i in range(len(a)) :
    
    if a[i].find("    ")!=-1 : #si on trouve 4 espaces de suite
        space=""
        j = a[i].find("    ") #trouver indice des 4 espaces
        
        while a[i][j+1] == " " : #nombre total espaces
            space+=" "
            j+=1
        a[i] = a[i].split(space) #split selon le nombre espace

for i in a :
    print(i,"\n")

#ECRITURE FICHIER SORTIE FORMAT TXT
with open("../result/"+nomFichier+".txt","w") as fichier :
    sortie =""
    
    for i in a :
        if len(i) == 2 : #detecte les lignes "classiques"
            
            if len(i[0])==1 : #quand la premiere lettre est grande (cf Torres Introduction "T")
                sortie+=i[0]+i[1][1:]+"\n" #on prends la maj et on prends pas l'espace au début de la case suivante
            else :
                sortie+=i[0]+"\n"#On ajoute juste la ligne
        
        elif isinstance(i,str) : #quand la case ne contien qu'une string (cf : Torres : "The research is carried out using a new content-based")
            sortie+=i+"\n"
        
    fichier.write(sortie)




#tableau au nom chapitre Jing-cutepaste et torres causer par la sep au espaces



"""
    ['', ' summaries is an arduous and costly process, a body of'] 

    ['', ' I. I NTRODUCTION', '        research has been produced in the last decade on automatic'] 2 COLONNES

    ['', ' content-based evaluation procedures. Early studies used text'] 

    ['T', ' EXT summarization evaluation has always been a'] COLONNE GAUCHE

    ['', ' complex and controversial issue in computational'] COLONNE GAUCHE

    linguistics. In the last decade, significant advances have been  COLONNE GAUCHE

    ['', ' similarity measures such as cosine similarity (with or without'] 

    ['', ' weighting schema) to compare peer and model summaries'] 

    ['', ' [5]. Various vocabulary overlap measures such as n-grams'] 

    ['made in this field as well as various evaluation measures have', ' overlap or longest common subsequence between peer and'] 2 COLONNES
"""