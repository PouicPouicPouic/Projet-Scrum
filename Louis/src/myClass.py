
class Paragraphe :
    """
        Interface Paragraphe aillant 3 attributs :
            str texte : contenu du §
            str title : titre donner au §
            integer position : numero dans la suite des § 
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
    """
    def isValidParagraph (self) -> bool:
        return self.texte[-1]=="\n"

    """
        Méthode isHeader retournant un booléen
        True : position vaut 0
        False : sinon
    """
    def isHeader(self) -> bool:
        return self.position == 0


class Header(Paragraphe) :
    """
        Class Header héritant de la class Paragraphe
        "Un entete est un paragraphe à la position 0 (le premier paragrapge du pdf)"
    """
    def __init__(self,texte,title="") :
        self.texte = texte
        self.titre = title
        self.position = 0
        

