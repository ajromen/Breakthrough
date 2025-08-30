import json
from enums.piece_color import *
from game.board.simulated_board import SimulatedBoard


class Eval:
    def __init__(self):        
        self.weights = {        
            "material": 15,
            "mobility": 2,
            "advancment": 30,
            "piece_safety": 10,
            "att/def": 15,#razlika izmedju broja napadaca i odbranitelja,
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
                            
                        if col!=board_size-1:
                            defenders += int(board_state[row+1][col+1]==PIECE_WHITE)
                            
                        score += defenders * w['piece_safety']
                        
                        if defenders == 0:
                            score -= w['piece_safety']
                            

                    #ATTACKS 
                    if col!=0:
                        att+=int(board_state[row-1][col-1]==PIECE_BLACK)
                        blacks_defenders = 0
                        if row>1 and att==1:
                            if col>1:
                                blacks_defenders += int(board_state[row-2][col-2]==PIECE_BLACK)
                                
                            blacks_defenders += int(board_state[row-2][col]==PIECE_BLACK)
                        score+=(defenders-blacks_defenders)*w['att/def']
                        
                    
                    if col!=board_size-1:
                        att=0
                        att+=int(board_state[row-1][col+1]==PIECE_BLACK)
                        blacks_defenders=0
                        if row>1 and att==1:
                            if col<board_size-2:
                                blacks_defenders+=int(board_state[row-2][col+2]==PIECE_BLACK)
                            blacks_defenders+=int(board_state[row-2][col]==PIECE_BLACK)
                        score+=(defenders-blacks_defenders)*w['att/def']
                    
                    
                        
                elif piece == PIECE_BLACK:
                    score -= w['material']
                    
                    #ADVANCMENT                    
                    score-=row*w["advancment"]
                            
                    #PIECE SAFETY
                    if row!=0:
                        if col!=0:
                            defenders+=int(board_state[row-1][col-1]==PIECE_BLACK)
                            
                        if col!=board_size-1:
                            defenders += int(board_state[row-1][col+1]==PIECE_BLACK)
                            
                        score -= defenders * w['piece_safety']
                        
                        if defenders == 0:
                            score += w['piece_safety']             
                    
                    
                    #ATTACKS 
                    if col!=0:
                        att+=int(board_state[row+1][col-1]==PIECE_WHITE)
                        white_defenders = 0
                        if row<board_size-2 and att==1:
                            if col>1:
                                white_defenders += int(board_state[row+2][col-2]==PIECE_WHITE)
                                
                            white_defenders += int(board_state[row+2][col]==PIECE_WHITE)
                        score-=(defenders-white_defenders)*w['att/def']
                        
                    
                    if col!=board_size-1:
                        att=0
                        att+=int(board_state[row+1][col+1]==PIECE_WHITE)
                        white_defenders=0
                        if row<board_size-2 and att==1:
                            if col<board_size-2:
                                white_defenders+=int(board_state[row+2][col+2]==PIECE_WHITE)
                            white_defenders+=int(board_state[row+2][col]==PIECE_WHITE)
                        score-=(defenders-white_defenders)*w['att/def']          
                        
                    
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
