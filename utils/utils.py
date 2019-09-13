# -*- coding: utf-8 -*-
#!/usr/bin/env python3

"""
module svg de http://www.codedrome.com/svg-library-in-python/
"""


class Svg:

    """
    Classe d'affichage Svg.

    Donne des méthodes pour créer une image SVG vide, ajouter des figures et du texte,
    et sauvegarder le fichier final.

    Attributes:
        svg_list (list): liste des figures svg de l'image
        width (int): largeur de l'image créée
        height (str): hauteur de l'image créée
        templates (dict): figures possibles

    """

    def __init__(self):
        """Le constructeur de la classe Svg.

        """
        self.svg_list = []
        self.width = 0
        self.height = 0

        self.templates = self.__generate_templates()

    def __add_to_svg(self, text):
        """Ajoute un élément sur l'image.

        Parameters:
            text (str): élément ajouté

        """
        self.svg_list.append(str(text))

    @classmethod
    def __generate_templates(cls):
        """Crèe des templates utilisés par les méthodes correspondantes.

        """
        templates = {}

        templates["create"] = "<svg width='{}px' height='{}px'>\n"
        templates["end"] = "</svg>"

        templates["circle"] = "<circle stroke='{}' stroke-width='{}px' \
        fill='{}' r='{}' cy='{}' cx='{}' />\n"
        templates["line"] = "<line stroke='{}' stroke-width='{}px' \
        y2='{}' x2='{}' y1='{}' x1='{}' />\n"
        templates["rectangle"] = "<rect fill='{}' stroke='{}' stroke-width='{}px' \
        width='{}' height='{}' y='{}' x='{}' ry='{}' rx='{}' />\n"
        templates["text"] = "<text x='{}' y='{}' font-family='{}' stroke='{}' \
        fill='{}' font-size='{}px'>{}</text>\n"
        templates["ellipse"] = "<ellipse cx='{}' cy='{}' rx='{}' ry='{}' \
        fill='{}' stroke='{}' stroke-width='{}' />\n"

        return templates

    def create(self, width, height):
        """Adds the necessary opening element to document.

        Parameters:
            width (int): largeur de l'image créée
            height (str): hauteur de l'image créée
            svg_list (list): largeur de l'image créée

        """
        self.width = width
        self.height = height

        self.svg_list.clear()

        self.__add_to_svg(self.templates["create"].format(width, height))

    def end(self):
        """Ferme l'élément SVG.

        """
        self.__add_to_svg(self.templates["end"])

    def circle(self, stroke, strokewidth, fill, rayon, centrex, centrey):
        """Ajoute un cercle.

        """
        self.__add_to_svg(self.templates["circle"].format(stroke, strokewidth, fill, \
        rayon, centrey, centrex))

    def line(self, stroke, strokewidth, absc1, ord1, absc2, ord2):
        """Ajoute une ligne.

        """
        self.__add_to_svg(self.templates["line"].format(stroke, strokewidth, \
        ord2, absc2, ord1, absc1))

    def rectangle(self, width, height, absc, ordo, fill, stroke, strokewidth, radiusx, radiusy):
        """Ajoute un rectangle.

        """
        self.__add_to_svg(self.templates["rectangle"].format(fill, stroke, \
        strokewidth, width, height, ordo, absc, radiusy, radiusx))

    def fill(self, color):
        """Remplie toute l'image avec une couleur.

        """
        self.rectangle(self.width, self.height, 0, 0, color, color, 0, 0, 0)

    def text(self, absc, ordo, fontfamily, fontsize, fill, stroke, text):
        """Ajoute du texte.

        """
        self.__add_to_svg(self.templates["text"].format(absc, ordo, \
        fontfamily, stroke, fill, fontsize, text))

    def ellipse(self, centrex, centrey, rayonx, rayony, fill, stroke, strokewidth):
        """Ajoute une ellipse.

        """
        self.__add_to_svg(self.templates["ellipse"].format(centrex, centrey, rayonx, rayony, \
        fill, stroke, strokewidth))

    def __str__(self):
        """Renvoie toute l'image en raccordant les éléments.

        """
        return "".join(self.svg_list)

    def save(self, path):
        """Sauvegarde l'image.

        """
        with open(path, "w+") as file:
            file.write(str(self))
