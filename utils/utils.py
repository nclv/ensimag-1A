#!/usr/bin/env python3

"""
module svg
"""

class Svg:
    """docstring for Svg."""

    def __init__(self, width=100, height=100, style="stroke:rgb(255,0,0);stroke-width:2"):
        self.width = width
        self.height = height
        self.style = style

        print(f"<svg width=\"{self.width}\" height=\"{self.height}\">")

    def draw_line(self, point1, point2):
        """
        Args:
            deux tuples de coordonnées
        Returns:
            une ligne entre les deux points
        """
        print(f"""<line x1="{point1[0]}" y1="{point1[1]}" """)
        print(f"""x2="{point2[0]}" y2="{point2[1]}" """)
        print(f"""style=""{self.style}"" />""")

    def __del__(self):
        """
        destructeur, termine le fichier svg
        """
        print("</svg>")
