import pyglet
import math

window = pyglet.window.Window(width=800, height= 600)


def zpracuj_text(text):
    snake.x

def tik(t):
    snake.x = snake.x + t * 20
    snake.y = snake.y + 20 * math.sin(snake.x / 5)
    snake.rotation = 10
obrazok2 = pyglet.image.load("snek1.jpg")

def zmen(t):
    snake.image = obrazok2
    pyglet.clock.schedule_once(zmen_spet, 3)


def zmen_spet(t):
    snake.image = obrazok
    pyglet.clock.schedule_once(zmen, 3)


obrazok = pyglet.image.load("snake.jpg")
snake = pyglet.sprite.Sprite(obrazok)
pyglet.clock.schedule_once(zmen, 3)
def vykresli():
    window.clear()
    snake.draw()

def klik(x,y,tlacitko,mod):
    snake.x = x
    snake.y = y
    print(tlacitko)
    print(x)
    print(y)
    print(mod)



window.push_handlers(
    on_text=zpracuj_text,
    on_draw=vykresli,
    on_mouse_press=klik
)

pyglet.clock.schedule_interval(tik, 1/30)

pyglet.app.run()