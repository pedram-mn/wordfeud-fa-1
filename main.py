import pygame as pg
import math
import random as rnd
import numpy as np

pg.init()

# ########## SOME DISPLAY CONSTANTS ############
width = pg.display.Info().current_h - 100      #
block_size = math.floor(width / 20)            #
tile_size = math.floor(width / 15)             #
font = pg.font.SysFont("Simplified Arabic", block_size)  #
WHITE = (255, 255, 255)                        #
# ##############################################

# ######################################## WORDS ARRAYS #############################################
                                                                                                    #
with open("F:\\files\\projects\\Games\\wordfeud-fa\\words\\fa2.txt", "r", encoding='utf-8') as f:   #
    _2l_words = np.array(f.read().split("\n"))                                                      #
with open("F:\\files\\projects\\Games\\wordfeud-fa\\words\\fa3.txt", "r", encoding='utf-8') as f:   #
    _3l_words = np.array(f.read().split("\n"))                                                      #
with open("F:\\files\\projects\\Games\\wordfeud-fa\\words\\fa4.txt", "r", encoding='utf-8') as f:   #
    _4l_words = np.array(f.read().split("\n"))                                                      #
with open("F:\\files\\projects\\Games\\wordfeud-fa\\words\\fa5.txt", "r", encoding='utf-8') as f:   #
    _5l_words = np.array(f.read().split("\n"))                                                      #
with open("F:\\files\\projects\\Games\\wordfeud-fa\\words\\fa6.txt", "r", encoding='utf-8') as f:   #
    _6l_words = np.array(f.read().split("\n"))                                                      #
with open("F:\\files\\projects\\Games\\wordfeud-fa\\words\\fa7.txt", "r", encoding='utf-8') as f:   #
    _7l_words = np.array(f.read().split("\n"))                                                      #
with open("F:\\files\\projects\\Games\\wordfeud-fa\\words\\fa8.txt", "r", encoding='utf-8') as f:   #
    _8l_words = np.array(f.read().split("\n"))                                                      #
with open("F:\\files\\projects\\Games\\wordfeud-fa\\words\\fa9.txt", "r", encoding='utf-8') as f:   #
    _9l_words = np.array(f.read().split("\n"))                                                      #
with open("F:\\files\\projects\\Games\\wordfeud-fa\\words\\fa10.txt", "r", encoding='utf-8') as f:  #
    _10l_words = np.array(f.read().split("\n"))                                                     #
with open("F:\\files\\projects\\Games\\wordfeud-fa\\words\\fa11.txt", "r", encoding='utf-8') as f:  #
    _11l_words = np.array(f.read().split("\n"))                                                     #
with open("F:\\files\\projects\\Games\\wordfeud-fa\\words\\fa12.txt", "r", encoding='utf-8') as f:  #
    _12l_words = np.array(f.read().split("\n"))                                                     #
with open("F:\\files\\projects\\Games\\wordfeud-fa\\words\\fa13.txt", "r", encoding='utf-8') as f:  #
    _13l_words = np.array(f.read().split("\n"))                                                     #
with open("F:\\files\\projects\\Games\\wordfeud-fa\\words\\fa14.txt", "r", encoding='utf-8') as f:  #
    _14l_words = np.array(f.read().split("\n"))                                                     #
with open("F:\\files\\projects\\Games\\wordfeud-fa\\words\\fa15.txt", "r", encoding='utf-8') as f:  #
    _15l_words = np.array(f.read().split("\n"))                                                     #
                                                                                                    #
# ###################################################################################################

# ################# TEXTS ##################
                                           #
