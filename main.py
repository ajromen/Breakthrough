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
        game = Game(opponent, dificulty, player_color, window,8)
        
        game_running = True       
        win = None
        clicked = False
        game.display()
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                        
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        do = ui.show_settings()
                        game.display()
                        if do == 'exit':
                            return
                        elif do == 'menu': 
                            game_running=False
                            break
                    elif event.key == pygame.K_z:
                        game.undo_move()
                        
            win = game.make_move(clicked)
            clicked = False
            
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