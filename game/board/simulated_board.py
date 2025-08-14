from game.board.base_board import BaseBoard
from game.board.board import Board


class SimulatedBoard(BaseBoard):    
    def __init__(self, board: Board):
        super().__init__(board.size)
        self.state = board.state.copy()
        
    def make_move(self, move):
        start_row = move[0]
        start_col = move[1]
        row=move[2]
        col = move[3]
        color = move[4]
        return self.quick_make_move(start_row,start_col,row,col,color)
        