a_t = font.render("a", True, WHITE)        #
alef_t = font.render("A", True, WHITE)     #
be_t = font.render("be", True, WHITE)      #
pe_t = font.render("pe", True, WHITE)      #
te_t = font.render("te", True, WHITE)      #
se_t = font.render("se", True, WHITE)      #
jim_t = font.render("jim", True, WHITE)    #
che_t = font.render("che", True, WHITE)    #
he_t = font.render("ح", True, WHITE)       #
khe_t = font.render("khe", True, WHITE)    #
dal_t = font.render("dal", True, WHITE)    #
zal_t = font.render("zal", True, WHITE)    #
re_t = font.render("re", True, WHITE)      #
ze_t = font.render("ze", True, WHITE)      #
zhe_t = font.render("zhe", True, WHITE)    #
sin_t = font.render("sin", True, WHITE)    #
shin_t = font.render("shin", True, WHITE)  #
sad_t = font.render("sad", True, WHITE)    #
zad_t = font.render("zad", True, WHITE)    #
ta_t = font.render("ta", True, WHITE)      #
za_t = font.render("za", True, WHITE)      #
ein_t = font.render("ein", True, WHITE)    #
qein_t = font.render("qein", True, WHITE)  #
fe_t = font.render("fe", True, WHITE)      #
quf_t = font.render("quf", True, WHITE)    #
kaf_t = font.render("kaf", True, WHITE)    #
gaf_t = font.render("gaf", True, WHITE)    #
lam_t = font.render("lam", True, WHITE)    #
mim_t = font.render("mim", True, WHITE)    #
nun_t = font.render("nun", True, WHITE)    #
vav_t = font.render("vav", True, WHITE)    #
he2_t = font.render("he2", True, WHITE)    #
ye_t = font.render("ye", True, WHITE)      #
                                           #
# ##########################################

# ########################## LOAD ALPHABETS IMAGES ##############################
a = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ا.png")      #
a = pg.transform.scale(a, (tile_size - 4, tile_size - 4))                       #
alef = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\آ.png")   #
alef = pg.transform.scale(alef, (tile_size - 4, tile_size - 4))                 #
be = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ب.png")     #
be = pg.transform.scale(be, (tile_size - 4, tile_size - 4))                     #
pe = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\پ.png")     #
pe = pg.transform.scale(pe, (tile_size - 4, tile_size - 4))                     #
te = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ت.png")     #
te = pg.transform.scale(te, (tile_size - 4, tile_size - 4))                     #
se = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ث.png")     #
se = pg.transform.scale(se, (tile_size - 4, tile_size - 4))                     #
jim = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ج.png")    #
jim = pg.transform.scale(jim, (tile_size - 4, tile_size - 4))                   #
che = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\چ.png")    #
che = pg.transform.scale(che, (tile_size - 4, tile_size - 4))                   #
he = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ح.png")     #
he = pg.transform.scale(he, (tile_size - 4, tile_size - 4))                     #
khe = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\خ.png")    #
khe = pg.transform.scale(khe, (tile_size - 4, tile_size - 4))                   #
dal = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\د.png")    #
dal = pg.transform.scale(dal, (tile_size - 4, tile_size - 4))                   #
zal = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ذ.png")    #
zal = pg.transform.scale(zal, (tile_size - 4, tile_size - 4))                   #
re = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ر.png")     #
re = pg.transform.scale(re, (tile_size - 4, tile_size - 4))                     #
ze = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ز.png")     #
ze = pg.transform.scale(ze, (tile_size - 4, tile_size - 4))                     #
zhe = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ژ.png")    #
zhe = pg.transform.scale(zhe, (tile_size - 4, tile_size - 4))                   #
sin = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\س.png")    #
sin = pg.transform.scale(sin, (tile_size - 4, tile_size - 4))                   #
shin = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ش.png")   #
shin = pg.transform.scale(shin, (tile_size - 4, tile_size - 4))                 #
sad = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ص.png")    #
sad = pg.transform.scale(sad, (tile_size - 4, tile_size - 4))                   #
zad = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ض.png")    #
zad = pg.transform.scale(zad, (tile_size - 4, tile_size - 4))                   #
ta = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ط.png")     #
ta = pg.transform.scale(ta, (tile_size - 4, tile_size - 4))                     #
za = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ظ.png")     #
za = pg.transform.scale(za, (tile_size - 4, tile_size - 4))                     #
ein = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ع.png")    #
ein = pg.transform.scale(ein, (tile_size - 4, tile_size - 4))                   #
qein = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\غ.png")   #
qein = pg.transform.scale(qein, (tile_size - 4, tile_size - 4))                 #
fe = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ف.png")     #
fe = pg.transform.scale(fe, (tile_size - 4, tile_size - 4))                     #
quf = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ق.png")    #
quf = pg.transform.scale(quf, (tile_size - 4, tile_size - 4))                   #
kaf = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ک.png")    #
kaf = pg.transform.scale(kaf, (tile_size - 4, tile_size - 4))                   #
gaf = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\گ.png")    #
gaf = pg.transform.scale(gaf, (tile_size - 4, tile_size - 4))                   #
lam = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ل.png")    #
lam = pg.transform.scale(lam, (tile_size - 4, tile_size - 4))                   #
mim = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\م.png")    #
mim = pg.transform.scale(mim, (tile_size - 4, tile_size - 4))                   #
nun = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ن.png")    #
nun = pg.transform.scale(nun, (tile_size - 4, tile_size - 4))                   #
vav = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\و.png")    #
vav = pg.transform.scale(vav, (tile_size - 4, tile_size - 4))                   #
he2 = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ه.png")    #
he2 = pg.transform.scale(he2, (tile_size - 4, tile_size - 4))                   #
ye = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\ی.png")     #
ye = pg.transform.scale(ye, (tile_size - 4, tile_size - 4))                     #
                                                                                #
