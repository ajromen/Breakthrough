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
    
    def make_move(self, row, col, player):
        selected_row = self.last_selected[0] # type: ignore
        selected_col = self.last_selected[1] # type: ignore
        
        to_check = (row,col)
        
        self.last_selected=None
        
        if self.last_moves.get(to_check, False): # type: ignore
            self.board[row][col] = 1 if player == 'white' else 2
            self.board[selected_row][selected_col] = 0  # type: ignore
            return True
        
        return False
        
        
    
    def get_legal_moves(self, row, col, player):        
        pos = self.board[row][col]
        moves = {}
        if  pos == 0:
            return
        if pos == 1 and player == "white":
            if row!=0 and self.board[row-1][col-1]!=1:# left
                moves[(row-1,col-1)]=True
                
            if self.board[row][col-1]==0: # center
                moves[(row,col-1)]=True
                
            if row!=7 and self.board[row+1][col-1]!=1:
                moves[(row+1,col-1)]=True
            
            return moves
        if pos == 2 and player == 'black':
            if row!=0 and self.board[row-1][col+1]!=2:# left
                moves[(row-1,col+1)]=True
                
            if self.board[row][col+1]==0: # center
                moves[(row,col+1)]=True
                
            if row!=7 and self.board[row+1][col+1]!=2:
                moves[(row+1,col+1)]=True
            
            return moves
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
        for move in moves:
            pygame.draw.rect(self.window, colors.highlight, (25 + move[0] * 94, 25 + move[1] * 94, 96, 96), width=2, border_radius=0)
        
        pygame.draw.rect(self.window, colors.selected, (25 + row * 94, 25 + col * 94, 96, 96), width=2, border_radius=0)
        
    def display_last_move(self):
        if(self.last_selected is None):
            return
        
        self.display_given_moves(self.last_selected[0],self.last_selected[1],self.last_moves)
        

        