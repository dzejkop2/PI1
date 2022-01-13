import pyglet


#okno
from pyglet import gl

SIRKA = 1200
VYSKA = 900

#lobda
VELKOST_LOPTY = 20
RYCHLOST = 200 #px za sekundu

#palky
SIRKA_PALKY = 10
VYSKA_PALKY = 100
RYCHLOST_PALKY = RYCHLOST * 1,5

#prostredna ciara
CIARA_HRUBKA = 20

#font
VELKOST_FONTU = 42
ODSADENIE_TEXTU = 30

#stavove premenne
pozicia_palok = [VYSKA //2, VYSKA//2]
pozicia_lopty = [SIRKA //2,VYSKA //2]
rychlost_lopty = [0,0]
stisknute_klavesy = set()
SKORE = [0,0]


def vykresli_obdlznik(x1,y1,x2,y2):
    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex2f(int(x1), int(y1))
    gl.glVertex2f(int(x1), int(y2))
    gl.glVertex2f(int(x2), int(y2))
    gl.glVertex2f(int(x2), int(y1))
    gl.glEnd()

def vykresli_text(text, x, y, pozicia_x):
    napis = pyglet.text.Label(text,font_size= VELKOST_FONTU,x=x,y=y,anchor_x=pozicia_x)
    napis.draw()
def vykresli():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)
    gl.glColor3f(1,1,1)
    vykresli_obdlznik(
        pozicia_lopty[0] - VELKOST_LOPTY //2,
        pozicia_lopty[1] - VELKOST_LOPTY //2,
        pozicia_lopty[0] + VELKOST_LOPTY //2,
        pozicia_lopty[1] + VELKOST_LOPTY //2
    )


    for x, y in [(0, pozicia_palok[0]), (SIRKA, pozicia_palok[1])]:
        vykresli_obdlznik(
            x - SIRKA_PALKY,
            y - VYSKA_PALKY //2,
            x + SIRKA_PALKY,
            y + VYSKA_PALKY //2
        )
    for y in range(CIARA_HRUBKA //2, VYSKA, CIARA_HRUBKA * 2):
        vykresli_obdlznik(
            SIRKA // 2 - 1,
            y,
            SIRKA // 2 + 1,
            y + CIARA_HRUBKA
        )

    vykresli_text(str(SKORE[0]),x=ODSADENIE_TEXTU, y=VYSKA - ODSADENIE_TEXTU - VELKOST_FONTU, pozicia_x="left")
    vykresli_text(str(SKORE[1]),x=SIRKA - ODSADENIE_TEXTU, y=VYSKA - ODSADENIE_TEXTU - VELKOST_FONTU, pozicia_x="right")


window = pyglet.window.Window(width=SIRKA, height=VYSKA)
window.push_handlers(
    on_draw = vykresli,
)


pyglet.app.run()