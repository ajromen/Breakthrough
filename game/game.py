from game import board
from ui.input_handler import InputHandler

class Game:
    def __init__(self, opponent, dificulty, player_color,window):
        self.opponent = opponent
        self.dificulty = dificulty
        self.player_color = player_color
        self.board = board.Board(window, 8, player_color!='white')
        self.turn = 'white'
        self.piece_selected=False
    
    def display_board(self):
        self.board.display(self.player_color)
        
    def white_play(self):
        pass
        
    def black_play(self):
        pass
    
    def check_click(self):
        row, col = InputHandler.get_square(self.board.flipped)
        
        # print(row, col, self.board.board[row][col],self.board.flipped,self.turn)
        
        # for i in range(8):
        #     print(self.board.board[i])
                    
        
        if not self.piece_selected:
            self.piece_selected = self.board.check_legal_moves(row, col, self.turn)
            return self.piece_selected, None
        
        
        self.piece_selected=False
        succ, win = self.board.make_move(row, col, self.turn)
        
        if win:
            return True, self.turn # ako je pobedio vraca True za uspesan potez i igraca koji je pobedio
        
        if succ: 
            self.turn = "black" if self.turn == "white" else "white"
            if self.opponent=="player":
                self.board.flipped= not self.board.flipped
                
        return True, None
        
            
                