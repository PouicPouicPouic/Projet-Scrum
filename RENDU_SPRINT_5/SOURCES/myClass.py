
class Paragraphe :
    """
        Classe Paragraphe aiyant 3 attributs : (exemple : "4.3 sentence combination" dans jing-cutepaste.pdf est un paragraphe)
            string texte : contenu du Paragraphe
            string title : titre donner au Paragraphe
            integer position : numero du Paragaraphe dans la Partie
    """
    
    """
        CONSTRUCTEUR
        Paramètres :
            string  texte : contenu du paragraphe
            integer  position : position du paragraphe dans la partie
            string  title : titre du paragraphe 
    """
    def __init__(self,texte,position,title="") :
        self.texte = texte
        self.title = title
        self.position = position


    """
        Méthode toStringTxt() 
        aucun paramètre
        retourne le contenu de texte en version txt
    """
    def toSringTxt(self) -> str:
        ParaReturn = ""
        ParaReturn+=self.title+"\n"
        ParaReturn+="/t"+self.texte+"\n"
        return ParaReturn

    """
        Méthode toStringXml() 
        aucun paramètre
        retourne le contenu de texte en version xml
    """
    def toStringXml(self) -> str:
        ParaReturn = ""
        ParaReturn+="/t<titreparagraphe>"+self.title+"</titreparagraphe>\n"
        ParaReturn+="/t<paragraphe>"+self.texte+"</paragraphe>\n"
        return ParaReturn
    """
        Méthode isValidParagraph retournant un booléen
            True : si texte fini par "\n"
            False : sinon
        Aucun paramètre
    """
    def isValidParagraph (self) -> bool:
        return self.texte[-1]=="\n"

#______________________________________________________________________________________________________________________


class Header :
    """
        Class Header héritant de la class Paragraphe, correspondant à l'entète du fichier : toute la partie avant (Introduction)
        "Un entete est un paragraphe à la position 0 (le premier paragrapge du pdf)"
        5 attributs dont 3 hérité
    """

    """
        CONSTRUCTEUR
        Paramètres :
            string  nomFichier : nom du fichier pdf d'origine
    """
    def __init__(self,nomFichier) :
        self.nomFichier = nomFichier
        self.titreArticle = ""
        self.auteur = []
        self.mail = []
        self.introduction = ""
        self.corps = ""
        self.abstract = ""        
        self.biblio = ""

    """
        Méthode toStringTxt :
        Aucun paramètre
        Retourne le texte du header séparé selons contenus des différents attributs en version TXT
    """
    def toStringTxt(self) -> str:
        headerReturn = ""
        headerReturn+="Nom du fichier :\n\t" + self.nomFichier + "\n"
        headerReturn+="Titre :\n\t" + self.titreArticle + "\n"

        headerReturn+="Auteur(s) :\n"
        for i in range (len(self.auteur)):
                headerReturn+="\t"+self.auteur[i]+ "\n"
                if len(self.mail) > 0 and len(self.mail) == len(self.auteur):
                    headerReturn+="\t\t"+self.mail[i]+ "\n"
            
        headerReturn+="Abstract :\n" + self.abstract + "\n"

        headerReturn+="Biblio :\n" + self.biblio + "\n"
        return headerReturn
    
    """
        Méthode toStringXml :
        Aucun paramètre
        Retourne le texte du header séparé selons contenus des différents attributs en version XML
    """
    def toStringXml(self) -> str:
        
        headerReturn = ""
        headerReturn+="<header>\n"
        headerReturn+="\t<preamble>" + self.nomFichier + "</preamble>\n"
        headerReturn+="\t<titre>" + self.titreArticle + "</titre>\n"

        headerReturn+="\t<auteurs>\n"
        for i in range (len(self.auteur)):
                headerReturn+="\t\t<auteur>\n"
                headerReturn+="\t\t\t<name>"+self.auteur[i]+"</name>\n"
                if len(self.mail) > 0 and len(self.mail) == len(self.auteur):
                    headerReturn+="\t\t\t\t<mail>"+self.mail[i]+"</mail>\n"
                headerReturn+="\t\t</auteur>\n"
        headerReturn+="\t</auteurs>\n"

        headerReturn+="\t<abstract>\n" + self.abstract + "\n\t</abstract>\n"

        headerReturn+="\t<introduction>\n"+ self.introduction + "\n\t</introduction>\n"

        headerReturn+="\n\t<corps>\n"+ self.corps + "\n\t</corps>\n"

        headerReturn+="\t<biblio>\n" + self.biblio + "\n\t</biblio>\n"

        headerReturn+="</header>\n"
        return headerReturn


#______________________________________________________________________________________________________________________


class Partie :
    """
        Classe Partie possédant 2 attributs : (exemple : Introduction est une Partie)
            Paragraphe[]  listPara : liste des paragraphes contenus dans une partie (Introduction est une partie)
            String  titre : titre ou dénomination de la Partie
    """
    

    """
        CONSTRUCTEUR
        Paramètre :
            string  titre : titre de la partie 
    """
    def __init__(self, titre) :
        self.listPara=[]
        self.titre = titre


    """"
        Méthode toStringTxt
        aucun paramètre
        retourne le contenu d'une partie en version TXT
    """
    def toStringTxt(self) -> str:
        partieReturn = ""
        partieReturn+="\t"+self.titre+"\n"
        for i in self.listPara :
            partieReturn+= i.toStringTxt()
        return partieReturn

    """"
        Méthode toStringXml 
        aucun paramètre
        retourne le contenu de d'une partie en version XML
    """
    def toStringXml(self) -> str:
        partieReturn = ""
        partieReturn+="<partie>"
        partieReturn+=self.titre+"\n"
        for i in self.listPara :
            partieReturn+= i.toStringTxt()
        partieReturn+="</partie>"
        return partieReturn


    """
        Méthode addParagraphe ne retournant rien 
        Paramètre :
            Paragraphe  para : paragraphe à ajouter à la partie
        
    """
    def addParagraphe(self,para) :
        self.listPara.append(para)


#______________________________________________________________________________________________________________________


class Texte :
    """
        Classe Texte possédant 2 attributs :
            Header  entete : entete du Texte
            Partie[]  listParties : listes contenant les différentes parties composant le Texte
    """
    def __init__(self) :
        self.header = None
        self.corps = []

        """
        Méthode toStringTxt :
        Aucun paramètre
        Retourne le texte séparé selons contenus des différents attributs en version TXT
    """
    def toStringTxt(self) -> str:
        texteReturn = ""
        texteReturn+=self.header.toStringTxt()
        for p in self.parties :
            texteReturn+=p.toStringTxt()
        return texteReturn
    
    """
        Méthode toStringXml :
        Aucun paramètre
        Retourne le texte séparé selons contenus des différents attributs en version XML
    """
    def toStringXml(self) -> str:
        texteReturn = ""
        texteReturn = "<article>\n"
        texteReturn+=self.header.toStringXml()
        texteReturn += "</article>\n"
        return texteReturn
