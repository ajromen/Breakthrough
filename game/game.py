import pygame
from game.board.board import Board
from ui.input_handler import InputHandler
from game.ai import Ai

class Game:
    def __init__(self, opponent, difficulty, player_color,window, size=8):
        self.opponent = opponent
        self.difficulty = difficulty
        self.player_color = player_color
        self.board = Board(window, size, player_color!='white')
        self.turn = 'white'
        self.piece_selected=False
        ai_color = 'black' if player_color == 'white' else 'white'
        self.ai = Ai(difficulty, ai_color, self.board) if self.opponent == "computer" or self.opponent=='computer_vs_computer' else None
        self.ai2 = Ai(difficulty, player_color, self.board) if self.opponent == "computer_vs_computer" else None
    
        
    def undo_move(self):
        if not self.board.undo_move():
            return
        
        self.flip_turn()
        self.display()
        
        if not self.ai:
            return
        
        if not self.board.undo_move():
            return
        
        self.flip_turn()
        self.display()
        

    
    def flip_turn(self):
        self.turn = "black" if self.turn == "white" else "white"
        if self.opponent == "player":
            self.board.flipped = not self.board.flipped
    
    def ai_play(self,ai:Ai):
        self.flip_turn()
        return ai.make_move(self.board)
    
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
        
        if self.ai2 and self.turn == self.player_color:
            win = self.ai_play(self.ai2)
            self.display()
            return win
            
        if self.ai and self.turn == self.ai.color: 
            win = self.ai_play(self.ai)
            self.display()
            return win        
            
    def display(self):
        self.board.display(self.turn)
        self.board.display_last_move()
        pygame.display.flip()
                