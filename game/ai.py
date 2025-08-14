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
        
    
    def make_move_radnom(self, board: Board):
        print(self.evaluator.eval(self.board))  # type: ignore
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
        self.board.state = board.state.copy()
    
    
    def make_move(self,board: Board):
        self.copy_move(board)
        self.alfa=float("-inf")
        self.beta=float("inf")
        move = self.minimax(self.difficulty, self.color=='white')
        win = self.board.make_move(move)
        return win
        
    def minimax(self, depth, maximizing):
        if depth==0:
            return self.evaluator.eval(self.board)
        
        if maximizing:
            max_eval = float('-inf')
            for move in self.board.get_legal_moves('white'): 
                self.board.make_move(move)
                eval = self.minimax(depth-1, False)
                self.board.undo_move()
                max_eval = max(eval,max_eval) 
                self.alfa = max(self.alfa,eval)
                if self.beta<self.alfa:
                    break
            return max_eval
        else:
            min_eval =float('inf')
            for move in self.board.get_legal_moves('black'): 
                self.board.make_move(move)
                eval = self.minimax(depth-1, True)
                self.board.undo_move()
                min_eval = max(eval,min_eval) 
                self.beta = min(self.beta,eval)
                if self.beta<=self.alfa:
                    break
            return min_eval
        
            
        