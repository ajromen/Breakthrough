import pygame
from game.game import Game
from ui import colors
from ui.image_menager import ImageMenager
from ui import menu

pygame.init()

window_size = (800, 800)



def main():
    window = pygame.display.set_mode(window_size, pygame.NOFRAME)
    pygame.display.set_caption("Breaktrough")
    clock = pygame.time.Clock()
    ImageMenager.load_all(ImageMenager)
    
    ui = menu.Menu(window)
    
    running = True
    while running:
        
        
        props = ui.start_main()
        
        opponent = props['opponent']
        dificulty = props['dificulty']
        player_color = props['player_color']
        game = Game(opponent, dificulty, player_color, window)
        
        game_running = True        
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_running = False
                    
            game.display_board()
            
            pygame.display.flip()  

            clock.tick(30) 
                
                
        
        
        

    pygame.quit()
    
if __name__ == "__main__":
    main() 