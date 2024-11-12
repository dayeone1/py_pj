import pygame
from system import Button, ScreenChange
from character import *

class Stage:
    def __init__(self, stageNumber, color):
        self.background = pygame.image.load("img/back/tree_1.png")
        self.base = pygame.image.load("img/tile/base.png")
        
        self.stageNumber = stageNumber
        self.color = color
        self.xy = [(720, 470), (489, 7)]
        
        self.table = Table()
        self.blue = Blue()
        self.red = Red()
        self.yellow = Yellow()
        
        self.button_blue = Button("", self.blue.getIndex(), self.blue.getIndexClick(), 823, 395, 120, 75, lambda: self.setColor("Blue"))
        self.button_red = Button("", self.red.getIndex(), self.red.getIndexClick(), 1062 , 395, 120, 75, lambda: self.setColor("Red"))
        self.button_yellow = Button("", self.yellow.getIndex(), self.yellow.getIndexClick(), 942, 395, 120, 75, lambda: self.setColor("Yellow"))
        
    def setColor(self, color):
        self.color = color 

    def show_stage(self, screen):
        screen.blit(self.background, (0,0))
        screen.blit(self.base, (85, 32))
        
        for i in range(5):
            for j in range(5):
                screen.blit(self.table.getTile(i, j), (103+94*i, 50+94*j))
                
        if self.color == "Blue":
            screen.blit(self.blue.getMainImg(), self.xy[1])
            screen.blit(self.blue.getBox(), self.xy[0])
            
        elif self.color == "Red":
            screen.blit(self.red.getMainImg(), self.xy[1])
            screen.blit(self.red.getBox(), self.xy[0])
            
        elif self.color == "Yellow":
            screen.blit(self.yellow.getMainImg(), self.xy[1])
            screen.blit(self.yellow.getBox(), self.xy[0])
            
                
        self.button_blue.draw(screen)
        self.button_red.draw(screen)
        self.button_yellow.draw(screen)
        
        
        
    
class Stage_1(Stage):
    def __init__(self):
        super().__init__(1, "Blue")
    
    def show_stage(self, screen):
        super().show_stage(screen)
        