# ###############################################################################

change_tile_img = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\تعویض.png")
change_tile_img = pg.transform.scale(change_tile_img, (int(13*width/120), int(width/15)))
next_img = pg.image.load("F:\\files\\projects\\Games\\wordfeud-fa\\logos\\بعدی.png")
next_img = pg.transform.scale(next_img, (int(13*width/120), int(width/15)))

# ############################################# ALPHABETS DIFFERENT FORMATS ###############################################
                                                                                                                          #
alphabets = {a: a_t, alef: alef_t, be: be_t, pe: pe_t, te: te_t, se: se_t, jim: jim_t, che: che_t, he: he_t, khe: khe_t,  #
             dal: dal_t, zal: zal_t, re: re_t, ze: ze_t, zhe: zhe_t, sin: sin_t, shin: shin_t, sad: sad_t, zad: zad_t,    #
             ta: ta_t, za: za_t, ein: ein_t, qein: qein_t, fe: fe_t, quf: quf_t, kaf: kaf_t, gaf: gaf_t, lam: lam_t,      #
             mim: mim_t, nun: nun_t, vav: vav_t, he2: he2_t, ye: ye_t}                                                    #
                                                                                                                          #
alphabets_text = ["ا", "آ", "ب", "پ", "ف", "ث", "ج", "چ", "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض", "ط",   #
                  "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م", "ن", "و", "ه", "ی"]                                       #
                                                                                                                          #
alphabets_on_grid = {}                                                                                                    #
for n in range(1, 226):                                                                                                   #
    alphabets_on_grid[n] = None                                                                                           #
                                                                                                                          #
# #########################################################################################################################

pg.display.set_caption("WordFeud")

screen = pg.display.set_mode((width, width))
screen.fill([17, 20, 26])
pg.display.set_icon(kaf)
pg.display.flip()

blocks = {}
tiles = {}
tiles_to_fill = {}
found_words = {}
tiles_filling = []
score = 0


def draw_background():
    main_border = pg.Rect(int(width / 8), int(width / 8), 15 * block_size, 15 * block_size)
    tile_border = pg.Rect(int(width / 2) - 4 * tile_size, width - tile_size - int(width / 40), 8 * tile_size, tile_size)
    pg.draw.rect(screen, [24, 27, 31], main_border, 0, border_radius=2)
    pg.draw.rect(screen, [0, 0, 0], main_border, 2, border_radius=2)
    pg.draw.rect(screen, [79, 79, 79], tile_border, 0, border_radius=2)
    pg.draw.rect(screen, [0, 0, 0], tile_border, 2, border_radius=2)


