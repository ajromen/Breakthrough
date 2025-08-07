import pygame


class InputHandler:
    @staticmethod
    def get_square():
        mouse_pos = pygame.mouse.get_pos()
        row = (mouse_pos[0]-26)//94
        col = (mouse_pos[1]-26)//94
        return row, col
    
    @staticmethod
    def check_mouse_hover(rect):
        mouse_pos = pygame.mouse.get_pos()
        return rect.collidepoint(mouse_pos)
    