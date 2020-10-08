import pygame
from .grid import Grid
from .control import Control
from .constants import *

class Window:
    def __init__(self, win, algorithm_type):
        self.win = win
        self.algorithm_type = algorithm_type
        self.grid = Grid(self.win)
        self.control = Control(self.win)
    
    def select(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos

        if self.control.selected_btn:
            selected_x, selected_y, selected_width, selected_height = self.control.get_selected_btn_info()

            if self.control.selected_btn == self.control.start_btn:
                if self.control.cancel_btn(mouse_pos):
                    self.control.reset()
                elif 0 <= mouse_x <= GRID_WIDTH and 0 <= mouse_y <= GRID_HEIGHT:
                    succ = self.grid.select_start(mouse_pos)

                    if succ:
                        self.control.reset()
            elif self.control.selected_btn == self.control.end_btn:
                if self.control.cancel_btn(mouse_pos):
                    self.control.reset()
                elif 0 <= mouse_x <= GRID_WIDTH and 0 <= mouse_y <= GRID_HEIGHT:
                    succ = self.grid.select_end(mouse_pos)

                    if succ:
                        self.control.reset()
            elif self.control.selected_btn == self.control.wall_btn:
                if self.control.cancel_btn(mouse_pos):
                    self.control.reset()
                elif 0 <= mouse_x <= GRID_WIDTH and 0 <= mouse_y <= GRID_HEIGHT:
                    self.grid.select_wall(mouse_pos)
            elif self.control.selected_btn == self.control.remove_btn:
                if self.control.cancel_btn(mouse_pos):
                    self.control.reset()
                elif 0 <= mouse_x <= GRID_WIDTH and 0 <= mouse_y <= GRID_HEIGHT:
                    self.grid.remove(mouse_pos)
        else:
            self.control.select_btn(mouse_pos)

            if self.control.selected_btn is None:
                return False
            elif self.control.selected_btn == self.control.go_btn and self.grid.ready():
                if self.algorithm_type == 'bfs':
                    self.grid.run_bfs()
                elif self.algorithm_type == 'dfs':
                    self.grid.run_dfs(self.grid.start_point)
                elif self.algorithm_type == 'dij':
                    self.grid.run_dijkstra()
                
                self.control.reset()
                self.control.turn_off_btns(self.control.reset_btn)
            elif self.control.selected_btn == self.control.go_btn and not self.grid.ready():
                self.control.reset()
            elif self.control.selected_btn == self.control.reset_btn:
                self.grid.reset()
                self.control.reset()

    def select_multiple(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos

        if self.control.selected_btn == self.control.wall_btn and 0 <= mouse_x <= GRID_WIDTH and 0 <= mouse_y <= GRID_HEIGHT:
            self.grid.select_wall(mouse_pos)
            self.grid.update()
            return True
        else:
            return False
    
    def update(self):
        self.grid.update()
        self.control.update()