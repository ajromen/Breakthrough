import random
from game.board.board import Board
from game.board.simulated_board import SimulatedBoard
from game.board.eval import Eval


class Ai:
    def __init__(self, difficulty, color, board: Board):
        self.difficulty = difficulty
        self.color = color
        self.board = SimulatedBoard(board)
        self.evaluator = Eval()  # type: ignore
    
    def make_move(self, board: Board):
        moves = board.get_all_legal_moves(self.color)
        
        if not moves:
            return None
        
        random_move = random.choice(list(moves.keys()))
        row, col = random_move[0], random_move[1]
        start_row, start_col = moves[random_move]
        win = board.quick_make_move(start_row,start_col, row, col, self.color)
        self.board.state = board.state.copy()
        print(self.evaluator.eval(self.board))  # type: ignore
        
        return win
    
    def make_move2(self,board: Board):
        move = self.minimax(3,True)
    
    def copy_move(self, board):
        self.board.state = board.state.copy()
        
    def minimax(self, depth, maximizing):
        if depth==0:
            return self.evaluator.eval(self.board)
        