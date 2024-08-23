import pygame
from constante import *


def DrawGrafico(screen,y,off):
    w = (WIDTH-BORDA*2)
    h = TAMYDISP+BORDA
    dist = w/(NUM-2)
    for i in range(NUM-2):
        i1= off-i-1
        if i1<0:
            i1 += (NUM)
        i2= i1-1
        if i2<0:
            i2=NUM-1
        pos1 = (w-(i*dist)+BORDA,h-y[i1])
        pos2 = (w-(i+1)*dist+BORDA,h-y[i2])
        pygame.draw.line(screen, COR_LINE, pos1, pos2, TAM_LINE)


