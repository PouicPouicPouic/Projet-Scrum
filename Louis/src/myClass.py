
class Paragraphe :
    """
        Interface Paragraphe aillant 3 attributs :
            string texte : contenu du Paragraphe
            string title : titre donner au Paragraphe
            integer position : numero dans la suite des Paragraphe
        Paramètres :
            string  texte : contenu du paragraphe
            integer  position : position du paragraphe dans la partie
            string  title : titre du paragraphe (exemple : "4.3 sentence combination" dans jing-cutepaste.pdf)
    """

    def __init__(self,texte,position,title="") :
        self.texte = texte
        self.position = position
        self.title = title

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



class Header(Paragraphe) :
    """
        Class Header héritant de la class Paragraphe
        "Un entete est un paragraphe à la position 0 (le premier paragrapge du pdf)"
        Paramètres :
            string  nomFichier : nom du fichier pdf d'origine
    """
    def __init__(self,nomFichier) :
        self.nomFichier = nomFichier
        self.titreArticle = ""
        self.auteur = ""
        self.abstract = ""
        self.position = 0
        


class Partie :
    """
        Classe Partie possédant un seul attribut :
            Paragraphe[]  listPara : liste des paragraphes contenus dans une partie (Introduction est une partie)
        Paramètre :
            string  titre : titre de la partie (exemple : Introduction)
    """

    def __init__(self, titre) :
        self.listPara=[]
        self.titre = titre


    """
        Méthode addParagraphe ne retournant rien 
        Paramètre :
            Paragraphe  para : paragraphe à ajouter à la partie
        
    """
    def addParagraphe(self,para) :
        self.listPara.append(para)