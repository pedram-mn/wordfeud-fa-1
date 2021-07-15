import math

import pygame as pg

pg.init()
width = pg.display.Info().current_h-100
screen = pg.display.set_mode((width, width))
screen.fill([17, 20, 26])  # set Gray color for background
pg.display.set_caption("WordFeud")
pg.display.flip()

blocks = {}
block_size = math.floor(width/20)

a = pg.load.image("logos\\ا.png")
alef = pg.load.image("logos\\آ.png")
be = pg.load.image("logos\\ب.png")
pe = pg.load.image("logos\\پ.png")
te = pg.load.image("logos\\ت.png")
se = pg.load.image("logos\\ث.png")
jim = pg.load.image("logos\\ج.png")
che = pg.load.image("logos\\چ.png")
he = pg.load.image("logos\\ح.png")
khe = pg.load.image("logos\\خ.png")
dal = pg.load.image("logos\\د.png")
zal = pg.load.image("logos\\ذ.png")
re = pg.load.image("logos\\ر.png")
ze = pg.load.image("logos\\ز.png")
zhe = pg.load.image("logos\\ژ.png")
sin = pg.load.image("logos\\س.png")
shin = pg.load.image("logos\\ش.png")
sad = pg.load.image("logos\\ص.png")
zad = pg.load.image("logos\\ض.png")
ta = pg.load.image("logos\\ط.png")
za = pg.load.image("logos\\ظ.png")
ein = pg.load.image("logos\\ع.png")
qein = pg.load.image("logos\\غ.png")
fe = pg.load.image("logos\\ف.png")
quf = pg.load.image("logos\\ق.png")
kaf = pg.load.image("logos\\ک.png")
gaf = pg.load.image("logos\\گ.png")
lam = pg.load.image("logos\\ل.png")
mim = pg.load.image("logos\\م.png")
nun = pg.load.image("logos\\ن.png")
vav = pg.load.image("logos\\و.png")
he2 = pg.load.image("logos\\ه.png")
ye = pg.load.image("logos\\ی.png")


def draw_grid():
    global blocks
    for x in range(int(width/8), int(width/8)+15*block_size, block_size):
        for y in range(int(width/8), int(width/8)+15*block_size, block_size):
            pg.draw.rect(screen, [0, 0, 0], pg.Rect(x, y, block_size, block_size), 1, border_radius=3)
            blocks[(int((x-int(width/8))/block_size)+1, int((y-int(width/8))/block_size)+1)] = (x, y)


done = False
while not done:
    main_border = pg.Rect(int(width/8), int(width/8), 15*block_size, 15*block_size)
    pg.draw.rect(screen, [24, 27, 31], main_border, 0, border_radius=2)
    pg.draw.rect(screen, [0, 0, 0], main_border, 2, border_radius=2)
    draw_grid()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
    pg.display.update()
