from game.board.base_board import BaseBoard


class SimulatedBoard(BaseBoard):
    def __init__(self, size=8):
        super().__init__(size)