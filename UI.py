import pygame
from constante import *

def DrawDisplay(screen):
    p1 = (BORDA,BORDA)
    p2 = (WIDTH - BORDA,BORDA)
    p3 = (BORDA,TAMYDISP + BORDA)
    p4 = (WIDTH - BORDA,TAMYDISP + BORDA)
    pygame.draw.line(screen, COR_BORDA, p1, p2, TAM_BORDA)
    pygame.draw.line(screen, COR_BORDA, p1, p3, TAM_BORDA)
    pygame.draw.line(screen, COR_BORDA, p3, p4, TAM_BORDA)
    pygame.draw.line(screen, COR_BORDA, p4, p2, TAM_BORDA)

def UpdateUI(screen):
    DrawDisplay(screen)
    pygame.display.update()
    screen.fill(COR_BACKGROUND)
    
