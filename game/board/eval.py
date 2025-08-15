import json
from enums.piece_color import *
from game.board.simulated_board import SimulatedBoard


class Eval:
    def __init__(self):
        self.weights = {        
            "material": 10,
            "mobility": 2,
            "advancment": 15,
            "piece_safety": 10,
            "att/def": 10,#razlika izmedju napadaca i odbranitelja
            "passed_piece": 15,
            "wining_path": 100,
        }
        #self.load_weights("./weights.json")
        self.positions={}
        
    def __del__(self):
        self.save_weights("./weights.json")
    
    def board_to_key(self,state:list[list[int]],is_white=True):
        return (tuple(tuple(row) for row in state),is_white)
    

    def eval(self, board: SimulatedBoard,is_white):
        """+ beli - crni"""
        key = self.board_to_key(board.state, is_white)
        if key in self.positions:
            return self.positions[key]
        
        w = self.weights
        score = 0
        board_state = board.state
        board_size =  board.size

        white_moves = board.get_all_moves_sorted('white')
        black_moves = board.get_all_moves_sorted('black')
        
        for row in range(board.size):
            for col in range(board.size):
                
                piece= board_state[row][col]
                if piece == PIECE_EMPTY:
                    continue
                
                defenders = 0
                att=0
                
                if piece == PIECE_WHITE:
                    score += w['material']
                    
                    #ADVANCMENT
                    score += (board_size-row-1)*w["advancment"]
                    
                    
                    #PIECE SAFETY
                    if row!=board_size-1:
                        if col!=0:
                            defenders+=int(board_state[row+1][col-1]==PIECE_WHITE)
                            score+=(1 if defenders else -1)*w['piece_safety']
                            
                            
                        if col!=board_size-1:
                            safe_right = int(board_state[row+1][col+1]==PIECE_WHITE)
                            defenders += safe_right
                            score+=(1 if safe_right else -1)*w['piece_safety']
                        
                    #ATTACKS PROSIRI NA JOS JEDAN NIVO
                    if col!=0:
                        att+=int(board_state[row-1][col-1]==PIECE_BLACK)
                    
                    if col!=board_size-1:
                        att+=int(board_state[row-1][col+1]==PIECE_BLACK)
                    
                    score+=(defenders-att)*w["att/def"]
                    
                        
                elif piece == PIECE_BLACK:
                    score -= w['material']
                    
                    #ADVANCMENT                    
                    score-=row*w["advancment"]
                    
                    #PIECE SAFETY
                    if row!=0:
                        if col!=0:
                            defenders+=int(board_state[row-1][col-1]==PIECE_BLACK)
                            score-=(1 if defenders else -1)*w['piece_safety']
                            
                            
                        if col!=board_size-1:
                            safe_right = int(board_state[row-1][col+1]==PIECE_BLACK)
                            defenders += safe_right
                            score-=(1 if safe_right else -1)*w['piece_safety']
                            
                    #ATTACKS 
                    if col!=0:
                        att+=int(board_state[row+1][col-1]==PIECE_WHITE)
                    
                    if col!=board_size-1:
                        att+=int(board_state[row+1][col+1]==PIECE_WHITE)
                        
                    score-=(defenders-att)*w["att/def"]
                            
                        
                    
        #MOBILITY  
        score += (len(white_moves) - len(black_moves)) * w['mobility']
        self.positions[key]=score
        
        return score

        

    def save_weights(self, path):        
        with open(path, "w") as f:
            json.dump(self.weights, f)

    def load_weights(self, path):
        with open(path, "r") as f:
            self.weights = json.load(f)
