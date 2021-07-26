import pygame as pg
import math
import random as rnd
import numpy as np
from pygame.event import clear

pg.init()

width = pg.display.Info().current_h - 100      
block_size = math.floor(width / 20)            
tile_size = math.floor(width / 15)             
font = pg.font.SysFont("Simplified Arabic", block_size)  
WHITE = (255, 255, 255)                        
                                                                                           
with open("words\\fa2.txt", "r", encoding='utf-8') as f:   
    _2l_words = np.array(f.read().split("\n"))                                                      
with open("words\\fa3.txt", "r", encoding='utf-8') as f:   
    _3l_words = np.array(f.read().split("\n"))                                                      
with open("words\\fa4.txt", "r", encoding='utf-8') as f:   
    _4l_words = np.array(f.read().split("\n"))                                                      
with open("words\\fa5.txt", "r", encoding='utf-8') as f:   
    _5l_words = np.array(f.read().split("\n"))                                                      
with open("words\\fa6.txt", "r", encoding='utf-8') as f:   
    _6l_words = np.array(f.read().split("\n"))                                                      
with open("words\\fa7.txt", "r", encoding='utf-8') as f:   
    _7l_words = np.array(f.read().split("\n"))                                                      
with open("words\\fa8.txt", "r", encoding='utf-8') as f:   
    _8l_words = np.array(f.read().split("\n"))                                                      
with open("words\\fa9.txt", "r", encoding='utf-8') as f:   
    _9l_words = np.array(f.read().split("\n"))                                                      
with open("words\\fa10.txt", "r", encoding='utf-8') as f:  
    _10l_words = np.array(f.read().split("\n"))                                                     
with open("words\\fa11.txt", "r", encoding='utf-8') as f:  
    _11l_words = np.array(f.read().split("\n"))                                                     
with open("words\\fa12.txt", "r", encoding='utf-8') as f:  
    _12l_words = np.array(f.read().split("\n"))                                                     
with open("words\\fa13.txt", "r", encoding='utf-8') as f:  
    _13l_words = np.array(f.read().split("\n"))                                                     
with open("words\\fa14.txt", "r", encoding='utf-8') as f:  
    _14l_words = np.array(f.read().split("\n"))                                                     
with open("words\\fa15.txt", "r", encoding='utf-8') as f:  
    _15l_words = np.array(f.read().split("\n"))                                                     

