import pygame

from ui.input_handler import InputHandler
from utils import colors
from utils.image_menager import ImageMenager


class Menu():
    def __init__(self,window: pygame.Surface):
        self.window = window
        
    def start_main(self):
        settings = {
            'opponent': 'player',
            'dificulty': 1,
            'player_color': 'white'
        }
        
        opponent = self.choose_opponent()
        
        if opponent =='player':
            return settings
        
        dificulty = self.choose_dificulty()
        player_color = self.choose_color()
        
        settings['opponent']=opponent
        settings['dificulty']=dificulty
        settings['player_color'] = player_color
        
        return settings

    def choose_opponent(self):
        pos1 = (83, 256)
        pos2 = (83, 256 + 159)
        pvp_rect = pygame.Rect(83, 256, 635, 111)
        pvc_rect = pygame.Rect(83, 256 + 159, 635, 111)
        running = True
        while running:
            clicked = self.checkQuit()
            self.window.fill(colors.background)  
            
            self.window.blit(ImageMenager.pvp, pos1) # type: ignore
            self.window.blit(ImageMenager.pvc, pos2) # type: ignore
            
            

            if InputHandler.check_mouse_hover(InputHandler,pvp_rect):
                pygame.draw.rect(self.window, colors.selected, pvp_rect, 2, border_radius=5)
                if clicked:
                    return 'player'
            if InputHandler.check_mouse_hover(InputHandler,pvc_rect):
                pygame.draw.rect(self.window, colors.selected, pvc_rect, 2, border_radius=5)
                if clicked:
                    return 'computer'
            
        return 'player'
    
    def choose_dificulty(self):
        return 1
    
    def choose_color(self):
        white = (147, 327)
        black = (147 +359, 327 )
        next = (81, 554)
        white_rect = pygame.Rect(147, 327, 147, 147)
        black_rect = pygame.Rect(147 + 359, 327, 147, 147)
        next_rect = pygame.Rect(83, 554, 635, 111)
        selected = 'white'
        
        font_50 = pygame.font.Font("assets/JetBrainsMono-Regular.ttf", 50)
        text_surface_50 = font_50.render("or", True, colors.selected)
        
        font_60 = pygame.font.Font("assets/JetBrainsMono-Regular.ttf", 60)
        text_surface_60 = font_60.render("Start as", True, colors.selected)
        
        running = True
        while running:
            clicked = self.checkQuit()
            self.window.fill(colors.background)  
            
            self.window.blit(ImageMenager.piece_white_xl, white) # type: ignore
            self.window.blit(ImageMenager.piece_black_xl, black) # type: ignore
            self.window.blit(ImageMenager.start, next) # type: ignore
            
            
            self.window.blit(text_surface_50, (370, 367))
            
            
            self.window.blit(text_surface_60, (256, 137))

            if InputHandler.check_mouse_hover(InputHandler,white_rect):
                pygame.draw.rect(self.window, colors.highlight, white_rect, 2, border_radius=5)
                if clicked:
                    selected = 'white'
                    
            if InputHandler.check_mouse_hover(InputHandler,black_rect):
                pygame.draw.rect(self.window, colors.highlight, black_rect, 2, border_radius=5)
                if clicked:
                    selected = 'black'
            
            if InputHandler.check_mouse_hover(InputHandler, next_rect):
                pygame.draw.rect(self.window, colors.selected, next_rect, 2, border_radius=5)
                if clicked:
                    return selected
            
        return selected
    
    def checkQuit(self):
        pygame.display.flip()  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return True
        return False