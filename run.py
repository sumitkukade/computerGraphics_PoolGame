from configurations import *
from color import *
import pygame
import sys

all_sprites = pygame.sprite.Group()
# this function handle game initlization stuff
def initGame():
    count = 0 # delete
    pygame.init()
    screen = pygame.display.set_mode((window_width,window_hight))
    pygame.display.set_caption("pool game")

    # it handles game speed
    clock = pygame.time.Clock()

    # Game loop
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
        all_sprites.update()
        # Draw / Render
        all_sprites.update(screen)
        screen.fill(randomColors[count])
        count+=1
        if count >= len(randomColors):
            count = 0
        # after drowing everything flip the display
        pygame.display.flip()

    # closing window
    pygame.display.quit()
    pygame.quit()
    sys.exit()

initGame()
