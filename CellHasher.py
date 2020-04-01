import time
import sys
import pygame
from pygame.locals import *
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SKYBLUE = (0, 191, 255)

cellsize = 50

def draw_map(bincode, size, e):
    poslist = []
    for i in range(0, size*cellsize, cellsize):
        for j in range(0, size*cellsize, cellsize):
            poslist.append((j, i))
    
    surface = pygame.display.set_mode((size*cellsize, size*cellsize))
    pygame.display.set_caption('Life Game Simulator')

    surface.fill(BLACK)

    

    for i in range(len(bincode)):
        if bincode[i]==1:
            pygame.draw.rect(surface, BLUE, (poslist[i][0], poslist[i][1], cellsize, cellsize))

    for i in range(cellsize, size*cellsize, cellsize):
        pygame.draw.line(surface, SKYBLUE, (i, 0), (i, size*cellsize))
        pygame.draw.line(surface, SKYBLUE, (0, i), (size*cellsize, i))

    if e==True:
        myfont = pygame.font.SysFont('Comic Sans MS', 17)
        textsurface = myfont.render('Encoded Integer', False, WHITE)
        surface.blit(textsurface,(0,0))
    else:
        myfont = pygame.font.SysFont('Comic Sans MS', 17)
        textsurface = myfont.render('Integer', False, WHITE)
        surface.blit(textsurface,(0,0))
        

    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                if e==True:
                    pygame.quit()
                    return
                return
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if e==True:
                        pygame.quit()
                        return
                    return

def iter(n):
    code = bin(n)
    seed = 1
    tresult = hex(int(encode(code, seed), 2))
    result = tresult[2:].upper()
    print('Encoded Integer: {0}'.format(result))
    return


def main():
    try:
        tcode = int(input('Input integer: '))
        seed = 1
    except:
        print('error')
        return
    else:
        code = bin(tcode)

    tresult = hex(int(encode(code, seed), 2))
    result = tresult[2:].upper()
    print('Encoded Integer: {0}'.format(result))
    input()
    return



def encode(code, seed):
    code = code[2:]
    res = []
    for i in code:
        res.append(int(i))

    for i in range(1, 1000001):
        if len(code) <= (i**2):
            mnum = i
            term = (i**2) - len(code)
            break

    for j in range(term):
        res.append(0)
    
    result = process(res, mnum, seed)
    
    return result

def process(bincode, size, seed):
    for r in range(seed):
        draw_map(bincode, size, False)
        for a in range(size**2):
            try:
                snum = bincode[a-size-1] + bincode[a-size] + bincode[a-size+1] + bincode[a-1] + bincode[a+1] + bincode[a+size-1] + bincode[a+size] + bincode[a+size+1]
            except:
                pass
            else:
                if snum==3:
                    bincode[a] = 1
                elif snum==2:
                    bincode[a] = bincode[a]
                else:
                    bincode[a] = 0
        draw_map(bincode, size, True)
        
    res = ''
    for s in bincode:
        res += str(s)
    return res
    

if __name__ == '__main__':
    main()

