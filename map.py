import pygame
import sys
from pygame import mixer
import time

#  määritetään kartan ruutujen arvo
W = 0 #WATER
G = 1 #GRASS
F = 2 #FOREST
M = 3 #MOUNTAIN
L = 4 #LIGHT BROWN/DRY GRASS
D = 5 #DARK BROWN/BRIDGE

#  yhdistetään ruudut ja kuvat
tile_colour = {W: pygame.image.load('water.jpg'),
               G: pygame.image.load('grass.jpg'),
               F: pygame.image.load('forest.jpg'),
               M: pygame.image.load('mountain.jpg'),
               L: pygame.image.load('drygrass.jpg'),
               D: pygame.image.load('bridge.jpg')}

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

# määritetään kartan koko
TILESIZE = 30
MAPWIDTH = 35
MAPHEIGHT = 20


#Alustetaan PyGame
pygame.init()
# luodaan näyttö ylempien parometrien pohjalta
DISPLAY = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))

#Annetaan pelille nimi
pygame.display.set_caption('The Epic Adventure of NomNom')

#NomNom, pelihahmo ja siihen liittyvät funktiot
#NomNomin graafinen presentaatio kartalla

#Graafisen presentaation koordinaatit (pikseleitä)
playerX = 0
playerY = 0
#alussa pelaajan kuva on:
playerImg = pygame.image.load('sheep.png')
#jos kokemus yli XX xp niin pelaajan graafinen kuva on:
playerImg2 = pygame.image.load('sheep2.png')
#NomNomin sijainti kartalla/ ruudukossa
pos_on_map_row = 0 #Y akseli
pos_on_map_column = 0 #X akseli

#NomNom luokka,
class NomNom:
    def __init__(self, hp=5, xp=0):
        self.hp = hp
        self.xp =xp
    #Funktion tehtävä on näyttää Nomnomin graafinen objekti kartalla

    def location(x,y):
        if nomnom.xp < 100:
            DISPLAY.blit(playerImg, (playerX,playerY))
        else:
            DISPLAY.blit(playerImg2, (playerX, playerY))

nomnom=NomNom()

# WOLF

#Suden kuva:
wolfImg = pygame.image.load('wolf.png')

# Susien graafisen presentaation koordinaatit (pikseleitä)
wolf1X = 270
wolf1Y = 270

wolf2X = 270
wolf2Y = 270
wolf3X = 270
wolf3Y = 270
wolf4X = 270
wolf4Y = 270
wolf5X = 270
wolf5Y = 270
wolf6X = 270
wolf6Y = 270

#Suden sijainti kartalla/ruudukossa
wolf1_pos_on_map_row = 9 #Y akseli
wolf1_pos_on_map_column = 9 #X akseli

wolf2_pos_on_map_row = 0 #Y akseli
wolf2_pos_on_map_column = 0 #X akseli
wolf3_pos_on_map_row = 0 #Y akseli
wolf3_pos_on_map_column = 0 #X akseli
wolf4_pos_on_map_row = 0 #Y akseli
wolf4_pos_on_map_column = 0 #X akseli
wolf5_pos_on_map_row = 0 #Y akseli
wolf5_pos_on_map_column = 0 #X akseli
wolf6_pos_on_map_row = 0 #Y akseli
wolf6_pos_on_map_column = 0 #X akseli

#Funktion tehtävä on näyttää suden graafinen objekti kartalla
def wolf_location(x,y):
    DISPLAY.blit(wolfImg, (x, y))

#Funktion tehtävä on liikuttaa suden graafista objektia sekä muuttaa suden sijaintia kartalla/ruudukossa
def move_wolf1(y_pos, y_coor):
    if y_pos == 9:
        # wolf1_pos_on_map_row += 1
        # wolf1X += 30
    # elif y_pos == 10:
    #     y_pos += 1
    #     y_coor += 30

move_left = 30
move_right = -30

# pygame.time.set_timer(USEREVENT, 1000)

#Tausta musiikki...
mixer.music.load("happy_clappy.wav")
#...joka soi loopissa
mixer.music.play(-1)

