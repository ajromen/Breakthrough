import pygame
from game.board.board import Board
from ui.input_handler import InputHandler
from game.ai import Ai

class Game:
    def __init__(self, opponent, difficulty, player_color,window):
        self.opponent = opponent
        self.difficulty = difficulty
        self.player_color = player_color
        self.board = Board(window, 4, player_color!='white')
        self.turn = 'white'
        self.piece_selected=False
        ai_color = 'black' if player_color == 'white' else 'white'
        self.ai = Ai(difficulty, ai_color, self.board) if self.opponent == "computer" else None
    
        
    def undo_move(self):# POPRAVI OVO PROTIV KOMPA
        if not self.board.undo_move():
            return
        
        self.flip_turn()
        self.display()
        
        if not self.ai:
            return
        
        #self.ai.copy_move(self.board) # type: ignore
        
        if not self.board.undo_move():
            return
        
        #self.ai.copy_move(self.board) # type: ignore
        self.flip_turn()
        self.display()
        

    
    def flip_turn(self):
        self.turn = "black" if self.turn == "white" else "white"
        if self.opponent == "player":
            self.board.flipped = not self.board.flipped
    
    def ai_play(self):
        self.flip_turn()
        return self.ai.make_move(self.board)
    
    def check_click(self):
        '''Vraca igraca koji je pobedio'''
        row, col = InputHandler.get_square(self.board.flipped, self.board.size)
        if row is None or col is None:
            return None
        
        if not self.piece_selected:
            self.check_clicked_square(row, col)
            return None

        self.piece_selected = False
        
        succ, win = self.board.make_move(row, col, self.turn)
        
        if succ: 
            self.flip_turn()
            # if self.ai:
            #     self.ai.copy_move(self.board) # type: ignore
            self.piece_selected = False
            
        self.display()
            
        return win
    
    
    def check_clicked_square(self, row, col):
        self.piece_selected = self.board.check_legal_moves(row, col, self.turn)
        self.display()
    
    def make_move(self, clicked):
        
        if clicked:
            win = self.check_click()
            return win
            
        if self.ai and self.turn == self.ai.color: # type: ignore
            win = self.ai_play()
            self.display()
            return win
        
            
    def display(self):
        self.board.display(self.turn)
        self.board.display_last_move()
        pygame.display.flip()
                