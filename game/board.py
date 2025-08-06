import pygame

from ui.image_menager import ImageMenager
from ui import colors

class Board:
    def __init__(self,window : pygame.Surface, board_size=8):
        self.window = window
        self.board_size = board_size
        self.board = [[2 if row < 2 else 1 if row > 5 else 0 for row in range(8)] for col in range(8)]
        
    def display(self,player_color):
        self.window.fill(colors.background)
        self.window.blit(ImageMenager.tabla, (25, 25)) # type: ignore
        if player_color == 'white':
            for i in range(0,self.board_size):
                for j in range(0,self.board_size):
                    if(self.board[i][j]==1):
                        self.window.blit(ImageMenager.piece_white, (27+i*(80+14),31+j*(80+14))) # type: ignore
                    elif(self.board[i][j]==2):
                        self.window.blit(ImageMenager.piece_black, (27+i*(80+14),31+j*(80+14))) # type: ignore
        else:
            for i in range(self.board_size-1,-1,-1):
                for j in range(self.board_size-1,-1,-1):
                    if(self.board[i][j]==1):
                        self.window.blit(ImageMenager.piece_black, (27+i*(80+14),31+j*(80+14))) # type: ignore
                    elif(self.board[i][j]==2):
                        self.window.blit(ImageMenager.piece_white, (27+i*(80+14),31+j*(80+14))) # type: ignore
                    
    def get_all_legal_moves(self, color):
        pass
    
    def make_move(self, start_pos, end_pos):
        pass
    
    def get_legal_moves(self, row, col):
        pass