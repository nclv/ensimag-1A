# -*- coding: utf-8 -*-
#!/usr/bin/env python3


"""
Patterns
"""

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
