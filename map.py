import pygame
import sys
from pygame import mixer
from level_1 import game_map
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
#alussa pelaajan kuva on:
playerImg = pygame.image.load('sheep.png')
#jos kokemus yli XX xp niin pelaajan graafinen kuva on:
playerImg2 = pygame.image.load('sheep2.png')
#Suden kuva:
wolfImg = pygame.image.load('wolf.png')
#Tausta musiikki...
mixer.music.load("happy_clappy.wav")
#...joka soi loopissa
mixer.music.play(-1)

#Fontteja:
font = pygame.font.SysFont("comicsansms", 22)
font1 = pygame.font.SysFont("comicsansms", 40)

mainClock = pygame.time.Clock()

def draw_text(text, font, color, surface, x,y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

click = False
#Päämenu
def main_menu():
    while True:
        #Päämenun tausta
        DISPLAY.fill((0,0,0))
        draw_text("The Epic Adventures of NomNom", font1, (255,255,255), DISPLAY, 200, 50)
        mx, my = pygame.mouse.get_pos()
        play_game_button = pygame.Rect(50,500,200,50)
        draw_text("NEW GAME", font1, (255,255,255), DISPLAY, 40, 450)
        end_game_button = pygame.Rect(800, 500, 200, 50)
        draw_text("QUIT", font1, (255,255,255), DISPLAY, 840, 450)

        #Jos klikkat "NEW GAME" nappulaa, aloita funktio "Peli"
        if play_game_button.collidepoint((mx, my)):
            if click:
                game()
        #Jos klikkaat "QUIT" nappulaa, sulje peli
        if end_game_button.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(DISPLAY,(45, 175, 110), play_game_button)
        pygame.draw.rect(DISPLAY, (45, 175, 110), end_game_button)

        click = False
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)

def game_over():
    DISPLAY.fill((0,0,0))
    draw_text("GAME OVER", font1, (255, 255, 255), DISPLAY, 400, 310)
    pygame.display.update()
    pygame.time.wait(1500)

def win():
    DISPLAY.fill((240, 240, 240))
    draw_text("Look on my Works, ye Mighty, and despair!", font1, (20, 20, 20), DISPLAY, 120, 310)
    draw_text("YOU WIN", font1, (20, 20, 20), DISPLAY, 400, 200)
    pygame.display.update()
    pygame.time.wait(1500)
    exit() #sulkee vain koko pelin


#Peli looppi/ GAME funktio
def game():
    game_on = True
    # Graafisen presentaation koordinaatit (pikseleitä)
    playerX = 0
    playerY = 0
    # NomNomin sijainti kartalla/ ruudukossa
    pos_on_map_row = 0  # Y akseli
    pos_on_map_column = 0  # X akseli

    # NomNom luokka,
    class NomNom:
        def __init__(self, hp=5, xp=0):
            self.hp = hp
            self.xp = xp
        # Funktion tehtävä on näyttää Nomnomin graafinen objekti kartalla
        def location(x, y):
            if nomnom.xp < 50:
                DISPLAY.blit(playerImg, (playerX, playerY))
            else:
                DISPLAY.blit(playerImg2, (playerX, playerY))
        def check_for_win(self):
            if nomnom.xp == 100:
                win()

    #Hahmo
    nomnom = NomNom()

    # Nomnomin statistiikka esitettynä alakulmassa:
    def show_stats(x, y):
        draw_text('Elinvoima:' + str(nomnom.hp), font, (255, 255, 255), DISPLAY, x, y)
        draw_text('Kokemus:' + str(nomnom.xp), font, (255, 255, 255), DISPLAY, x, y+20)

    #Kun peli on käynnissä tee tätä looppia
    while game_on:

        for event in pygame.event.get():
            #  lopettaa ohjelman painaessa x-painiketta
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #jos näppäintä on painettu, tsekkaa onko vasen, oikea, ylös, alas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_on = False
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
                            game_over()
                            return game_on == False

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
                            game_over()
                            return game_on == False

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
                            game_over()
                            return game_on == False

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
                        # muutoin lisää 1 piste kestävyyteen
                        else:
                            nomnom.hp += 1


                if event.key == pygame.K_DOWN:
                    if pos_on_map_row == 19:
                        continue
                    elif game_map[pos_on_map_row + 1][pos_on_map_column] == 0 or game_map[pos_on_map_row + 1][pos_on_map_column] == 2 or game_map[pos_on_map_row + 1][pos_on_map_column] == 3:
                        continue
                    elif game_map[pos_on_map_row + 1][pos_on_map_column] == 4:
                        nomnom.hp -= 1
                        playerY = playerY + 30
                        pos_on_map_row = pos_on_map_row + 1
                        if nomnom.hp == 0:
                            game_over()
                            return game_on == False

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
        if nomnom.check_for_win() == True:
            return game_on==False

        #Näytä elinvoima ja kokemus
        show_stats(10, 550)

        pygame.display.update()



main_menu()


