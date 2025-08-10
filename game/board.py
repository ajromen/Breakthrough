import pygame

from ui.image_menager import ImageMenager
from ui import colors

class Board:
    def __init__(self,window : pygame.Surface, board_size=8, flipped = False):
        self.window = window
        self.board_size = board_size
        self.board = self.create_board(board_size)
        self.flipped = flipped
        self.last_selected = None
        self.last_moves = None

        
    def create_board(self, board_size):
        board = []
        for i in range(board_size):
            row = []
            for j in range(board_size):
                if i < 2:
                    row.append(2)
                elif i >= board_size - 2:
                    row.append(1)
                else:
                    row.append(0)
            board.append(row)
            
        return board
        
    def display(self,player_color):
        self.window.fill(colors.background)
        self.window.blit(ImageMenager.tabla, (25, 25)) # type: ignore
        
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.flipped:
                    r, c = self.board_size - 1 - i, self.board_size -1 - j
                else:
                    r, c = i, j

                if self.board[r][c] == 1:
                    self.window.blit(ImageMenager.piece_white, (27 + j * 94, 31 + i * 94)) # type: ignore
                elif self.board[r][c] == 2:
                    self.window.blit(ImageMenager.piece_black, (27 + j * 94, 31 + i * 94)) # type: ignore
                    
    def get_all_legal_moves(self, color):
        pass
    
    def make_move(self, row, col, player):
        selected_row = self.last_selected[0] # type: ignore
        selected_col = self.last_selected[1] # type: ignore
        
        to_check = (row,col)
        
        self.last_selected=None
        win = False
        
        if self.last_moves.get(to_check, False): # type: ignore
            self.board[row][col] = 1 if player == 'white' else 2
            self.board[selected_row][selected_col] = 0  # type: ignore
            if row == 0 if player=='white' else 1:
                win = True 
            return True, win
        
        return False, False
        
        
    
    def get_legal_moves(self, row, col, player):        
        pos = self.board[row][col]
        moves = {}
        if  pos == 0:
            return None
        
        if pos == 1 and player == 'white':
            if col!=0 and self.board[row-1][col-1]!=1:
                moves[(row-1,col-1)]=True
            
            if self.board[row-1][col]==0:
                moves[(row-1,col)]=True
                
            if col!=7 and self.board[row-1][col+1]!=1:
                moves[(row-1,col+1)]=True

            return moves
        
        if pos==2 and player =="black":
            print(row,col,player,pos)
            if col!=0 and self.board[row+1][col-1]!=2:
                moves[(row+1,col-1)]=True
                
            if self.board[row+1][col]==0:
                moves[(row+1,col)]=True
                
            if col!=7 and self.board[row+1][col+1]!=2:
                moves[(row+1,col+1)]=True
            
            return moves
                
        return None
    
        
    def check_legal_moves(self, row, col, player):            
        moves = self.get_legal_moves(row, col, player)
        
        if moves == None:
            self.last_selected=None
            return False
        
        self.last_selected = (row, col)
        self.last_moves = moves
        
        return True
            
            
    def display_coords(self, row, col):
        if self.flipped:
            return (self.board_size - 1 - row, self.board_size - 1 - col)
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
        

        