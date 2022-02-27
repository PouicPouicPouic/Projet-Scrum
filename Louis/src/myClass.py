
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
        self.position = position
        self.title = title


    """"
        Méthode to_string (__str__) 
        aucun paramètre
        retourne le contenu de texte
    """
    def __str__ (self) -> str:
        return self.texte


    """
        Méthode isValidParagraph retournant un booléen
            True : si texte fini par "\n"
            False : sinon
        Aucun paramètre
    """
    def isValidParagraph (self) -> bool:
        return self.texte[-1]=="\n"


    """
        Méthode isHeader retournant un booléen
            True : position vaut 0
            False : sinon
        Aucun paramètre
    """
    def isHeader(self) -> bool:
        return self.position == 0


#______________________________________________________________________________________________________________________


class Header(Paragraphe) :
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
        self.auteur = ""
        self.abstract = ""
        self.position = 0
        

    """
        Méthode to_string :
        Aucun paramètre
        Retourne une string avec les contenus des différents attributs
    """
    def ___str__(self) -> str:
        return "Titre du documents :\n\t" + self.titreArticle + "\nAuteur(s) :\n\t" + self.auteur + "\nAbstract :\n\t" + self.abstract


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
        Méthode to_string (__str__) 
        aucun paramètre
        retourne le contenu de texte
    """
    def __str__(self) -> str:
        sortie = ""
        for i in self.listPara :
            sortie+= i.texte
        return sortie


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