a = pg.image.load("logos\\ا.png")      
a = pg.transform.scale(a, (tile_size - 4, tile_size - 4))                       
alef = pg.image.load("logos\\آ.png")   
alef = pg.transform.scale(alef, (tile_size - 4, tile_size - 4))                 
be = pg.image.load("logos\\ب.png")     
be = pg.transform.scale(be, (tile_size - 4, tile_size - 4))                     
pe = pg.image.load("logos\\پ.png")     
pe = pg.transform.scale(pe, (tile_size - 4, tile_size - 4))                     
te = pg.image.load("logos\\ت.png")     
te = pg.transform.scale(te, (tile_size - 4, tile_size - 4))                     
se = pg.image.load("logos\\ث.png")     
se = pg.transform.scale(se, (tile_size - 4, tile_size - 4))                     
jim = pg.image.load("logos\\ج.png")    
jim = pg.transform.scale(jim, (tile_size - 4, tile_size - 4))                   
che = pg.image.load("logos\\چ.png")    
che = pg.transform.scale(che, (tile_size - 4, tile_size - 4))                   
he = pg.image.load("logos\\ح.png")     
he = pg.transform.scale(he, (tile_size - 4, tile_size - 4))                     
khe = pg.image.load("logos\\خ.png")    
khe = pg.transform.scale(khe, (tile_size - 4, tile_size - 4))                   
dal = pg.image.load("logos\\د.png")    
dal = pg.transform.scale(dal, (tile_size - 4, tile_size - 4))                   
zal = pg.image.load("logos\\ذ.png")    
zal = pg.transform.scale(zal, (tile_size - 4, tile_size - 4))                   
re = pg.image.load("logos\\ر.png")     
re = pg.transform.scale(re, (tile_size - 4, tile_size - 4))                     
ze = pg.image.load("logos\\ز.png")     
ze = pg.transform.scale(ze, (tile_size - 4, tile_size - 4))                     
zhe = pg.image.load("logos\\ژ.png")    
zhe = pg.transform.scale(zhe, (tile_size - 4, tile_size - 4))                   
sin = pg.image.load("logos\\س.png")    
sin = pg.transform.scale(sin, (tile_size - 4, tile_size - 4))                   
shin = pg.image.load("logos\\ش.png")   
shin = pg.transform.scale(shin, (tile_size - 4, tile_size - 4))                 
sad = pg.image.load("logos\\ص.png")    
sad = pg.transform.scale(sad, (tile_size - 4, tile_size - 4))                   
zad = pg.image.load("logos\\ض.png")    
zad = pg.transform.scale(zad, (tile_size - 4, tile_size - 4))                   
ta = pg.image.load("logos\\ط.png")     
ta = pg.transform.scale(ta, (tile_size - 4, tile_size - 4))                     
za = pg.image.load("logos\\ظ.png")     
za = pg.transform.scale(za, (tile_size - 4, tile_size - 4))                     
ein = pg.image.load("logos\\ع.png")    
ein = pg.transform.scale(ein, (tile_size - 4, tile_size - 4))                   
qein = pg.image.load("logos\\غ.png")   
qein = pg.transform.scale(qein, (tile_size - 4, tile_size - 4))                 
fe = pg.image.load("logos\\ف.png")     
fe = pg.transform.scale(fe, (tile_size - 4, tile_size - 4))                     
quf = pg.image.load("logos\\ق.png")    
quf = pg.transform.scale(quf, (tile_size - 4, tile_size - 4))
kaf = pg.image.load("logos\\ک.png")    
kaf = pg.transform.scale(kaf, (tile_size - 4, tile_size - 4))                   
gaf = pg.image.load("logos\\گ.png")    
gaf = pg.transform.scale(gaf, (tile_size - 4, tile_size - 4))                   
lam = pg.image.load("logos\\ل.png")    
lam = pg.transform.scale(lam, (tile_size - 4, tile_size - 4))                   
mim = pg.image.load("logos\\م.png")    
mim = pg.transform.scale(mim, (tile_size - 4, tile_size - 4))                   
nun = pg.image.load("logos\\ن.png")    
nun = pg.transform.scale(nun, (tile_size - 4, tile_size - 4))                   
vav = pg.image.load("logos\\و.png")    
vav = pg.transform.scale(vav, (tile_size - 4, tile_size - 4))                   
he2 = pg.image.load("logos\\ه.png")
he2 = pg.transform.scale(he2, (tile_size - 4, tile_size - 4))    
ye = pg.image.load("logos\\ی.png")     
ye = pg.transform.scale(ye, (tile_size - 4, tile_size - 4))

change_tile_img = pg.image.load("logos\\تعویض.png")
change_tile_img = pg.transform.scale(change_tile_img, (int(13*width/120), int(width/15)))
next_img = pg.image.load("logos\\بعدی.png")
next_img = pg.transform.scale(next_img, (int(13*width/120), int(width/15)))
clear_img = pg.image.load("logos\\پاک.png")
clear_img = pg.transform.scale(clear_img, (int(13*width/120), int(width/15)))
                                                                                                                          
alphabets = {a: "ا", alef: "آ", be: "ب", pe: "پ", te: "ت", se: "ث", jim: "ج", che: "چ", he: "ح", khe: "خ", dal: "د",     
             zal: "ذ", re: "ر", ze: "ز", zhe: "ژ", sin: "س", shin: "ش", sad: "ص", zad: "ض", ta: "ط", za: "ظ", ein: "ع",  
             qein: "غ", fe: "ف", quf: "ق", kaf: "ک", gaf: "گ", lam: "ل", mim: "م", nun: "ن", vav: "و", he2: "ه", ye: "ی"}                                                    
                                                                                                                          
alphabets_on_grid = {}                                                                                                    
for n in range(1, 226):                                                                                                   
    alphabets_on_grid[n] = None                                                                                           

test = []
for n in range(1, 226):   
    test.append(alphabets_on_grid[n])
del test

scores = {"ا": 1, "آ": 1, "ب": 1, "پ": 2, "ت": 1, "ث": 3, "ج": 2, "چ": 1, "ح": 3, "خ": 2, "د": 2, "ذ": 5, "ر": 1, "ز": 2,
          "ژ": 10, "س": 1, "ش": 2, "ص": 2, "ض": 3, "ط": 4, "ظ": 5, "ع": 3 ,"غ": 3, "ف": 2, "ق": 3, "ک": 2, "گ": 2, "ل": 5,
          "م": 2, "ن": 2, "و": 1, "ه": 2, "ی": 2}

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
new_on_grid = {}
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
            index = list(alphabets.values()).index(alphabets_on_grid[pos])
            screen.blit(pg.transform.scale(list(alphabets.keys())[index], (block_size-4, block_size-4)), (blocks[pos][0]+2, blocks[pos][1]+2))


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
        tiles_filling.append(rnd.randint(0, 32))


