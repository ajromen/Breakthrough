import random
from game.board import Board


class Ai:
    def __init__(self, difficulty, color):
        self.difficulty = difficulty
        self.color = color
    
    def make_move(self, board: Board):
        moves = board.get_all_legal_moves(self.color)
        if not moves:
            return False, None
        random_move = random.choice(list(moves.keys()))
        row, col = random_move[0], random_move[1]
        start_row, start_col = moves[random_move]
        succ, win = board.quick_make_move(start_row,start_col, row, col, self.color)
        if win:
            return True, self.color
        return succ, None