def draw_grid():
    global blocks
    num = 1
    for y in range(int(width / 8), int(width / 8) + 15 * block_size, block_size):
        for x in range(int(width / 8), int(width / 8) + 15 * block_size, block_size):
            pg.draw.rect(screen, [0, 0, 0], pg.Rect(x, y, block_size, block_size), 1, border_radius=3)
            blocks[num] = (x, y)
            num += 1
    for pos in list(alphabets_on_grid.keys()):
        if alphabets_on_grid[pos] is not None:
            screen.blit(alphabets_on_grid[pos], blocks[pos])


def draw_tiles():
    global tiles, tiles_to_fill
    i = 1
    for x in range(int(width / 2) - 4 * tile_size, int(width / 2) + 4 * tile_size, tile_size):
        pg.draw.rect(screen, [0, 0, 0], pg.Rect(x, width - tile_size - int(width / 40), tile_size, tile_size), 1,
                     border_radius=3)
        tiles[i] = (x, width - tile_size - int(width / 40))
        tiles_to_fill[i] = (x + 2, width - tile_size - int(width / 40) + 2)
        i += 1


def start_tile():
    global tiles_filling
    for i in range(8):
        rnd_num = rnd.randint(0, 32)
        tiles_filling.append(rnd_num)


def put_tiles():
    global tiles_filling
    for i in range(1, len(tiles_filling) + 1):
        tile = list(alphabets.keys())[tiles_filling[i - 1]]
        screen.blit(tile, (tiles_to_fill[i]))


def move_tile(x, y):
    global tiles_filling, alphabets_on_grid
    for pos in tiles.keys():
        if x in range(tiles[pos][0], tiles[pos][0] + tile_size) and y in range(tiles[pos][1],
                                                                               tiles[pos][1] + tile_size):
            selected_tile = list(alphabets.keys())[tiles_filling[pos - 1]]
            click_count = 1
            while 1:
                for mouse_event in pg.event.get():
                    if mouse_event.type == pg.MOUSEBUTTONUP:
                        click_count = 2
                if click_count == 2:
                    for block in blocks.keys():
                        if pg.mouse.get_pos()[0] in range(blocks[block][0], blocks[block][0] + block_size) and \
                                pg.mouse.get_pos()[1] in range(blocks[block][1], blocks[block][1] + block_size):
                            alphabets_on_grid[block] = list(alphabets.values())[tiles_filling[pos - 1]]
                            del tiles_filling[pos - 1]
                            break
                    break
                screen.blit(selected_tile, pg.mouse.get_pos())
                pg.display.update()

                screen.fill([17, 20, 26])
                draw_background()
                draw_grid()
                draw_tiles()
                put_tiles()
                bars()


