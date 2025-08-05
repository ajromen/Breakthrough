import pygame


class ImageMenager:
    @staticmethod
    def load_all(self):
        self.tabla = pygame.image.load("assets/tabla.png")
        self.piece_white = pygame.image.load("assets/piece_white.png")
        self.piece_black = pygame.image.load("assets/piece_black.png")
        self.piece_white_xl = pygame.image.load("assets/piece_white_xl.png")
        self.piece_black_xl = pygame.image.load("assets/piece_black_xl.png")
