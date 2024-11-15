import pygame
import sys

class Character: 
    def __init__(self, color, main_img, box, index, index_click, anima):
        
        self.stamina = 100          # 캐릭터의 체력
        self.color = color          # 캐릭터의 색
        self.animaCheck = False     # 애니메이션 실행 여부
        self.main_img = pygame.image.load(main_img) # 메인 일러
        self.box = pygame.image.load(box) # ui 1(박스)
        self.index = pygame.image.load(index) # ui 2(인덱스)
        self.index_click = pygame.image.load(index_click) # 인덱스 클릭 여부
        # 애니메이션 파일
        self.anima = [
            pygame.image.load(anima[0]),pygame.image.load(anima[1]),pygame.image.load(anima[2])
        ]
        # 캐릭터의 현재 위치
        self.location_x = 0
        self.location_y = 0
    
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

    # 어디서 꼬인건지 행열 거꾸로 저장됨... 따라 거꾸로 반환
    def getLocationX(self):
        return self.location_y
    
    def getLocationY(self):
        return self.location_x
    
    def setLocation(self, x, y):
        self.location_x = x
        self.location_y = y
    
    def getAnima(self):
        return self.anima[0]
    
    def animaDraw(self, screen):
        self.animaCheck = True

    def animaStop(self):
        self.animaCheck = False
        
    
    

# player 캐릭터
class Red(Character):
    def __init__(self):
        self.anima = ["img/character/anima_red_0.png", "img/character/anima_red_1.png", "img/character/anima_red_2.png"]
        super().__init__("red", "img/character/character_red.png", "img/interface/box_red.png",
                         "img/interface/index_red.png", "img/interface/index_red_click.png", self.anima)

class Yellow(Character): 
    def __init__(self):
        self.anima = ["img/character/anima_yellow_0.png", "img/character/anima_yellow_1.png", "img/character/anima_yellow_2.png"]
        super().__init__("yellow", "img/character/character_yellow.png", "img/interface/box_yellow.png",
                         "img/interface/index_yellow.png", "img/interface/index_yellow_click.png", self.anima)
        
class Blue(Character):
    def __init__(self):
        self.anima = ["img/character/anima_blue_0.png", "img/character/anima_blue_1.png", "img/character/anima_blue_2.png"]
        super().__init__("blue", "img/character/character_blue.png", "img/interface/box_blue.png",
                         "img/interface/index_blue.png", "img/interface/index_blue_click.png", self.anima)


