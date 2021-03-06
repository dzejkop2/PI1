import math
import random

import pyglet
from pyglet import gl
from pyglet.window import key

"---------Globalne konštanty a premenne----------"

"Window constants"
WIDTH = 1200
HEIGHT = 800

"Game constants"
ACCELERATION = 120              #Zrýchlenie rakety
ROTATION_SPEED = 0.05           #Rýchlosť otáčania rakety

objects = []                    #ZOZNAM VŠETKÝCH AKTÍVNYCH OBJEKTOV V HRE
batch = pyglet.graphics.Batch() #ZOZNAM SPRITOV PRE ZJEDNODUŠENÉ VYKRESLENIE
pressed_keyboards = set()       #MNOŽINA ZMAČKNUTÝCH KLÁVES


"------------------- FUNKCIE __________________"

"""
Vycentruj ukotvenie obrázka na stred
"""
def set_anchor_of_image_to_center(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2

"----------------VLASTNÉ TRIEDY----------------"

"""
Rodičovská trieda
"""
class SpaceObject:
   #Todo 1: Vytvorenie rodičovskej triedy
    def __init__(self, sprite, x, y, speed_x = 0, speed_y = 0):
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rotation = 1.57
        self.sprite = pyglet.sprite.Sprite(sprite, batch=batch)
        self.sprite.x = x
        self.sprite.y = y

    """
         Metóda pre kontrolu pozície či sa nachádzame na okraji
    """
    def checkBoundaries(self):
        if self.sprite.x > WIDTH:
            self.sprite.x = 0

        if self.sprite.x < 0:
            self.sprite.x = WIDTH

        if self.sprite.y < 0:
            self.sprite.y = HEIGHT

        if self.sprite.y > HEIGHT:
            self.sprite.y = 0

    def tick(self,dt):
        self.sprite.x += dt * self.speed_x
        self.sprite.y += dt * self.speed_y
        self.sprite.rotation = 90 - math.degrees(self.rotation)
        self.checkBoundaries()

"""
Trieda Spaceship
Hlavný objekt hry, predstavuje hráča
"""
class Spaceship(SpaceObject):
    #Todo 1: Presunťe metódy ktoré budú spoločné pre všetky objekty do triedy spaceObject
    """
    Každý frame sa vykoná táto metóda to znamená v našom prípade:
    60 simkov * za sekundu
    Mechanic of spaceship - rotation, movement, controls
    """
    def tick(self, dt):
        "Zrýchlenie po kliknutí klávesy W. Výpočet novej rýchlosti"
        if 'W' in pressed_keyboards:
            self.speed_x = self.speed_x + dt * ACCELERATION * math.cos(self.rotation)
            self.speed_y = self.speed_y + dt * ACCELERATION * math.sin(self.rotation)

        "Spomalenie/spätný chod po kliknutí klávesy S"
        if 'S' in pressed_keyboards:
            self.speed_x = self.speed_x - dt * ACCELERATION * math.cos(self.rotation)
            self.speed_y = self.speed_y - dt * ACCELERATION * math.sin(self.rotation)

        "Otočenie doľava - A"
        if 'A' in pressed_keyboards:
            self.rotation -= ROTATION_SPEED

        "Otočenie doprava - D"
        if 'D' in pressed_keyboards:
            self.rotation += ROTATION_SPEED

        "Ručná brzda - SHIFT"
        if 'SHIFT' in pressed_keyboards:
            self.speed_x = 0
            self.speed_y = 0

        "Posunutie vesmírnej lode na novú pozíciu"
        self.sprite.x += dt * self.speed_x
        self.sprite.y += dt * self.speed_y
        self.sprite.rotation = 90 - math.degrees(self.rotation)

        "Kontrola či sme prešli kraj"
        self.checkBoundaries()

"""
GAME WINDOW CLASS
"""
class Game:
    """
    Konstruktor
    """
    def __init__(self):
        self.window = None
        self.game_objects = []

    """
    Načítanie všetkých spritov
    """
    def load_resources(self):
        self.playerShip_image = pyglet.image.load('Assetss/PNG/playerShip1_blue.png')
        set_anchor_of_image_to_center(self.playerShip_image)
        self.background_image = pyglet.image.load('Assetss/Backgrounds/black.png')
        #Todo 2: Loadnutie viac typov asteroidov do listu
        self.asteridimages = ["Assetss/PNG/Meteors/meteorGrey_big1.png",
                              "Assetss/PNG/Meteors/meteorGrey_med1.png",
                              "Assetss/PNG/Meteors/meteorGrey_small1.png",
                              "Assetss/PNG/Meteors/meteorGrey_tiny1.png"]

    """
    Vytvorenie objektov pre začiatok hry
    """
    def init_objects(self):
        #Vytvorenie lode
        spaceShip = Spaceship(self.playerShip_image, WIDTH // 2, HEIGHT//2)  #
        self.game_objects.append(spaceShip)

        #Nastavenie pozadia a prescalovanie
        self.background = pyglet.sprite.Sprite(self.background_image)
        self.background.scale_x = 6
        self.background.scale_y = 4

        #Vytvorenie Meteoritov
        self.create_asteroids(7)
        #Todo 2

    def create_asteroids(self,count):
        "Vytvorenie X asteroidov"
        #Todo 2
        for i in range(count):
            img = pyglet.image.load(random.choice(self.asteridimages))
            set_anchor_of_image_to_center(img)

            position = [0,0]
            dimension = [WIDTH,HEIGHT]
            axis = random.choice([0,1])
            position[axis] = random.uniform(0,dimension[axis])

            tmp_speed_x = random.randint(-100,100)
            tmp_speed_y = random.randint(-100,100)

            asteroid = SpaceObject(img,position[0],position[1], tmp_speed_x,tmp_speed_y)
            self.game_objects.append(asteroid)
        pass

    """
    Event metóda ktorá sa volá na udalosť on_draw stále dookola
    """
    def draw_game(self):
        # Vymaže aktualny obsah okna
        self.window.clear()
        # Vykreslenie pozadia
        self.background.draw()

        # Táto časť sa stará o to aby bol prechod cez okraje okna plynulý a nie skokový
        for x_offset in (-self.window.width, 0, self.window.width):
            for y_offset in (-self.window.height, 0, self.window.height):
                # Remember the current state
                gl.glPushMatrix()
                # Move everything drawn from now on by (x_offset, y_offset, 0)
                gl.glTranslatef(x_offset, y_offset, 0)

                # Draw !!! -> Toto vykreslí všetky naše sprites
                batch.draw()

                # Restore remembered state (this cancels the glTranslatef)
                gl.glPopMatrix()

    """
    Event metóda pre spracovanie klávesových vstupov
    """
    def key_press(self, symbol, modifikatory):
        if symbol == key.W:
            pressed_keyboards.add('W')
        if symbol == key.S:
            pressed_keyboards.add('S')
        if symbol == key.A:
            pressed_keyboards.add('A')
        if symbol == key.D:
            pressed_keyboards.add('D')
        if symbol == key.LSHIFT:
            pressed_keyboards.add('SHIFT')

    """
    Event metóda pre spracovanie klávesových výstupov
    """
    def key_release(self, symbol, modifikatory):
        if symbol == key.W:
            pressed_keyboards.discard('W')
        if symbol == key.S:
            pressed_keyboards.discard('S')
        if symbol == key.A:
            pressed_keyboards.discard('A')
        if symbol == key.D:
            pressed_keyboards.discard('D')
        if symbol == key.LSHIFT:
            pressed_keyboards.discard('SHIFT')

    """
    Start game metóda 
    """
    def start(self):
        "Vytvorenie hlavneho okna"
        self.window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

        "Nastavenie udalosti (eventov)"
        self.window.push_handlers(
            on_draw=self.draw_game,
            on_key_press=self.key_press,
            on_key_release=self.key_release
        )

        "Load resources"
        self.load_resources()

        "Inicializacia objektov"
        self.init_objects()

        "Nastavenie timeru pre update všetkých objektov v intervale 1./60 = 60FPS"
        for object in self.game_objects:
            pyglet.clock.schedule_interval(object.tick, 1. / 60)
        pyglet.app.run()  # all is set, the game can start

"----------- StartGame -----------"
Game().start()