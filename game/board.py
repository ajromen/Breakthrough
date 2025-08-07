import pygame

from ui.image_menager import ImageMenager
from ui import colors

class Board:
    def __init__(self,window : pygame.Surface, board_size=8, flipped = False):
        self.window = window
        self.board_size = board_size
        self.board = [[2 if row < 2 else 1 if row > 5 else 0 for row in range(8)] for col in range(8)]
        self.flipped = flipped
        self.last_selected = None
        self.last_moves = None
        self.positions = [[(27+i*(80+14), 31+j*(80+14)) for j in range(8)] for i in range(8)]

        
    def display(self,player_color):
        self.window.fill(colors.background)
        self.window.blit(ImageMenager.tabla, (25, 25)) # type: ignore
        if not self.flipped:
            for i in range(0,self.board_size):
                for j in range(0,self.board_size):
                    if(self.board[i][j]==1):
                        self.window.blit(ImageMenager.piece_white, self.positions[i][j]) # type: ignore
                    elif(self.board[i][j]==2):
                        self.window.blit(ImageMenager.piece_black, self.positions[i][j]) # type: ignore
        else:
            for i in range(self.board_size-1,-1,-1):
                for j in range(self.board_size-1,-1,-1):
                    if(self.board[i][j]==1):
                        self.window.blit(ImageMenager.piece_black, self.positions[i][j]) # type: ignore
                    elif(self.board[i][j]==2):
                        self.window.blit(ImageMenager.piece_white, self.positions[i][j]) # type: ignore
                    
    def get_all_legal_moves(self, color):
        pass
    
    def make_move(self, start_pos, end_pos):
        pass
    
    def get_legal_moves(self, row, col, player):        
        pos = self.board[row][col]
        if  pos == 0:
            return
        if pos == 1 and player == "white":
            return []
        if pos == 2 and player == 'black':
            return []
        return
        
    def check_legal_moves(self, row, col, player):            
        moves = self.get_legal_moves(row, col, player)
        
        if moves == None:
            self.last_selected=None
            return False
        
        self.last_selected = (row, col)
        self.last_moves = moves
        
        return True
            
            
    def display_given_moves(self,row,col,moves):
        pygame.draw.rect(self.window, colors.selected, (26 + row * 94, 26 + col * 94, 94, 94), width=2, border_radius=5)
        for move in moves:
            pass
        
    def display_last_move(self):
        if(self.last_selected is None):
            return
        
        self.display_given_moves(self.last_selected[0],self.last_selected[1],self.last_moves)
        

        