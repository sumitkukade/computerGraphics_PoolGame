from configurations import *
import pygame

# this function handle some game initlization stuff
def initGame():
    pygame.init()
    screen = pygame.display.set_mode((window_width,window_hight))
    pygame.display.set_caption("pool game")
    
    ## it handles game speed
    clock = pygame.time.Clock()
    print screen