def put_tiles():
    for i in range(1, len(tiles_filling) + 1):
        tile = list(alphabets.keys())[tiles_filling[i - 1]]
        screen.blit(tile, (tiles_to_fill[i]))


def move_tile(x, y):
    global tiles_filling, alphabets_on_grid
    for pos in range(1, len(tiles_filling)+1):
        if x in range(tiles[pos][0], tiles[pos][0] + tile_size) and y in range(tiles[pos][1],
                                                                               tiles[pos][1] + tile_size):
            selected_tile = list(alphabets.keys())[tiles_filling[pos - 1]]
            click_count = 1
            while True:
                for mouse_event in pg.event.get():
                    if mouse_event.type == pg.MOUSEBUTTONUP:
                        click_count = 2
                if click_count == 2:
                    for block in blocks.keys():
                        if pg.mouse.get_pos()[0] in range(blocks[block][0], blocks[block][0] + block_size) and \
                                pg.mouse.get_pos()[1] in range(blocks[block][1], blocks[block][1] + block_size):
                            if alphabets_on_grid[block] is None:
                                alphabets_on_grid[block] = list(alphabets.values())[tiles_filling[pos - 1]]
                                new_on_grid[block] = alphabets_on_grid[block]
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
    word_stat = None
    return_stat = True
    false_words = []
    new_words = {}
    # vertical search
    for i in range(1, 16):  # select x value of grid
        for j in range(i, 226, 15):  # change y value in a column (up -> down)
            if alphabets_on_grid[j] in list(alphabets.values()):  # check if any alphabet assigns to that block
                word += alphabets_on_grid[j]  # add alphabet to word to make it
                if j == i+14*15:  # check if y value of grid is the last one of the column
                    if len(word) > 1 and (j-(len(word)-1)*15, j) not in list(found_words.keys()):  # check lenght of word if its bigger than 1 and not found before
                        new_words[(j-(len(word)-1)*15, j)] = word
                        # reset word value for next check
                        word = ""
        
                elif alphabets_on_grid[j+15] not in list(alphabets.values()):  # check if next block is empty to recognize the end of the word (checked if last "if" doesn't run)
                    if len(word) > 1 and (j-(len(word)-1)*15, j) not in list(found_words.keys()):  # check lenght of word if its bigger than 1 and not found before
                        new_words[(j-(len(word)-1)*15, j)] = word
                        # reset word value for next check
                        word = ""
            else:
                word = ""
        word = ""
    # horizental search
    for i in range(1, 212, 15):  # select y value of grid
        for j in range(i+14, i-1, -1):  # change x value in a row (right -> left)
            if alphabets_on_grid[j] in list(alphabets.values()):  # check if any alphabet assigns to that block
                word += alphabets_on_grid[j]  # add alphabet to word to make it
                if j == i:  # check if x value of grid is the last one of the row
                    if len(word) > 1 and (j+len(word)-1, j) not in list(found_words.keys()):  # check lenght of word if its bigger than 1 and not found before
                        new_words[(j+len(word)-1, j)] = word
                        # reset word value for next check
                        word = ""
                
                elif alphabets_on_grid[j-1] not in list(alphabets.values()):  # check if next block is empty to recognize the end of the word (checked if last "if" doesn't run)
                    if len(word) > 1 and (j+len(word)-1, j) not in list(found_words.keys()):  # check lenght of word if its bigger than 1 and not found before
                        new_words[(j+len(word)-1, j)] = word
                        # reset word value for next check
                        word = ""
            else:
                word = ""
        word = ""
    # check words that found in new round
    for i, new_word in enumerate(list(new_words.values())):
        length = len(new_word)
        # check that the word is in the dictionary or not
        # if it is, add the word to found_words and change word_stat status to true
        # if not, add the word to false_words to show it later to player and change word_stat status to false
        if length == 2:
            if new_word in _2l_words:
                word_stat = True
            else:
                word_stat = False
        if length == 3:
            if new_word in _3l_words:
                word_stat = True
            else:
                word_stat = False
        if length == 4:
            if new_word in _4l_words:
                word_stat = True
            else:
                word_stat = False
        if length == 5:
            if new_word in _5l_words:
                word_stat = True
            else:
                word_stat = False
        if length == 6:
            if new_word in _6l_words:
                word_stat = True
            else:
                word_stat = False
        if length == 7:
            if new_word in _7l_words:
                word_stat = True
            else:
                word_stat = False
        if length == 8:
            if new_word in _8l_words:
                word_stat = True
            else:
                word_stat = False
        if length == 9:
            if new_word in _9l_words:
                word_stat = True
            else:
                word_stat = False
        if length == 10:
            if new_word in _10l_words:
                word_stat = True
            else:
                word_stat = False
        if length == 11:
            if new_word in _11l_words:
                word_stat = True
            else:
                word_stat = False
        if length == 12:
            if new_word in _12l_words:
                word_stat = True
            else:
                word_stat = False
        if length == 13:
            if new_word in _13l_words:
                word_stat = True
            else:
                word_stat = False
        if length == 14:
            if new_word in _14l_words:
                word_stat = True
            else:
                word_stat = False
        if length == 15:
            if new_word in _15l_words:
                word_stat = True
            else:
                word_stat = False
        if word_stat is False:
            false_words.append(new_word)
            del new_words[list(new_words.keys())[i]]
            return_stat = False
        else:
            found_words[list(new_words.keys())[i]] = new_word

    return (False, false_words) if not return_stat else (True, list(new_words.values()))


