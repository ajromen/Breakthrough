import copy
import random
import sys
from game.board.board import Board
from game.board.simulated_board import SimulatedBoard
from game.board.eval import Eval


MAX_INT = sys.maxsize
MIN_INT = -sys.maxsize

class Ai:
    def __init__(self, difficulty, color, board: Board):
        self.difficulty = difficulty
        self.color = color
        self.board = SimulatedBoard(board)
        self.evaluator = Eval()  # type: ignore
        self.best_move=None
        
    
    def make_move_random(self, board: Board):
        print(self.evaluator.eval(self.board),self.color)
        moves = board.get_all_legal_moves(self.color)
        
        if not moves:
            return None
        
        random_move = random.choice(list(moves.keys()))
        row, col = random_move[0], random_move[1]
        start_row, start_col = moves[random_move]
        win = board.quick_make_move(start_row,start_col, row, col, self.color)
        self.copy_move(board)
        
        return win
    
    def copy_move(self, board):
        self.board.state = copy.deepcopy(board.state)
    
    
    def make_move(self, board: Board):
        self.copy_move(board)
        self.best_move = None
        self.minimax(self.difficulty, MIN_INT, MAX_INT, self.color == 'white')
        return board.make_move_from_move(self.best_move)

    def minimax(self, depth, alpha, beta, maximizing):
        if depth == 0:
            return self.evaluator.eval(self.board, maximizing)
        
        moves = self.board.get_all_moves_sorted('white' if maximizing else 'black')
        
        if not moves:
            return MAX_INT if maximizing else MIN_INT

        if maximizing:
            max_eval = MIN_INT
            for move in moves:
                win = self.board.make_move_from_move(move)
                if win:
                    if depth == self.difficulty:
                        self.best_move = move
                    self.board.undo_move()
                    return MAX_INT - (self.difficulty - depth)
                eval = self.minimax(depth - 1, alpha, beta, False)
                self.board.undo_move()

                if eval > max_eval:
                    max_eval = eval
                    if depth == self.difficulty: # and self.color == 'white':  # mozda 
                        self.best_move = move

                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
                
            return max_eval
        else:
            min_eval = MAX_INT
            for move in moves:
                win = self.board.make_move_from_move(move)
                if win:
                    if depth == self.difficulty:
                        self.best_move = move
                    self.board.undo_move()
                    return MIN_INT + (self.difficulty - depth)
                eval = self.minimax(depth - 1, alpha, beta, True)
                self.board.undo_move()

                if eval < min_eval:
                    min_eval = eval
                    if depth == self.difficulty:
                        self.best_move = move

                beta = min(beta, eval)
                if beta <= alpha:
                    break
                
            return min_eval
