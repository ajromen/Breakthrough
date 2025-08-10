import pygame
from game.game import Game
from ui import colors
from ui.image_menager import ImageMenager
from ui import menu
from ui.input_handler import InputHandler

pygame.init()

window_size = (800, 800)



def main():
    window = pygame.display.set_mode(window_size, pygame.NOFRAME)
    pygame.display.set_caption("Breaktrough")
    clock = pygame.time.Clock()
    ImageMenager.load_all()

    ui = menu.Menu(window)
    
    running = True
    while running:
        
        props = ui.start_main()
        
        opponent = props['opponent']
        dificulty = props['dificulty']
        player_color = props['player_color']
        game = Game(opponent, dificulty, player_color, window)
        
        redraw_needed = True
        game_running = True       
        win = None
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    redraw_needed, win = game.check_click()
                        
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        do = ui.show_settings()
                        redraw_needed=True
                        if do == 'exit':
                            return
                        elif do == 'menu':
                            game_running=False
                            break
            
            if redraw_needed: 
                game.display_board()
                game.board.display_last_move()
                pygame.display.flip()  
                redraw_needed=False
                if win:
                    ui.show_winner(win)
                    do = ui.show_settings(no_exit=True)
                    
                    if do == 'exit':
                        running = False
                        game_running = False
                    elif do == 'menu':
                        game_running = False
                        break
                
            
            clock.tick(30)
                  

    pygame.quit()
    
if __name__ == "__main__":
    main() 