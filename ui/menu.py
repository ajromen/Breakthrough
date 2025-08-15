import pygame

from ui.text_renderer import TextRenderer
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
        if opponent == 'computer_vs_computer':
            player_color = 'white'
        else:
            player_color = self.choose_color()
        
        settings['opponent']=opponent
        settings['dificulty']=dificulty
        settings['player_color'] = player_color
        
        return settings

    def choose_opponent(self):
        pos1 = (83, 201)
        pos2 = (83, 344)
        pos3 = (83, 487)
        pvp_rect = pygame.Rect(83, pos1[1], 635, 111)
        pvc_rect = pygame.Rect(83, pos2[1], 635, 111)
        cvc_rect = pygame.Rect(83, pos3[1], 635, 111)
        running = True
        selected = None
        options = ['player', 'computer', 'computer_vs_computer']
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
                        if selected is None:
                            selected = 'player'
                        else:
                            selected = options[(options.index(selected) - 1) % len(options)]
                    elif event.key == pygame.K_DOWN:
                        if selected is None:
                            selected = 'computer_vs_computer'
                        else:
                            selected = options[(options.index(selected) + 1) % len(options)]
                    elif event.key == pygame.K_ESCAPE:
                        do=self.show_settings()
                        if do == 'exit':
                            pygame.quit()
                        
            self.window.fill(colors.background)  
            
            self.window.blit(ImageMenager.pvp, pos1) # type: ignore
            self.window.blit(ImageMenager.pvc, pos2) # type: ignore
            self.window.blit(ImageMenager.cvc, pos3) # type: ignore
            
            if selected == 'player':
                pygame.draw.rect(self.window, colors.highlight, pvp_rect, 2, border_radius=5)
            elif selected == 'computer':
                pygame.draw.rect(self.window, colors.highlight, pvc_rect, 2, border_radius=5)
            elif selected == 'computer_vs_computer':
                pygame.draw.rect(self.window, colors.highlight, cvc_rect, 2, border_radius=5)
            
            
            if InputHandler.check_mouse_hover(pvp_rect):
                pygame.draw.rect(self.window, colors.selected, pvp_rect, 2, border_radius=5)
                if clicked:
                    return 'player'
            if InputHandler.check_mouse_hover(pvc_rect): # type: ignore
                pygame.draw.rect(self.window, colors.selected, pvc_rect, 2, border_radius=5)
                if clicked:
                    return 'computer'
            if InputHandler.check_mouse_hover(cvc_rect):
                pygame.draw.rect(self.window, colors.selected, cvc_rect, 2, border_radius=5)
                if clicked:
                    return 'computer_vs_computer'
            
        return 'player'
    
    def choose_dificulty(self):
        dificulty = 2
        slider = (85, 470+42)
        ellipse_y = 470 + 42+5
                
        while True:
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
                        return dificulty
                    elif event.key == pygame.K_LEFT:
                        dificulty= max(1, dificulty - 1)
                    elif event.key == pygame.K_RIGHT:
                        dificulty = min(10, dificulty + 1)
                        
            self.window.fill(colors.background)
            TextRenderer.render_text("Dificulty level", 60, colors.selected, (128, 262), self.window)
            TextRenderer.render_text("seconds", 40, colors.muted, (313, 341), self.window)
            
            self.window.blit(ImageMenager.slider, slider) # type: ignore
            
            ellipse_x = 85 + 26 + (dificulty - 1) * 62
            
            pygame.draw.ellipse(self.window, colors.highlight, (ellipse_x, ellipse_y, 25, 25))

            slider_rect = pygame.Rect(86+26, 470 + 42 + 5, 9 * 62 + 25, 25)
            if InputHandler.check_mouse_hover(slider_rect) and clicked:
                mouse_x, _ = pygame.mouse.get_pos()
                dificulty = min(10, max(1, 1 + (mouse_x - 85) // 62))
        
    
    def choose_color(self):
        white = (141, 402)
        black = (141 + 359, 402 )
        next = (81, 554)
        white_rect = pygame.Rect(139, 392, 170, 170)
        black_rect = pygame.Rect(139 + 359, 392, 170, 170)
        selected = None     
        
        while True:
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
                    elif event.key == pygame.K_LEFT:
                        selected = 'white'
                    elif event.key == pygame.K_RIGHT:
                        selected = 'black'
            
            
            self.window.fill(colors.background)  
            
            self.window.blit(ImageMenager.piece_white_xl, white) # type: ignore
            self.window.blit(ImageMenager.piece_black_xl, black) # type: ignore
            
            
            TextRenderer.render_text("Start as", 60 , colors.selected, (256, 240), self.window)
            TextRenderer.render_text("or", 50, colors.selected, (364, 444), self.window)
            
        
            if(selected=='white'):
                pygame.draw.rect(self.window, colors.highlight, white_rect, 2, border_radius=5)
            elif(selected=='black'):
                pygame.draw.rect(self.window, colors.highlight, black_rect, 2, border_radius=5)


            if InputHandler.check_mouse_hover(white_rect):
                pygame.draw.rect(self.window, colors.selected, white_rect, 2, border_radius=5)
                if clicked:
                    return 'white'
                    
            if InputHandler.check_mouse_hover(black_rect):
                pygame.draw.rect(self.window, colors.selected, black_rect, 2, border_radius=5)
                if clicked:
                    return 'black'
            
            
    
    def show_settings(self, no_exit=False):
        clicked = False
        menu_btn =  pygame.Rect(88+42, 230+44, 560, 111)
        exit_btn = pygame.Rect(88+42, 230+192, 560, 111)
        selected = None
        clock = pygame.time.Clock()
        
        self.window.blit(ImageMenager.settings, (88-10, 230)) # type: ignore
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and not no_exit:
                        return False 
                    elif event.key == pygame.K_RETURN:
                        if selected is None:
                            continue
                        return selected
                    elif event.key == pygame.K_UP:
                        selected = 'menu'
                    elif event.key == pygame.K_DOWN:
                        selected = 'exit'
            
            self.window.blit(ImageMenager.settings_no_shadow, (98, 230)) # type: ignore
            
            
            if selected == 'menu':
                pygame.draw.rect(self.window, colors.highlight, menu_btn, 2, border_radius=5)
            elif selected == 'exit':
                pygame.draw.rect(self.window, colors.highlight, exit_btn, 2, border_radius=5)
            
            if InputHandler.check_mouse_hover( menu_btn):
                pygame.draw.rect(self.window, colors.selected, menu_btn, 2, border_radius=5)
                if clicked:
                    return 'menu'
            
            if InputHandler.check_mouse_hover( exit_btn):
                pygame.draw.rect(self.window, colors.selected, exit_btn, 2, border_radius=5)
                if clicked:
                    return 'exit'
                
            clock.tick(30)
            pygame.display.flip()  
            
    def show_winner(self, winner):
        if winner == 'white':
            image = ImageMenager.white_wins
        else:
            image = ImageMenager.black_wins
            
        self.window.blit(ImageMenager.win_shadow, (88-10, 323-3)) # type: ignore
        self.window.blit(image, (88, 323)) # type: ignore
        while True:
            clicked = False
            pygame.display.flip()  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                        return 'menu'

        
        