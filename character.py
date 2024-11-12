import pygame
import sys

class Character: 
    def __init__(self):     
        self.stamina = 100
        self.color = ""
        self.color_img = None
        self.main_img = None 
        self.ain_img = []
    
    def getMainImg(self):
        return self.main_img
    def attack(self, i, j):
        return None


# player 캐릭터
class Red(Character):
    def __init__(self):
        super().__init__()
        self.color = "red"
        self.main_img = pygame.image.load("img/character/character_red.png")
        
    def getMainImg(self):
        return super().getMainImg()

class Yellow(Character): 
    def __init__(self):
        super().__init__()
        self.color = "yellow" 
        self.main_img = pygame.image.load("img/character/character_yellow.png")
        
    def getMainImg(self):
        return super().getMainImg()
        
class Blue(Character):
    def __init__(self):
        super().__init__()
        self.color = "blue"
        self.main_img = pygame.image.load("img/character/character_blue.png")
        
    def getMainImg(self):
        return super().getMainImg()


