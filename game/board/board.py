import pygame

from enums.piece_color import *
from game.board.base_board import BaseBoard
from ui.image_menager import ImageMenager
from ui import colors

class Board(BaseBoard):
    def __init__(self,window : pygame.Surface, size=8, flipped = False):
        super().__init__(size)
        self.window = window
        self.state = self.create_board_state(size)
        self.flipped = flipped
        self.last_selected = None
        self.last_moves = None
        
    def create_board_state(self, size):
        state = []
        for i in range(size):
            row = []
            for j in range(size):
                if i < 2:
                    row.append(PIECE_BLACK)
                elif i >= size - 2:
                    row.append(PIECE_WHITE)
                else:
                    row.append(PIECE_EMPTY)
            state.append(row)
            
        return state
        
    def display(self,player_color):
        self.window.fill(colors.background)
        self.window.blit(ImageMenager.tabla, (25, 25)) # type: ignore
        
        for i in range(self.size):
            for j in range(self.size):
                if self.flipped:
                    r, c = self.size - 1 - i, self.size -1 - j
                else:
                    r, c = i, j

                if self.state[r][c] == PIECE_WHITE:
                    self.window.blit(ImageMenager.piece_white, (27 + j * 94, 31 + i * 94)) # type: ignore
                elif self.state[r][c] == 2:
                    self.window.blit(ImageMenager.piece_black, (27 + j * 94, 31 + i * 94)) # type: ignore
    
    
    def make_move(self, row, col, player):
        '''Vraca True ako je potez uspesan i igraca koji je pobedio'''
        selected_row = self.last_selected[0] # type: ignore
        selected_col = self.last_selected[1] # type: ignore
        
        to_check = (row,col)
        
        self.last_selected=None
        
        if self.last_moves.get(to_check, False):  # type: ignore
            return True, self.quick_make_move(selected_row, selected_col, row, col, player)
        
        
        return False, None
        
        
    def check_legal_moves(self, row, col, player): 
        """Vraca True ako je selektovana figura"""         
        moves = self.get_legal_moves(row, col, player)
        
        if moves == None:
            self.last_selected=None
            return False
        
        self.last_selected = (row, col)
        self.last_moves = moves
        
        return True
            
            
    def display_coords(self, row, col):
        if self.flipped:
            return (self.size - 1 - row, self.size - 1 - col)
        return row, col

    def display_given_moves(self, row, col, moves):
        for r, c in moves:
            dr, dc = self.display_coords(r, c)
            pygame.draw.rect(self.window, colors.highlight, (25 + dc * 94, 25 + dr * 94, 96, 96), width=2)

        dr, dc = self.display_coords(row, col)
        pygame.draw.rect(self.window, colors.selected, (25 + dc * 94, 25 + dr * 94, 96, 96), width=2)

    def display_last_move(self):
        if(self.last_selected is None):
            return
        
        self.display_given_moves(self.last_selected[0],self.last_selected[1],self.last_moves)
        

    
    
    