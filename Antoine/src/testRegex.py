import pdftotext
import re

nomFichier = "jing-cutepaste"
with open("../Corpus_2021/"+nomFichier+".pdf","rb") as f :
    pdf = pdftotext.PDF(f)

pages = pdf
total = "\n\n".join(pdf)

for i in pages :
    x = re.search("\.\n+ *[0-9]+ +[A-Z]",i)
    if x :
        print(x.span())
        y = x.span()
        print(i[y[0]+2:y[1]])

with open("../result/"+nomFichier+".txt","w") as fichier :
    sortie=""
    for i in pages :
        sortie +=i
    fichier.write(sortie)