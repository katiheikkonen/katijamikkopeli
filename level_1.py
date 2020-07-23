W = 0 #WATER
G = 1 #GRASS
F = 2 #FOREST
M = 3 #MOUNTAIN
L = 4 #LIGHT BROWN/DRY GRASS
D = 5 #DARK BROWN/BRIDGE

# kartta, jossa kirjain vastaa 30x30 ruutua, jonka ympäristön määrittää Kijain
game_map =[[G,G,G,G,G,G,G,G,F,F,F,F,G,G,G,W,G,G,W,G,G,G,M,M,M,W,G,G,G,G,G,G,G,W,W],
        [W,G,G,G,G,G,G,G,G,F,F,F,G,G,G,W,G,G,W,G,G,G,G,M,M,W,W,G,G,G,G,G,W,W,W],
        [W,W,G,G,G,G,G,G,F,F,F,F,G,G,G,W,W,G,W,G,G,G,G,M,M,M,G,G,G,G,G,G,G,W,W],
        [W,W,G,G,G,G,G,F,F,F,F,F,G,G,G,G,W,W,W,G,G,G,G,G,M,W,G,G,G,G,G,G,G,G,W],
        [W,W,W,G,G,G,G,G,F,F,G,F,G,G,G,G,W,G,G,G,G,G,M,M,M,M,G,G,G,G,G,G,G,W,W],
        [W,W,W,G,G,G,G,G,F,F,F,F,G,G,G,G,D,G,G,G,G,G,G,M,M,G,G,G,G,G,G,G,G,G,G],
        [W,W,W,G,G,G,G,G,G,F,G,F,G,G,G,G,W,G,G,G,G,G,G,G,M,G,G,G,G,G,G,G,G,F,G],
        [W,W,W,W,W,G,G,G,G,G,F,F,G,G,G,W,W,G,G,G,G,G,G,G,G,G,G,G,G,G,G,G,F,F,G],
        [W,W,W,W,W,W,G,G,G,G,G,F,G,G,W,W,G,G,G,G,G,G,F,F,G,G,G,G,G,G,G,F,F,G,G],
        [W,W,W,W,W,G,G,G,F,G,G,G,G,W,W,G,G,G,G,G,G,G,G,F,F,G,G,G,G,G,G,G,F,F,G],
        [F,W,W,W,W,W,W,W,W,W,W,D,W,W,G,G,G,G,W,G,G,G,F,F,F,G,G,G,G,G,F,F,F,F,G],
        [M,F,W,W,W,W,W,W,W,W,G,G,G,D,G,G,W,W,W,G,G,G,G,G,F,G,G,G,G,F,F,F,G,G,G],
        [M,M,M,F,W,W,W,W,G,G,G,G,G,W,W,W,W,W,W,G,G,G,G,G,G,G,G,G,G,G,G,G,F,G,G],
        [M,F,M,W,W,W,W,W,W,G,G,G,G,G,G,G,G,G,W,G,G,G,G,G,F,G,G,G,G,G,G,G,F,F,G],
        [M,M,W,W,W,W,W,W,G,G,G,G,F,F,G,G,G,G,W,W,G,G,F,M,M,M,G,G,G,G,G,G,G,G,G],
        [M,W,W,W,W,W,W,W,G,G,G,G,G,F,G,G,G,G,W,G,G,G,F,M,M,F,G,G,G,G,G,G,G,W,W],
        [W,W,W,W,W,W,W,F,G,G,G,G,G,G,G,G,G,G,D,G,G,F,F,M,M,F,G,G,G,G,W,D,W,W,W],
        [W,W,W,W,W,W,F,F,F,G,G,G,G,F,F,G,G,W,W,G,G,F,F,F,M,F,G,G,W,W,W,G,G,W,W],
        [W,W,W,W,W,W,W,W,G,G,G,G,G,G,G,G,G,G,W,W,G,G,F,M,M,W,W,D,W,G,G,G,G,G,W],
        [W,W,W,W,W,W,G,G,G,G,G,G,F,F,G,G,G,G,W,G,G,G,G,M,M,M,G,G,G,G,G,G,G,G,G]]