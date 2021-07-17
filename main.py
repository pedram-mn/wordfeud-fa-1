import math
import pygame as pg
import random as rnd
import time
pg.init()
pg.font.init()

pg.display.set_caption("WordFeud")

width = pg.display.Info().current_h-100
screen = pg.display.set_mode((width, width))
screen.fill([17, 20, 26])
pg.display.flip()

blocks = {}
block_size = math.floor(width/20)

tiles = {}
tile_size = math.floor(width/15)

font = pg.font.SysFont("vivaldi", tile_size)

# alef_t = font.render("F", True, (255, 255, 255))

a = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ا.png")
a = pg.transform.scale(a, (tile_size-4, tile_size-4))
alef = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\آ.png")
alef = pg.transform.scale(alef, (tile_size-4, tile_size-4))
be = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ب.png")
be = pg.transform.scale(be, (tile_size-4, tile_size-4))
pe = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\پ.png")
pe = pg.transform.scale(pe, (tile_size-4, tile_size-4))
# te = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ت.png")
# se = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ث.png")
# jim = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ج.png")
# che = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\چ.png")
# he = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ح.png")
# khe = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\خ.png")
# dal = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\د.png")
# zal = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ذ.png")
# re = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ر.png")
# ze = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ز.png")
# zhe = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ژ.png")
# sin = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\س.png")
# shin = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ش.png")
# sad = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ص.png")
# zad = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ض.png")
# ta = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ط.png")
# za = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ظ.png")
# ein = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ع.png")
# qein = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\غ.png")
# fe = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ف.png")
# quf = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ق.png")
# kaf = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ک.png")
# gaf = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\گ.png")
# lam = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ل.png")
# mim = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\م.png")
# nun = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ن.png")
# vav = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\و.png")
# he2 = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ه.png")
# ye = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ی.png")

alphabets_tile = [a, alef, be, pe]
    # , te, se, jim, che, he, khe, dal, zal, re, ze, zhe, sin, shin, sad, zad, ta, za, ein,
    #               qein, fe, quf, kaf, gaf, lam, mim, nun, vav, he2, ye]

# alphabets_texts = [a_t, alef_t, be_t, pe_t, te_t, se_t, jim_t, che_t, he_t, khe_t, dal_t, zal_t, re_t, ze_t, zhe_t,
#                    sin_t, shin_t, sad_t, zad_t, ta_t, za_t, ein_t, qein_t, fe_t, quf_t, kaf_t, gaf_t, lam_t, mim_t,
#                    nun_t, vav_t, he2_t, ye_t]


def draw_tiles():
    global tiles
    i = 1
    for x in range(int(width/2)-4*tile_size, int(width/2)+4*tile_size, tile_size):
        pg.draw.rect(screen, [0, 0, 0], pg.Rect(x, width-tile_size-int(width/40), tile_size, tile_size), 1,
                     border_radius=3)
        tiles[i] = (x, width-tile_size-int(width/40))
        i += 1


tiles_filling = [1, 2, 0, 3]


def reset_tile():
    global tiles_filling
    for i in range(8):
        tiles_filling[i] = rnd.randint(0, 32)


def put_tiles():
    global tiles_filling
    for i in range(1, 5):
        tile = alphabets_tile[tiles_filling[i-1]]
        screen.blit(tile, (tiles[i][0]+2, tiles[i][1]+2))


def draw_grid():
    global blocks
    for x in range(int(width/8), int(width/8)+15*block_size, block_size):
        for y in range(int(width/8), int(width/8)+15*block_size, block_size):
            pg.draw.rect(screen, [0, 0, 0], pg.Rect(x, y, block_size, block_size), 1, border_radius=3)
            blocks[(int((x-int(width/8))/block_size)+1, int((y-int(width/8))/block_size)+1)] = (x, y)


def selected_tile(x, y):
    for pos in tiles.keys():
        if x in range(tiles[pos][0], tiles[pos][0]+tile_size) and y in range(tiles[pos][1], tiles[pos][1]+tile_size):
            mouse_on = True
            while mouse_on:
                # screen.blit(alphabets_tile[tiles_filling[pos-1]], pg.mouse.get_pos())
                print(pg.mouse.get_pos())
                time.sleep(0.2)
                # pg.display.update()
            # for block in blocks.keys():
            #     if pg.mouse.get_pos()[0] in range(blocks[block][0], blocks[block][0]+block_size) and \
            #             pg.mouse.get_pos()[1] in range(blocks[block][1], blocks[block][1]+block_size):
            #         screen.blit(alphabets_tile[tiles_filling[pos-1]], blocks[block])
            #         break


done = False
while not done:

    main_border = pg.Rect(int(width/8), int(width/8), 15*block_size, 15*block_size)
    tile_border = pg.Rect(int(width/2)-4*tile_size,  width-tile_size-int(width/40), 8*tile_size, tile_size)
    pg.draw.rect(screen, [24, 27, 31], main_border, 0, border_radius=2)
    pg.draw.rect(screen, [0, 0, 0], main_border, 2, border_radius=2)
    pg.draw.rect(screen, [79, 79, 79], tile_border, 0, border_radius=2)
    pg.draw.rect(screen, [0, 0, 0], tile_border, 2, border_radius=2)

    mouse_pos = pg.mouse.get_pos()
    draw_grid()
    draw_tiles()
    put_tiles()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                selected_tile(mouse_pos[0], mouse_pos[1])
    pg.display.update()
