import pygame
from system import Button, ScreenChange

class StageCheck:
    def __init__(self):
        self.background = pygame.image.load("img/back/tree_1.png")
        self.line = pygame.image.load("img/interface/line.png")
        self.menu = pygame.image.load("img/interface/menu_bar.png")
        self.line = pygame.image.load("img/interface/line.png")
        
    def show_stage(self, screen):  
        screen.blit(self.background, (0,0))