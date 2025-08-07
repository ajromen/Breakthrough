import pygame

from ui.input_handler import InputHandler
from ui import colors
from ui.image_menager import ImageMenager


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
        selected = None
        while running:
            clicked = False
            pygame.display.flip()  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if selected is None:
                            continue
                        return selected
                    elif event.key == pygame.K_UP:
                        selected = 'player'
                    elif event.key == pygame.K_DOWN:
                        selected = 'computer'
                        
            self.window.fill(colors.background)  
            
            self.window.blit(ImageMenager.pvp, pos1) # type: ignore
            self.window.blit(ImageMenager.pvc, pos2) # type: ignore
            
            if selected == 'player':
                pygame.draw.rect(self.window, colors.highlight, pvp_rect, 2, border_radius=5)
            elif selected == 'computer':
                pygame.draw.rect(self.window, colors.highlight, pvc_rect, 2, border_radius=5)
            
            
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
        white = (141, 402)
        black = (141 + 359, 402 )
        next = (81, 554)
        white_rect = pygame.Rect(141, 393, 170, 170)
        black_rect = pygame.Rect(141 + 359, 393, 170, 170)
        selected = None     
        
        
        font_50 = pygame.font.Font("assets/JetBrainsMono-Regular.ttf", 50)
        text_surface_50 = font_50.render("or", True, colors.selected)
        
        font_60 = pygame.font.Font("assets/JetBrainsMono-Regular.ttf", 60)
        text_surface_60 = font_60.render("Start as", True, colors.selected)
        
        running = True
        while running:
            clicked = False
            
            pygame.display.flip()  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return selected
                    elif event.key == pygame.K_LEFT:
                        selected = 'white'
                    elif event.key == pygame.K_RIGHT:
                        selected = 'black'
            
            
            self.window.fill(colors.background)  
            
            self.window.blit(ImageMenager.piece_white_xl, white) # type: ignore
            self.window.blit(ImageMenager.piece_black_xl, black) # type: ignore
            
            
            self.window.blit(text_surface_50, (364, 444))                        
            self.window.blit(text_surface_60, (256, 240))
        
            if(selected=='white'):
                pygame.draw.rect(self.window, colors.highlight, white_rect, 2, border_radius=5)
            elif(selected=='black'):
                pygame.draw.rect(self.window, colors.highlight, black_rect, 2, border_radius=5)


            if InputHandler.check_mouse_hover(InputHandler,white_rect):
                pygame.draw.rect(self.window, colors.selected, white_rect, 2, border_radius=5)
                if clicked:
                    return 'white'
                    
            if InputHandler.check_mouse_hover(InputHandler,black_rect):
                pygame.draw.rect(self.window, colors.selected, black_rect, 2, border_radius=5)
                if clicked:
                    return 'black'
            
            
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
    
    def show_settings(self, ):
        clicked = False
        menu_btn =  pygame.Rect(98+42, 230+44, 560, 111)
        exit_btn = pygame.Rect(98+42, 230+192, 560, 111)
        selected = None
        clock = pygame.time.Clock()
        
        self.window.blit(ImageMenager.settings, (98, 230)) # type: ignore
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                    elif event.key == pygame.K_RETURN:
                        if selected is None:
                            continue
                        return selected
                    elif event.key == pygame.K_UP:
                        selected = 'menu'
                    elif event.key == pygame.K_DOWN:
                        selected = 'exit'
            
            self.window.blit(ImageMenager.settings_no_shadow, (108, 233)) # type: ignore
            
            
            if selected == 'menu':
                pygame.draw.rect(self.window, colors.highlight, menu_btn, 2, border_radius=5)
            elif selected == 'exit':
                pygame.draw.rect(self.window, colors.highlight, exit_btn, 2, border_radius=5)
            
            if InputHandler.check_mouse_hover(InputHandler, menu_btn):
                pygame.draw.rect(self.window, colors.selected, menu_btn, 2, border_radius=5)
                if clicked:
                    return 'menu'
            
            if InputHandler.check_mouse_hover(InputHandler, exit_btn):
                pygame.draw.rect(self.window, colors.selected, exit_btn, 2, border_radius=5)
                if clicked:
                    return 'exit'
                
            clock.tick(60)
            pygame.display.flip()  