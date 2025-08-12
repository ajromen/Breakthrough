from enums.piece_color import *


class BaseBoard:
    def __init__(self, size=8):
        self.size = size
        self.undo_stack = []
        self.board = []        
        
    def get_all_legal_moves(self, color):
        moves = {}
        piece_code = PIECE_WHITE if color == 'white' else PIECE_BLACK
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == piece_code:
                    legal_moves = self.get_legal_moves(i, j, color)
                    if legal_moves:
                        moves.update(legal_moves)
        return moves
    
    def get_legal_moves(self, row, col, player):        
        pos = self.board[row][col]
        start_pos = (row, col) 
        moves = {}
        if  pos == PIECE_EMPTY:
            return None
        
        if pos == PIECE_WHITE and player == 'white':
            if col!=0 and self.board[row-1][col-1]!=PIECE_WHITE:
                moves[(row-1,col-1)]=start_pos
            
            if self.board[row-1][col]==PIECE_EMPTY:
                moves[(row-1,col)]=start_pos
                
            if col!=7 and self.board[row-1][col+1]!=PIECE_WHITE:
                moves[(row-1,col+1)]=start_pos

            return moves
        
        if pos==PIECE_BLACK and player =="black":
            if col!=0 and self.board[row+1][col-1]!=PIECE_BLACK:
                moves[(row+1,col-1)]=start_pos
                
            if self.board[row+1][col]==PIECE_EMPTY:
                moves[(row+1,col)]=start_pos
                
            if col!=7 and self.board[row+1][col+1]!=PIECE_BLACK:
                moves[(row+1,col+1)]=start_pos
            
            return moves
                
        return None
    
    def quick_make_move(self,start_row, start_col, row, col, player):
        '''Vraca igraca koji je pobedio ako je igrac pobedio'''
        captured_piece = self.board[row][col]
        self.board[row][col] = PIECE_WHITE if player == 'white' else PIECE_BLACK
        self.board[start_row][start_col] = PIECE_EMPTY  # type: ignore
        win = None
        self.undo_stack.append((start_row, start_col, row, col, player, captured_piece))  # type: ignore
        if (player == 'white' and row == 0) or (player == 'black' and row == self.size - 1):
            win = player 
        return win