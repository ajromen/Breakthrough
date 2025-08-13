from game.board.base_board import BaseBoard
from game.board.board import Board


class SimulatedBoard(BaseBoard):    
    def __init__(self, board: Board):
        super().__init__(board.size)
        self.state = board.state.copy()