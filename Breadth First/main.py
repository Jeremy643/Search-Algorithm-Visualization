import pygame
import os
from Window.constants import *
from Window.grid import Grid
from Window.control import Control

FPS = 60

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (100, 100)
WIN = pygame.display.set_mode((GRID_WIDTH + CONTROL_WIDTH, GRID_HEIGHT))
pygame.display.set_caption('Breadth First Search')


def main():
    run = True
    clock = pygame.time.Clock()
    grid = Grid(WIN)
    control = Control(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = mouse_pos

                if control.selected_btn:
                    selected_x, selected_y = control.selected_btn.x, control.selected_btn.y
                    selected_width, selected_height = control.selected_btn.width, control.selected_btn.height

                    if control.selected_btn.btn_type == TYPE_START:
                        if control.cancel_btn(mouse_pos):
                            control.reset()
                        elif 0 <= mouse_x <= GRID_WIDTH and 0 <= mouse_y <= GRID_HEIGHT:
                            succ = grid.select_start(mouse_pos)

                            if succ:
                                control.reset()
                    elif control.selected_btn.btn_type == TYPE_END:
                        if control.cancel_btn(mouse_pos):
                            control.reset()
                        elif 0 <= mouse_x <= GRID_WIDTH and 0 <= mouse_y <= GRID_HEIGHT:
                            succ = grid.select_end(mouse_pos)

                            if succ:
                                control.reset()
                    elif control.selected_btn.btn_type == TYPE_WALL:
                        if control.cancel_btn(mouse_pos):
                            control.reset()
                        elif 0 <= mouse_x <= GRID_WIDTH and 0 <= mouse_y <= GRID_HEIGHT:
                            grid.select_wall(mouse_pos)
                    elif control.selected_btn.btn_type == TYPE_REMOVE:
                        if control.cancel_btn(mouse_pos):
                            control.reset()
                        elif 0 <= mouse_x <= GRID_WIDTH and 0 <= mouse_y <= GRID_HEIGHT:
                            grid.remove(mouse_pos)
                else:
                    control.select_btn(mouse_pos)

                    if control.selected_btn is None:
                        break
                    elif control.selected_btn.btn_type == TYPE_GO and grid.ready():
                        grid.run()
                        control.reset()
                        control.turn_off_btns(control.reset_btn)
                    elif control.selected_btn.btn_type == TYPE_GO and not grid.ready():
                        control.reset()
                    elif control.selected_btn.btn_type == TYPE_RESET:
                        grid.reset()
                        control.reset()
            elif control.selected_btn == control.wall_btn and pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                mouse_x, mouse_y = mouse_pos

                if 0 <= mouse_x <= GRID_WIDTH and 0 <= mouse_y <= GRID_HEIGHT:
                    grid.select_wall(mouse_pos)
                    grid.update()
        
        grid.update()
        control.update()
        
    pygame.quit()

main()