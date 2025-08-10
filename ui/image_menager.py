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
    slider = None
    win_shadow = None
    white_wins = None
    black_wins = None

    @staticmethod
    def load_all():
        ImageMenager.tabla = pygame.image.load("assets/tabla.png").convert_alpha()
        ImageMenager.piece_white = pygame.image.load("assets/piece_white.png").convert_alpha()
        ImageMenager.piece_black = pygame.image.load("assets/piece_black.png").convert_alpha()
        ImageMenager.piece_white_xl = pygame.image.load("assets/piece_white_xl.png").convert_alpha()
        ImageMenager.piece_black_xl = pygame.image.load("assets/piece_black_xl.png").convert_alpha()
        ImageMenager.next = pygame.image.load("assets/next.png").convert_alpha()
        ImageMenager.pvp = pygame.image.load("assets/pvp.png").convert_alpha()
        ImageMenager.pvc = pygame.image.load("assets/pvc.png").convert_alpha()
        ImageMenager.start = pygame.image.load("assets/start.png").convert_alpha()
        ImageMenager.settings = pygame.image.load("assets/pause.png").convert_alpha()
        ImageMenager.settings_no_shadow = pygame.image.load("assets/pause_no_shadow.png").convert_alpha()
        ImageMenager.slider = pygame.image.load("assets/slider.png").convert_alpha()
        ImageMenager.win_shadow = pygame.image.load("assets/win_shadow.png").convert_alpha()
        ImageMenager.white_wins = pygame.image.load("assets/white_wins.png").convert_alpha()
        ImageMenager.black_wins = pygame.image.load("assets/black_wins.png").convert_alpha()
