from game import board

class Game:
    def __init__(self, opponent, dificulty, player_color,window):
        self.opponent = opponent
        self.dificulty = dificulty
        self.player_color = player_color
        self.board = board.Board(window, 8, player_color!='white')
        self.turn = 'white'
    
    def display_board(self):
        self.board.display(self.player_color)
        
    def white_play(self):
        pass
        
    def black_play(self):
        pass
    
    def check_legal_moves(self, row, col):
        return self.board.check_legal_moves(row,col,self.turn)