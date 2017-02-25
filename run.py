from configurations import *
from color import *
import pygame
import sys

all_sprites = pygame.sprite.Group()
# this function handle game initlization stuff
def initGame():
    x = pygame.init()
    print x
    screen = pygame.display.set_mode((window_width,window_hight))
    pygame.display.set_caption("pool game")

    # it handles game speed
    clock = pygame.time.Clock()

    # Game loop
    count = 0 #delete
    x,y = 0,0
    game_running_flag = True
    while game_running_flag:
        # keep loop running at right speed
        clock.tick(fps)
        # process input (events)

        for event in pygame.event.get():
            # check for closing window (event)
            if event.type == pygame.QUIT:
                game_running_flag = False
        # Update
        pygame.draw.rect(screen,randomColors[count],[x,y,200,200])
        all_sprites.update(screen)
        count += 1
        x += 5
        y += 5
        if x > 1300:
            x = 0
            y = 0
        if count > len(randomColors):
            count = 0

        # Draw / Render

        # after drowing everything flip the display
        pygame.display.flip()

    # closing window
    pygame.display.quit()
    pygame.quit()
    sys.exit()

initGame()
