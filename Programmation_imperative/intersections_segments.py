#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
affichage d'intersection de segments
"""
from segment import segment_aleatoire


def main():
    segments = []

    print('<svg width="800" height="800">')

    for _ in range(10):
        segments.append(segment_aleatoire())

    for segment in segments:
        segment.affiche()

    print('</svg>')


main()
