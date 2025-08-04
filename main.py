import pygame
from utils import colors
from utils.image_menager import ImageMenager


window_size = (800, 800)

window = pygame.display.set_mode(window_size, pygame.NOFRAME)

pygame.display.set_caption("Breaktrough")

def main():
    pygame.init()
    clock = pygame.time.Clock()
    ImageMenager.load_all(ImageMenager)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(colors.background)  
        window.blit(ImageMenager.tabla, (27, 27))
        pygame.display.flip()  

        clock.tick(60) 

    pygame.quit()
    
if __name__ == "__main__":
    main() 