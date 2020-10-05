import pygame
from .constants import *


class Button:
    def __init__(self, x, y, width, height, btn_type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.btn_type = btn_type
        self.btn_on = True
        self.selected = False
    
    def draw(self, win):
        if self.btn_on:
            btn_colour = LIGHT_GREY
        else:
            btn_colour = DARK_GREY
        pygame.draw.rect(win, btn_colour, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, BLACK, (self.x, self.y, self.width, self.height), 2)
        
        pygame.font.init()

        small_text = pygame.font.Font('freesansbold.ttf', 20)
        if self.btn_on:
            txt_colour = BLACK
        else:
            txt_colour = WHITE
        if self.selected:
            txt = 'Cancel'
        else:
            txt = self.btn_type
        text_surf = small_text.render(txt, False, txt_colour)

        x_offset = (self.width - text_surf.get_width()) // 2
        y_offset = (self.height - text_surf.get_height()) // 2
        win.blit(text_surf, (self.x + x_offset, self.y + y_offset))
    
    def select(self):
        self.selected = True
    
    def turn_off(self):
        if not self.selected:
            self.btn_on = False

    def reset(self):
        self.btn_on = True
        self.selected = False