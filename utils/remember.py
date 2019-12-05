# -*- coding: utf-8 -*-
#!/usr/bin/env python3


"""
Patterns
https://www.toptal.com/python/python-design-patterns
"""

#Instead of doing this: inheritance

class User(DbObject):
    pass

#We can do something like this: composition

class User:
    _persist_methods = ['get', 'save', 'delete']

    def __init__(self, persister):
        self._persister = persister

    def __getattr__(self, attribute):
        if attribute in self._persist_methods:
            return getattr(self._persister, attribute)

failed = False
for other_room in rooms:
    if test(other_room):
        failed = True
        break
failed = any(test(other_room) for other_room in rooms)


for room in rooms:
    if in_and_side_room((absc, ordo), room):
        board[absc][ordo] = 1
        break
board[absc][ordo] = any(in_and_side_room((absc, ordo), room) for room in rooms)

def connect_rooms_corridor(self):
    """Renvoi toutes les cases pouvant connecter une pièce avec un couloir

    """
    connecteurs = np.zeros(board.shape)
    for position, _ in np.ndenumerate(self.board):
        tile = board[position]
        #check if not wall
        if tile != EMPTY:
            continue

        regions = set()
        for direction in DIRECTIONS:
            region = board[position + direction]
            if region:
                regions.add(region)

        if len(regions) < 2: continue

        connecteurs[position] = regions