def next_round():
    global new_on_grid, tiles_filling, score
    if mouse_pos[0] in range(int(2*width/15)+15*block_size,  int(29*width/120)+15*block_size) and mouse_pos[1] in range(int(width/8), int(23*width/120)):
        stat = find_word()
        if stat[0]:
            new_on_grid.clear()
            for word in stat[1]:
                for i in word:
                    score += scores[i]
            for i in range(8-len(tiles_filling)):
                tiles_filling.append(rnd.randint(0, 32))


def bars():

    top_bar = pg.Rect(int(width/8), int(width/40), 15*block_size, int(width/15))
    pg.draw.rect(screen, [54, 54, 54], top_bar, 0, border_radius=3)
    pg.draw.rect(screen, [0, 0, 0], top_bar, 2, border_radius=3)
    pg.draw.line(screen, [0, 0, 0], (int(width/2), int(width/40)), (int(width/2), int(11*width/120)-1), 2)
    screen.blit(font.render("Score : %i" % score, True, WHITE), (int(width/8)+5, int(width/60)))
    screen.blit(font.render("Words : %i" % len(found_words.values()), True, WHITE), (int(width/2)+5, int(width/60)))

    change_bar = pg.Rect(int(width/120)-2, int(width/8)-2, int(13*width/120)+4, int(width/15)+4)
    pg.draw.rect(screen, [0, 0, 0], change_bar, 2, border_radius=3)
    screen.blit(change_tile_img, (int(width/120), int(width/8)))

    next_bar = pg.Rect(int(2*width/15)+15*block_size-2, int(width/8)-2, int(13*width/120)+4, int(width/15)+4)
    pg.draw.rect(screen, [0, 0, 0], next_bar, 2, border_radius=3)
    screen.blit(next_img, (int(2*width/15)+15*block_size, int(width/8)))
    
    clear_bar = pg.Rect(int(2*width/15)+15*block_size-2, int(5*width/24)-2, int(13*width/120)+4, int(width/15)+4)
    pg.draw.rect(screen, [0, 0, 0], clear_bar, 2, border_radius=3)
    screen.blit(clear_img, (int(2*width/15)+15*block_size, int(5*width/24)))


def reset_tile():
    global tiles_filling, new_on_grid
    if mouse_pos[0] in range(int(width/120),  int(7*width/60)) and mouse_pos[1] in range(int(width/8), int(23*width/120)):
        for pos in list(new_on_grid.keys()):
            tiles_filling.append(list(alphabets.values()).index(new_on_grid[pos]))
            del new_on_grid[pos], alphabets_on_grid[pos]
        for i in range(len(tiles_filling)):
            tiles_filling[i] = rnd.randint(0, 32)


def clear_grid():
    global new_on_grid, tiles_filling, alphabets_on_grid
    if mouse_pos[0] in range(int(2*width/15)+15*block_size,  int(29*width/120)+15*block_size) and mouse_pos[1] in range(int(5*width/24), int(11*width/40)):
        for pos in list(new_on_grid.keys()):
            tiles_filling.append(list(alphabets.values()).index(new_on_grid[pos]))
            del new_on_grid[pos]
            alphabets_on_grid[pos] = None


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
                clear_grid()
                reset_tile()
                move_tile(mouse_pos[0], mouse_pos[1])
                next_round()

    pg.display.update()
