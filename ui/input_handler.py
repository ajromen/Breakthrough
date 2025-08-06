import pygame


class InputHandler:
    @staticmethod
    def get_square(self):
        return
    
    @staticmethod
    def check_mouse_hover(self, rect):
        mouse_pos = pygame.mouse.get_pos()
        return rect.collidepoint(mouse_pos)
    