#Nomnomin statistiikka esitettynä yläkulmassa:
font = pygame.font.SysFont("comicsansms", 22)
textX = 10
textY = 550
def show_stats(x,y):
    show_hp = font.render('Elinvoima:' +str(nomnom.hp), True,(255,255,255))
    DISPLAY.blit(show_hp, (x, y))
    show_xp = font.render('Kokemus:' + str(nomnom.xp), True, (255, 255, 255))
    DISPLAY.blit(show_xp, (x, y+20))

#Peli looppi
while True:

    for event in pygame.event.get():
        #  lopettaa ohjelman painaessa x-painiketta
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #jos näppäintä on painettu, tsekkaa onko vasen, oikea, ylös, alas
        if event.type == pygame.KEYDOWN:
    #kun painat nuolta VASEN

            if event.key == pygame.K_LEFT:
    # -------------------------------------------------------------------------------------------------
    #TÄMÄ OSIA OMAKSI FUNKTIOKSI (def move_left())
                #tarkistetaan voiko kyseiseen suuntaan liikkua
                if game_map[pos_on_map_row][pos_on_map_column-1] == 0 or game_map[pos_on_map_row][
                    pos_on_map_column-1] == 2 or game_map[pos_on_map_row][pos_on_map_column-1] == 3 or pos_on_map_column==0:
                    continue

                # Jos suunnassa on ruskeaa maata, kestävyys alenee 1 pisteen verran:
                elif game_map[pos_on_map_row][pos_on_map_column - 1] == 4:
                    # jos suuntaan voi liikkua niin muutetaan graafisen presentaation positiota,
                    # sekä Nomnomin sijaintia kartta ruudukossa:
                    playerX = playerX - 30
                    pos_on_map_column = pos_on_map_column - 1
                    nomnom.hp -= 1
                    # tarkistetaan onko Nomnom hengissä. Jos ei, peli loppuu
                    if nomnom.hp == 0:
                        break  # Myöhemmin GAME OVER grafiikka ja paluu main menuun

                #jos edessä on silta, ei tapahdu mitään erityistä
                elif game_map[pos_on_map_row][pos_on_map_column - 1] == 5:
                    playerX = playerX - 30
                    pos_on_map_column = pos_on_map_column - 1

                # Jos suunnassa ruohoa...
                else:
                    playerX = playerX - 30
                    pos_on_map_column = pos_on_map_column - 1
                    game_map[pos_on_map_row][pos_on_map_column] = 4
                    # jos nomnom kestävyys on täysi lisää 1 piste kokemukseen...
                    if nomnom.hp == 5:
                        nomnom.xp += 1
                        print(nomnom.xp)
                        # if nomnom.xp == 20: NomNom kehittyy
                    # muutoin lisää 1 piste kestävyyteen
                    else:
                        nomnom.hp += 1


            if event.key == pygame.K_RIGHT:
        # -------------------------------------------------------------------------------------------------
        # TÄMÄ OSIA OMAKSI FUNKTIOKSI (def move_right())

                if pos_on_map_column==34:
                    continue
                elif game_map[pos_on_map_row][pos_on_map_column + 1] == 0 or game_map[pos_on_map_row][pos_on_map_column + 1] == 2 or game_map[pos_on_map_row][pos_on_map_column + 1] == 3:
                    continue
                    # Jos suunnassa on ruskeaa maata, kestävyys alenee 1 pisteen verran:
                elif game_map[pos_on_map_row][pos_on_map_column + 1] == 4:
                    nomnom.hp -= 1
                    playerX = playerX + 30
                    pos_on_map_column = pos_on_map_column + 1
                    if nomnom.hp == 0:
                        break  # Myöhemmin GAME OVER grafiikka ja paluu main menuun

                elif game_map[pos_on_map_row][pos_on_map_column + 1] == 5:
                    playerX = playerX + 30
                    pos_on_map_column = pos_on_map_column + 1

                    # Jos suunnassa ruohoa...
                else:
                    playerX = playerX + 30
                    pos_on_map_column = pos_on_map_column + 1
                    game_map[pos_on_map_row][pos_on_map_column] = 4
                    # jos nomnom kestävyys on täysi lisää 1 piste kokemukseen...
                    if nomnom.hp == 5:
                        nomnom.xp += 1
                        print(nomnom.xp)
                        # if nomnom.xp == 20: NomNom kehittyy
                    # muutoin lisää 1 piste kestävyyteen
                    else:
                        nomnom.hp += 1

            if event.key == pygame.K_UP:
        # -------------------------------------------------------------------------------------------------
        # TÄMÄ OSIA OMAKSI FUNKTIOKSI (def move_up())
                if game_map[pos_on_map_row-1][pos_on_map_column] == 0 or game_map[pos_on_map_row-1][pos_on_map_column] == 2 or game_map[pos_on_map_row-1][pos_on_map_column] == 3 or pos_on_map_row==0:
                    continue

                elif game_map[pos_on_map_row - 1][pos_on_map_column] == 4:
                    nomnom.hp -= 1
                    playerY = playerY - 30
                    pos_on_map_row = pos_on_map_row - 1
                    if nomnom.hp == 0:
                        break  # Myöhemmin GAME OVER grafiikka ja paluu main menuun

                elif game_map[pos_on_map_row - 1][pos_on_map_column] == 5:
                    playerY = playerY - 30
                    pos_on_map_row = pos_on_map_row - 1

                    # Jos suunnassa ruohoa...
                else:
                    playerY = playerY - 30
                    pos_on_map_row = pos_on_map_row - 1
                    game_map[pos_on_map_row][pos_on_map_column] = 4
                    # jos nomnom kestävyys on täysi lisää 1 piste kokemukseen...
                    if nomnom.hp == 5:
                        nomnom.xp += 1
                        print(nomnom.xp)
                        # if nomnom.xp == 20: NomNom kehittyy
                    # muutoin lisää 1 piste kestävyyteen
                    else:
                        nomnom.hp += 1


            if event.key == pygame.K_DOWN:
        # -------------------------------------------------------------------------------------------------
        # TÄMÄ OSIA OMAKSI FUNKTIOKSI (def move_down())
                if pos_on_map_row == 19:
                    continue
                elif game_map[pos_on_map_row + 1][pos_on_map_column] == 0 or game_map[pos_on_map_row + 1][pos_on_map_column] == 2 or game_map[pos_on_map_row + 1][pos_on_map_column] == 3:
                    continue
                elif game_map[pos_on_map_row + 1][pos_on_map_column] == 4:
                    nomnom.hp -= 1
                    playerY = playerY + 30
                    pos_on_map_row = pos_on_map_row + 1
                    if nomnom.hp == 0:
                        break
                         # Myöhemmin GAME OVER grafiikka ja paluu main menuun

                elif game_map[pos_on_map_row + 1][pos_on_map_column] == 5:
                    playerY = playerY + 30
                    pos_on_map_row = pos_on_map_row + 1

                    # Jos suunnassa ruohoa...
                else:
                    playerY = playerY + 30
                    pos_on_map_row = pos_on_map_row + 1
                    game_map[pos_on_map_row][pos_on_map_column] = 4
                    # jos nomnom kestävyys on täysi lisää 1 piste kokemukseen...
                    if nomnom.hp == 5:
                        nomnom.xp += 1
                        # if nomnom.xp == 20: NomNom kehittyy
                    # muutoin lisää 1 piste kestävyyteen
                    else:
                        nomnom.hp += 1


    #  piirtää kartan
    #  pystyrivit
    for row in range(MAPHEIGHT):
        #  vaakarivit
        for column in range(MAPWIDTH):
            DISPLAY.blit(tile_colour[game_map[row][column]], (column * TILESIZE, row * TILESIZE))
    #DISPLAY.blit(playerImg, (playerX, playerY))
    nomnom.location((playerX,playerY))


    wolf_location(wolf1X, wolf1Y)

    move_wolf1(wolf1_pos_on_map_row, wolf1Y)

    wolf_location(wolf1X, wolf1Y)

    #Näytä elinvoima ja kokemus
    show_stats(textX, textY)

    pygame.display.update()






