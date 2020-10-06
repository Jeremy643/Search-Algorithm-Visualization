import pygame
from .constants import *
from .button import Button

class Control:
    def __init__(self, win):
        self.win = win
        self.selected_btn = None
        self.start_btn = Button(START_POS_X, START_POS_Y, BTN_WIDTH, BTN_HEIGHT, TYPE_START)
        self.end_btn = Button(END_POS_X, END_POS_Y, BTN_WIDTH, BTN_HEIGHT, TYPE_END)
        self.wall_btn = Button(WALL_POS_X, WALL_POS_Y, BTN_WIDTH, BTN_HEIGHT, TYPE_WALL)
        self.remove_btn = Button(REMOVE_POS_X, REMOVE_POS_Y, BTN_WIDTH, BTN_HEIGHT, TYPE_REMOVE)
        self.go_btn = Button(GO_POS_X, GO_POS_Y, BTN_WIDTH, BTN_HEIGHT, TYPE_GO)
        self.reset_btn = Button(RESET_POS_X, RESET_POS_Y, BTN_WIDTH, BTN_HEIGHT, TYPE_RESET)
        self.buttons = {TYPE_START: self.start_btn, TYPE_END: self.end_btn, TYPE_WALL: self.wall_btn, TYPE_REMOVE: self.remove_btn, TYPE_GO: self.go_btn, TYPE_RESET: self.reset_btn}
    
    def _reset_buttons(self):
        for btn in self.buttons.values():
            btn.reset()
    
    def draw(self):
        pygame.draw.rect(self.win, GREY, (GRID_WIDTH, 0, CONTROL_WIDTH, CONTROL_HEIGHT))
        pygame.draw.rect(self.win, BLACK, (GRID_WIDTH, 0, CONTROL_WIDTH, CONTROL_HEIGHT), 2)
        for btn_type in self.buttons:
            self.buttons[btn_type].draw(self.win)

    def select_btn(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        for btn in self.buttons.values():
            if btn.x <= mouse_x <= btn.x + btn.width and btn.y <= mouse_y <= btn.y + btn.height and btn.btn_on:
                self.selected_btn = btn
                btn.select()
                for btn in self.buttons.values():
                    btn.turn_off()
                break
    
    def cancel_btn(self, mouse_pos):
        mouse_x, mouse_y = mouse_pos
        if self.selected_btn.x <= mouse_x <= self.selected_btn.x + self.selected_btn.width and self.selected_btn.y <= mouse_y <= self.selected_btn.y + self.selected_btn.height:
            return True
        else:
            return False
    
    def turn_off_btns(self, except_btn=None):
        for btn in self.buttons.values():
            if btn == except_btn:
                continue
            else:
                btn.turn_off()
    
    def get_selected_btn_info(self):
        return self.selected_btn.x, self.selected_btn.y, self.selected_btn.width, self.selected_btn.height

    def reset(self):
        self.selected_btn = None
        self._reset_buttons()
    
    def update(self):
        self.draw()
        pygame.display.update()