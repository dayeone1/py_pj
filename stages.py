import pygame
from system import Button, ScreenChange

class StageCheck:
    def __init__(self):
        self.screenChange = ScreenChange()
        
        # 이미지 로드
        self.background = pygame.image.load("img/back/tree_1.png")
        self.line = pygame.image.load("img/interface/line.png")
        self.menu = pygame.image.load("img/interface/menu_bar.png")
        self.menu_button_on = pygame.image.load("img/interface/menu_button.png")        
        self.menu_button_click = pygame.image.load("img/interface/menu_button_click.png")
        self.stage_button_on = pygame.image.load("img/interface/stage_button.png")
        self.stage_button_click = pygame.image.load("img/interface/stage_button_click.png")
        
        self.xy = [85, 232, 303, 480, 430, 73, 611, 320, 876, 480, 913,146] # 순서대로 각 버튼 x, y 좌표
        self.stages = []
        # stage_button 초기화
        for i in range(0, 6):
            self.stages.append(Button(str(i+1), self.stage_button_on, self.stage_button_click, self.xy[i*2], self.xy[i*2+1], 
                                      160, 160, lambda i=i: self.screenChange.setScreen(3+i)))
            
        self.menu_button1 = Button("처음으로", self.menu_button_on, self.menu_button_click, 
                                   871, 29, 140, 70, lambda: self.screenChange.setScreen(0))
        
        
    def show_stages(self, screen):
        
        pygame.event.wait(100)
        screen.blit(self.background, (0,0))
        screen.blit(self.line, (165,146))
        screen.blit(self.menu, (850, 16))
        self.menu_button1.draw(screen)
        
        for stage in self.stages:
            stage.draw(screen) 