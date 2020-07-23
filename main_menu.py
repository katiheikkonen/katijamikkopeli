
font1 = pygame.font.SysFont("comicsansms", 30)

mainClock = pygame.time.Clock()

def draw_text(text, font, color, surface, x,y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get.rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

def main_menu():
    while True:
        DISPLAY.fill(0,0,0)
        draw_text("The Epic Adventures of NomNom", font1, (255,255,255), DISPLAY, 400, 50)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key = K_ESCAPE:

            pygame.display.update()
            mainClock.tick(60)
