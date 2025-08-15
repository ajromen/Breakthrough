from enums.piece_color import *
from game.board.base_board import BaseBoard
from game.board.board import Board


class SimulatedBoard(BaseBoard):    
    def __init__(self, board: Board):
        super().__init__(board.size)
        self.state = board.state.copy()
    
    def get_all_moves_sorted(self,color):
        moves = []
        for row in range(self.size):
            for col in range(self.size):
                piece= self.state[row][col]
                if piece is PIECE_EMPTY:
                    continue
                if piece is PIECE_WHITE and color=='white':
                    moves.extend(self.get_moves(row,col))
                    
                if piece is PIECE_BLACK and color=='black':
                    moves.extend(self.get_moves(row,col))
                
        return moves
    
    def get_moves(self,row,col):
        pos = self.state[row][col]
        moves = []
        if  pos == PIECE_EMPTY:
            return None
        
        if pos == PIECE_WHITE:
            if col!=0 and self.state[row-1][col-1]!=PIECE_WHITE:
                moves.append((row,col,row-1,col-1,'white'))
            
            if self.state[row-1][col]==PIECE_EMPTY:
                moves.append((row,col,row-1,col,'white'))
                
            if col!=self.size-1 and self.state[row-1][col+1]!=PIECE_WHITE:
                moves.append((row,col,row-1,col+1,'white'))

            return moves
        
        if pos==PIECE_BLACK:
            if col!=0 and self.state[row+1][col-1]!=PIECE_BLACK:
                moves.append((row,col,row+1,col-1,'black'))
                
            if self.state[row+1][col]==PIECE_EMPTY:
                moves.append((row,col,row+1,col,'black'))
                
            if col!=self.size-1 and self.state[row+1][col+1]!=PIECE_BLACK:
                moves.append((row,col,row+1,col+1,'black'))
            
            return moves
                
        return None
    
        