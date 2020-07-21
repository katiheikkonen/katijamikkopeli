


#  luodaan pelaajan hahmo



class NomNom():

    def __init__(self, hp=10, xp=0, x, y):
        self.hp = hp
        self.xp = xp
        self.x = x
        self.y = y

    #  piirretään esimerkkikartta

    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    SCREEN_TITLE = "NomNom"

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.set_background_color(arcade.color.GREEN)

    arcade.start_render()

    #  piirretään NomNom

    x = 20
    y = 580
    radius = 40
    arcade.draw_rectangle_filled(x, y, 45, 65, arcade.color.WHITE)

    #  lopetetaan ja piirretään lopputulos

    arcade.finish_render()

    arcade.run()


