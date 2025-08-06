from game import board

class Game:
    def __init__(self, opponent, dificulty, player_color,window):
        self.opponent = opponent
        self.dificulty = dificulty
        self.player_color = player_color
        self.board = board.Board(window)
    
    def display_board(self):
        self.board.display(self.player_color)