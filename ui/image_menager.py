import pygame

class ImageMenager:
    tabla = None
    piece_white = None
    piece_black = None
    piece_white_xl = None
    piece_black_xl = None
    next = None
    pvp = None
    pvc = None
    start = None
    settings = None
    settings_no_shadow = None

    @staticmethod
    def load_all():
        ImageMenager.tabla = pygame.image.load("assets/tabla.png")
        ImageMenager.piece_white = pygame.image.load("assets/piece_white.png")
        ImageMenager.piece_black = pygame.image.load("assets/piece_black.png")
        ImageMenager.piece_white_xl = pygame.image.load("assets/piece_white_xl.png")
        ImageMenager.piece_black_xl = pygame.image.load("assets/piece_black_xl.png")
        ImageMenager.next = pygame.image.load("assets/next.png")
        ImageMenager.pvp = pygame.image.load("assets/pvp.png")
        ImageMenager.pvc = pygame.image.load("assets/pvc.png")
        ImageMenager.start = pygame.image.load("assets/start.png")
        ImageMenager.settings = pygame.image.load("assets/pause.png")
        ImageMenager.settings_no_shadow = pygame.image.load("assets/pause_no_shadow.png")
