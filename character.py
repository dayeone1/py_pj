import pygame
import sys

class Character: 
    def __init__(self, color, main_img, box, index, index_click):     
        self.stamina = 100
        self.color = color
        self.main_img = pygame.image.load(main_img)
        self.box = pygame.image.load(box)
        self.index = pygame.image.load(index)
        self.index_click = pygame.image.load(index_click)
        
    def attack(self, i, j):
        return None
    
    def getMainImg(self):
        return self.main_img
    
    def getColor(self):
        return self.color
    
    def getBox(self):
        return self.box
    
    def getIndex(self):
        return self.index
    
    def getIndexClick(self):
        return self.index_click
    
    

# player 캐릭터
class Red(Character):
    def __init__(self):
        super().__init__("red", "img/character/character_red.png", "img/interface/box_red.png",
                         "img/interface/index_red.png", "img/interface/index_red_click.png")

class Yellow(Character): 
    def __init__(self):
        super().__init__("yellow", "img/character/character_yellow.png", "img/interface/box_yellow.png",
                         "img/interface/index_yellow.png", "img/interface/index_yellow_click.png")
        
class Blue(Character):
    def __init__(self):
        super().__init__("blue", "img/character/character_blue.png", "img/interface/box_blue.png",
                         "img/interface/index_blue.png", "img/interface/index_blue_click.png")

class Table:
    def __init__(self):

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
                
    def getTile(self, i, j):
        return self.tile[i][j]