def find_word():
    global found_words, score
    word = ""
    # vertical search
    for i in range(1, 16):
        for j in range(i, 226, 15):
            if alphabets_on_grid[j] in list(alphabets.values()):
                word += alphabets_text[list(alphabets.values()).index(alphabets_on_grid[j])]
                if j == i+14*15:
                    if len(word) > 1 and (j-(len(word)-1)*15, j) not in list(found_words.keys()):
                        length = len(word)
                        if length == 2:
                            if word in _2l_words:
                                score += 2
                                found_words[(j-15, j)] = word
                        if length == 3:
                            if word in _3l_words:
                                score += 3
                                found_words[(j-30, j)] = word
                        if length == 4:
                            if word in _4l_words:
                                score += 4
                                found_words[(j-45, j)] = word
                        if length == 5:
                            if word in _5l_words:
                                score += 5
                                found_words[(j-60, j)] = word
                        if length == 6:
                            if word in _6l_words:
                                score += 6
                                found_words[(j-75, j)] = word
                        if length == 7:
                            if word in _7l_words:
                                score += 7
                                found_words[(j-90, j)] = word
                        if length == 8:
                            if word in _8l_words:
                                score += 8
                                found_words[(j-105, j)] = word
                        if length == 9:
                            if word in _9l_words:
                                score += 9
                                found_words[(j-120, j)] = word
                        if length == 10:
                            if word in _10l_words:
                                score += 10
                                found_words[(j-135, j)] = word
                        if length == 11:
                            if word in _11l_words:
                                score += 11
                                found_words[(j-150, j)] = word
                        if length == 12:
                            if word in _12l_words:
                                score += 12
                                found_words[(j-165, j)] = word
                        if length == 13:
                            if word in _13l_words:
                                score += 13
                                found_words[(j-180, j)] = word
                        if length == 14:
                            if word in _14l_words:
                                score += 14
                                found_words[(j-195, j)] = word
                        if length == 15:
                            if word in _15l_words:
                                score += 15
                                found_words[(j-210, j)] = word
                        word = ""
        
                elif alphabets_on_grid[j+15] not in list(alphabets.values()):
                    if len(word) > 1 and (j-(len(word)-1)*15, j) not in list(found_words.keys()):
                        length = len(word)
                        if length == 2:
                            if word in _2l_words:
                                score += 2
                                found_words[(j-15, j)] = word
                        if length == 3:
                            if word in _3l_words:
                                score += 3
                                found_words[(j-30, j)] = word
                        if length == 4:
                            if word in _4l_words:
                                score += 4
                                found_words[(j-45, j)] = word
                        if length == 5:
                            if word in _5l_words:
                                score += 5
                                found_words[(j-60, j)] = word
                        if length == 6:
                            if word in _6l_words:
                                score += 6
                                found_words[(j-75, j)] = word
                        if length == 7:
                            if word in _7l_words:
                                score += 7
                                found_words[(j-90, j)] = word
                        if length == 8:
                            if word in _8l_words:
                                score += 8
                                found_words[(j-105, j)] = word
                        if length == 9:
                            if word in _9l_words:
                                score += 9
                                found_words[(j-120, j)] = word
                        if length == 10:
                            if word in _10l_words:
                                score += 10
                                found_words[(j-135, j)] = word
                        if length == 11:
                            if word in _11l_words:
                                score += 11
                                found_words[(j-150, j)] = word
                        if length == 12:
                            if word in _12l_words:
                                score += 12
                                found_words[(j-165, j)] = word
                        if length == 13:
                            if word in _13l_words:
                                score += 13
                                found_words[(j-180, j)] = word
                        if length == 14:
                            if word in _14l_words:
                                score += 14
                                found_words[(j-195, j)] = word
                        if length == 15:
                            if word in _15l_words:
                                score += 15
                                found_words[(j-210, j)] = word
                        word = ""
        word = ""

    # horizental search
    word = ""
    for i in range(1, 212, 15):
        for j in range(i, i+15):
            if alphabets_on_grid[j] in list(alphabets.values()):
                word += alphabets_text[list(alphabets.values()).index(alphabets_on_grid[j])]
                if j == i+14:
                    if len(word) > 1 and (j-len(word)+1, j) not in list(found_words.keys()):
                        length = len(word)
                        if length == 2:
                            if word in _2l_words:
                                score += 2
                                found_words[(j-1, j)] = word
                        if length == 3:
                            if word in _3l_words:
                                score += 3
                                found_words[(j-2, j)] = word
                        if length == 4:
                            if word in _4l_words:
                                score += 4
                                found_words[(j-3, j)] = word
                        if length == 5:
                            if word in _5l_words:
                                score += 5
                                found_words[(j-4, j)] = word
                        if length == 6:
                            if word in _6l_words:
                                score += 6
                                found_words[(j-5, j)] = word
                        if length == 7:
                            if word in _7l_words:
                                score += 7
                                found_words[(j-6, j)] = word
                        if length == 8:
                            if word in _8l_words:
                                score += 8
                                found_words[(j-7, j)] = word
                        if length == 9:
                            if word in _9l_words:
                                score += 9
                                found_words[(j-8, j)] = word
                        if length == 10:
                            if word in _10l_words:
                                score += 10
                                found_words[(j-9, j)] = word
                        if length == 11:
                            if word in _11l_words:
                                score += 11
                                found_words[(j-10, j)] = word
                        if length == 12:
                            if word in _12l_words:
                                score += 12
                                found_words[(j-11, j)] = word
                        if length == 13:
                            if word in _13l_words:
                                score += 13
                                found_words[(j-12, j)] = word
                        if length == 14:
                            if word in _14l_words:
                                score += 14
                                found_words[(j-13, j)] = word
                        if length == 15:
                            if word in _15l_words:
                                score += 15
                                found_words[(j-14, j)] = word
                        word = ""
                elif alphabets_on_grid[j+1] not in list(alphabets.values()):
                    if len(word) > 1 and (j-len(word)+1, j) not in list(found_words.keys()):
                        length = len(word)
                        if length == 2:
                            if word in _2l_words:
                                score += 2
                                found_words[(j-1, j)] = word
                        if length == 3:
                            if word in _3l_words:
                                score += 3
                                found_words[(j-2, j)] = word
                        if length == 4:
                            if word in _4l_words:
                                score += 4
                                found_words[(j-3, j)] = word
                        if length == 5:
                            if word in _5l_words:
                                score += 5
                                found_words[(j-4, j)] = word
                        if length == 6:
                            if word in _6l_words:
                                score += 6
                                found_words[(j-5, j)] = word
                        if length == 7:
                            if word in _7l_words:
                                score += 7
                                found_words[(j-6, j)] = word
                        if length == 8:
                            if word in _8l_words:
                                score += 8
                                found_words[(j-7, j)] = word
                        if length == 9:
                            if word in _9l_words:
                                score += 9
                                found_words[(j-8, j)] = word
                        if length == 10:
                            if word in _10l_words:
                                score += 10
                                found_words[(j-9, j)] = word
                        if length == 11:
                            if word in _11l_words:
                                score += 11
                                found_words[(j-10, j)] = word
                        if length == 12:
                            if word in _12l_words:
                                score += 12
                                found_words[(j-11, j)] = word
                        if length == 13:
                            if word in _13l_words:
                                score += 13
                                found_words[(j-12, j)] = word
                        if length == 14:
                            if word in _14l_words:
                                score += 14
                                found_words[(j-13, j)] = word
                        if length == 15:
                            if word in _15l_words:
                                score += 15
                                found_words[(j-14, j)] = word
                        word = ""
        word = ""


