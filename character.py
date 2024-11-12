import pygame
import sys

class Character: 
    def __init__(self, color, main_img):     
        self.stamina = 100
        self.color = color
        self.main_img = pygame.image.load(main_img)
    
    def getMainImg(self):
        return self.main_img
    
    def attack(self, i, j):
        return None

# player 캐릭터
class Red(Character):
    def __init__(self):
        super().__init__("red", "img/character/character_red.png")

class Yellow(Character): 
    def __init__(self):
        super().__init__("yellow", "img/character/character_yellow.png")
        
class Blue(Character):
    def __init__(self):
        super().__init__("blue", "img/character/character_blue.png")

class Table:
    def __init__(self):
        self.base = pygame.image.load("img/tile/base.png")
        self.tile_white = pygame.image.load("img/tile/tile_white.png")
        self.tile_black = pygame.image.load("img/tile/tile_black.png")
        self.tile_red = pygame.image.load("img/tile/tile_red.png")
        self.tile_blue = pygame.image.load("img/tile/tile_blue.png")
        self.tile_yellow = pygame.image.load("img/tile/tile_yellow.png")
        self.tile_orange = pygame.image.load("img/tile/tile_orange.png")
        self.tile_green = pygame.image.load("img/tile/tile_green.png")
        self.tile_purple = pygame.image.load("img/tile/tile_purple.png")
        
        # 2차원 리스트 초기화
        self.tile = [[None for _ in range(5)] for _ in range(5)]
        self.tile_color = [[None for _ in range(5)] for _ in range(5)] 
        for i in range(0, 5):
            for j in range(0, 5):
                self.tile[i][j] = self.tile_white
                self.tile_color[i][j] = "white"
