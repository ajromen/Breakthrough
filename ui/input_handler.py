import pygame


class InputHandler:
    @staticmethod
    def get_square(is_flipped=False):
        mouse_pos = pygame.mouse.get_pos()
        col = (mouse_pos[0]-26)//94
        row = (mouse_pos[1]-26)//94
        if is_flipped:
            row = 7 - row
            col = 7 - col
        return row, col
    
    @staticmethod
    def check_mouse_hover(rect):
        mouse_pos = pygame.mouse.get_pos()
        return rect.collidepoint(mouse_pos)
    