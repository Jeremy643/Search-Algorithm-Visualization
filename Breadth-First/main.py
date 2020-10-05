import pygame
import os
from Window.constants import *
from Window.window import Window

FPS = 60

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (100, 100)
WIN = pygame.display.set_mode((GRID_WIDTH + CONTROL_WIDTH, GRID_HEIGHT))
pygame.display.set_caption('Breadth First Search')


def main():
    run = True
    clock = pygame.time.Clock()
    window = Window(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                window.select(mouse_pos)
            elif pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                window.select_multiple(mouse_pos)
        
        window.update()
        
    pygame.quit()

main()