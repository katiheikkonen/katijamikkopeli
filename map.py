import pygame
import sys

#  määritetään kartan palikat

W = 0 #WATER
G = 1 #GRASS
F = 2 #FOREST
M = 3 #MOUNTAIN
L = 4 #LIGHT BROWN
D = 5 #DARK BROWN

#  määritetään palikoiden värit

WATER = (0,0,255)
GRASS = (124, 252, 0)
FOREST = (0, 100, 0)
MOUNTAIN = (166, 166, 166)
LIGHT_BROWN = (204, 102, 0)
DARK_BROWN = (102, 51, 0)

#  yhdistetään palikat ja värit

tile_colour = {W: WATER, G: GRASS, F: FOREST, M: MOUNTAIN, L: LIGHT_BROWN, D: DARK_BROWN}

#  kartta

game_map =[[G,G,G,G,G,G,G,G,F,F,F,F,G,G,G,W,G,G,W,G,G,G,M,M,M],
        [W,G,G,G,G,G,G,G,G,F,F,F,G,G,G,W,G,G,W,G,G,G,G,M,M],
        [W,W,G,G,G,G,G,G,F,F,F,F,G,G,G,W,W,G,W,G,G,G,G,M,M],
        [W,W,G,G,G,G,G,F,F,F,F,F,G,G,G,G,W,W,W,G,G,G,G,G,M],
        [W,W,W,G,G,G,G,G,F,F,G,F,G,G,G,G,W,G,G,G,G,G,M,M,M],
        [W,W,W,G,G,G,G,G,F,F,F,F,G,G,G,G,D,G,G,G,G,G,G,M,M],
        [W,W,W,G,G,G,G,G,G,F,G,F,G,G,G,G,W,G,G,G,G,G,G,G,M],
        [W,W,W,W,W,G,G,G,G,G,F,F,G,G,G,W,W,G,G,G,G,G,G,G,G],
        [W,W,W,W,W,W,G,G,G,G,G,F,G,G,W,W,G,G,G,G,G,G,F,F,G],
        [W,W,W,W,W,G,G,G,F,G,G,G,G,W,W,G,G,G,G,G,G,G,G,F,F],
        [F,W,W,W,W,W,W,W,W,W,W,D,W,W,G,G,G,G,G,G,G,G,F,F,F],
        [M,F,W,W,W,W,W,W,W,W,G,G,G,G,G,G,G,W,W,G,G,G,G,G,F],
        [M,M,M,F,W,W,W,W,G,G,G,G,G,G,G,W,W,W,W,G,G,G,G,G,G],
        [M,F,M,W,W,W,W,W,W,G,G,G,F,G,G,G,G,G,W,G,G,G,G,G,F],
        [M,M,W,W,W,W,W,W,G,G,G,G,F,F,G,G,G,G,G,G,G,G,F,M,M]]

#  määrittää kartan koon

TILESIZE = 40
MAPWIDTH = 25
MAPHEIGHT = 15

#  luo näytön

pygame.init()
DISPLAY = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))

#  käyttöliittymä

while True:

    for event in pygame.event.get():

        #  lopettaa ohjelman painaessa x-painiketta
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #  piirtää kartan
    #  pystyrivit
    for row in range(MAPHEIGHT):
        #  vaakarivit
        for column in range(MAPWIDTH):
            pygame.draw.rect(DISPLAY, tile_colour)








