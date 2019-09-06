"""
le module implemente les primitives graphiques basiques
d’une tortue logo.
"""

from math import sin, cos, pi

class Logo:
    """
    une tortue logo, positionnee dans le plan.
    """
    def __init__(self):
        """
        positionne la tortue a l’origine, demarre le svg
        """
        self.abscisse = 0.0
        self.ordonnee = 0.0
        self.direction = 270.0  # angle du regard de la tortue (en degre)
        self.crayon_en_bas = False
        # en tete du fichier svg
        print("<svg width=\"100\" height=\"100\">")

    def avance(self, distance):
        """
        avance la tortue tout droit de la distance donnee
        """
        new_abscisse = self.abscisse + cos(self.direction * pi / 180) * distance
        new_ordonnee = self.ordonnee + sin(self.direction * pi / 180) * distance

        if self.crayon_en_bas:
            print(f"""<line x1="{self.abscisse}" y1="{self.ordonnee}" """)
            print(f"""x2="{new_abscisse}" y2="{new_ordonnee}" """)
            print('style="stroke:rgb(255,0,0);stroke-width:2" />')

        self.abscisse, self.ordonnee = new_abscisse, new_ordonnee

    def tourne_droite(self, angle):
        """
        change la direction de la tortue en tournant a droite
        de l’angle donne (en degre)
        """
        self.direction += angle

    def tourne_gauche(self, angle):
        """
        change la direction de la tortue en tournant a gauche
        de l’angle donne (en degre)
        """
        self.direction -= angle

    def baisse_crayon(self):
        """
        baisse le crayon. a partir de maintenant la tortue dessine
        lorsqu’elle avance
        """
        self.crayon_en_bas = True

    def leve_crayon(self):
        """
        leve le crayon. a partir de maintenant la tortue ne dessine pas
        lorsqu’elle avance.
        """
        self.crayon_en_bas = False

    def __del__(self):
        """
        destructeur, termine le fichier svg
        """
        print("</svg>")
