from enums.piece_color import *


class BaseBoard:
    def __init__(self, size=8):
        self.size = size
        self.undo_stack = []
        self.state = []
        
    def make_move_from_move(self, move):
        start_row = move[0]
        start_col = move[1]
        row=move[2]
        col = move[3]
        color = move[4]
        return self.quick_make_move(start_row,start_col,row,col,color)
    
    
    def quick_make_move(self,start_row, start_col, row, col, player):
        '''Vraca igraca koji je pobedio/None'''
        captured_piece = self.state[row][col]
        self.state[row][col] = PIECE_WHITE if player == 'white' else PIECE_BLACK
        self.state[start_row][start_col] = PIECE_EMPTY  # type: ignore
        win = None
        self.undo_stack.append((start_row, start_col, row, col, player, captured_piece))  # type: ignore
        if (player == 'white' and row == 0) or (player == 'black' and row == self.size - 1):
            win = player 
        return win
    
    def eval(self):
        score = 0
        white_moves = self.get_all_legal_moves('white')
        black_moves = self.get_all_legal_moves('black')

        for row in range(self.size):
            for col in range(self.size):
                if self.state[row][col] == PIECE_WHITE:
                    score += 1
                elif self.state[row][col] == PIECE_BLACK:
                    score -= 1
            
            
        score += len(white_moves) - len(black_moves)
        
        return score
    
    def undo_move(self):
        """Vraca True ako je uspeo da undo"""
        if len(self.undo_stack)==0:
            return False
        
        start_row, start_col, row, col, color, captured_piece = self.undo_stack.pop() # type: ignore
        self.state[row][col] = captured_piece
        self.state[start_row][start_col] = PIECE_WHITE if color=="white" else PIECE_BLACK
        
        return True