def next_round():
    if mouse_pos[0] in range(int(2*width/15)+15*block_size,  int(29*width/120)+15*block_size) and mouse_pos[1] in range(int(width/8), int(23*width/120)):
        find_word()


def bars():
    top_bar = pg.Rect(int(width/8), int(width/40), 15*block_size, int(width/15))
    reset_tile_bar = pg.Rect(int(width/120)-2, int(width/8)-2, int(13*width/120)+4, int(width/15)+4)
    next_bar = pg.Rect(int(2*width/15)+15*block_size-2, int(width/8)-2, int(13*width/120)+4, int(width/15)+4)
    pg.draw.rect(screen, [54, 54, 54], top_bar, 0, border_radius=3)
    pg.draw.rect(screen, [0, 0, 0], top_bar, 2, border_radius=3)
    pg.draw.line(screen, [0, 0, 0], (int(width/2), int(width/40)), (int(width/2), int(11*width/120)-1), 2)
    pg.draw.rect(screen, [0, 0, 0], reset_tile_bar, 2, border_radius=3)
    pg.draw.rect(screen, [0, 0, 0], next_bar, 2, border_radius=3)
    screen.blit(font.render("Score : %s" % str(score), True, WHITE), (int(width/8)+5, int(width/60)))
    screen.blit(font.render("Words found : %s" % str(len(found_words.values())), True, WHITE), (int(width/2)+5, int(width/60)))
    screen.blit(change_tile_img, (int(width/120), int(width/8)))
    screen.blit(next_img, (int(2*width/15)+15*block_size, int(width/8)))


def reset_tile():
    global tiles_filling
    if mouse_pos[0] in range(int(width/120),  int(7*width/60)) and mouse_pos[1] in range(int(width/8), int(23*width/120)):
        for i in range(len(tiles_filling)):
            tiles_filling[i] = rnd.randint(0, 32)


start_tile()
done = False
while not done:
    mouse_pos = pg.mouse.get_pos()
    draw_background()
    draw_grid()
    draw_tiles()
    put_tiles()
    bars()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:
                reset_tile()
                move_tile(mouse_pos[0], mouse_pos[1])
                next_round()

    pg.display.update()
print(found_words)
