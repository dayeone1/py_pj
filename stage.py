import pygame
from system import Button, ScreenChange
from character import *

class Table:
    def __init__(self):
        self.tile_images = {
            "White": pygame.image.load("img/tile/tile_white.png"),
            "Black": pygame.image.load("img/tile/tile_black.png"),
            "Red": pygame.image.load("img/tile/tile_red.png"),
            "Blue": pygame.image.load("img/tile/tile_blue.png"),
            "Yellow": pygame.image.load("img/tile/tile_yellow.png"),
            "Orange": pygame.image.load("img/tile/tile_orange.png"),
            "Green": pygame.image.load("img/tile/tile_green.png"),
            "Purple": pygame.image.load("img/tile/tile_purple.png"),
        }
        # 2차원 리스트 초기화
        self.tile = [[None for _ in range(5)] for _ in range(5)]
        self.tile_color = [[None for _ in range(5)] for _ in range(5)] 
        for i in range(0, 5):
            for j in range(0, 5):
                self.tile[i][j] = self.tile_images["White"]
                self.tile_color[i][j] = "White"
                
    def getTile(self, i, j):
        return self.tile[j][i]
    
    def setTile(self, i, j, color):
        self.tile[i][j] = self.tile_images[color]
        self.tile_color[i][j] = color

class Stage:
    def __init__(self, stageNumber, color):
        self.background = pygame.image.load("img/back/tree_1.png")
        self.base = pygame.image.load("img/tile/base.png")
        self.attack_on = pygame.image.load("img/interface/attack_button.png")
        self.attack_click = pygame.image.load("img/interface/attack_button_click.png")
        
        self.stageNumber = stageNumber # 몇 번째 스테이지 인지 확인
        self.color = color # 현재 선택된 컬러
        self.colorSet = {
            "Blue" : 0,
            "Red" : 1,
            "Yellow" : 2
        }
        self.xy = [(720, 470), (489, 7)] # 캐릭터, uiBox 좌표값
        
        self.table = Table()
        self.character = [Blue(), Red(), Yellow()]
        
        self.button_blue = Button("", self.character[0].getIndex(), self.character[0].getIndexClick(), 823, 395, 120, 75, lambda: self.setColor("Blue"))
        self.button_red = Button("", self.character[1].getIndex(), self.character[1].getIndexClick(), 1062 , 395, 120, 75, lambda: self.setColor("Red"))
        self.button_yellow = Button("", self.character[2].getIndex(), self.character[2].getIndexClick(), 942, 395, 120, 75, lambda: self.setColor("Yellow"))
        self.button_move = Button("move", self.attack_on, self.attack_click, 755, 503, 410, 70, lambda: self.character[self.colorSet[self.color]].move())
        self.button_attack = Button("attack", self.attack_on, self.attack_click, 755, 596, 410, 70, lambda: self.character[self.colorSet[self.color]].attack())
        
    def setColor(self, color):
        self.color = color 

    def show_stage(self, screen):
        
        screen.blit(self.background, (0,0))
        screen.blit(self.base, (85, 32))
        
        # 타일깔기
        for i in range(5):
            for j in range(5):
                screen.blit(self.table.getTile(i, j), (103+94*i, 50+94*j)) # 첫번째 칸의 위치 + 두번째 칸과의 간격 * i
        
        # while self.animaCheck:
        #     screen.blit(self.anima[frame], (107 + 94 * self.location_x, 32 + 94 * self.location_y)) 
        #     frame = (frame + 1) % len(self.anima)  # 프레임 업데이트
        #     pygame.display.update()  # 화면 업데이트
        #     pygame.time.wait(150)  # 150ms 대기
        
        screen.blit(self.character[0].getAnima(), (107 + 94 * self.character[0].getLocationX(), 32 + 94 * self.character[0].getLocationY()))
        screen.blit(self.character[1].getAnima(), (107 + 94 * self.character[1].getLocationX(), 32 + 94 * self.character[1].getLocationY()))
        screen.blit(self.character[2].getAnima(), (107 + 94 * self.character[2].getLocationX(), 32 + 94 * self.character[2].getLocationY()))
        
        screen.blit(self.character[self.colorSet[self.color]].getMainImg(), self.xy[1])
        screen.blit(self.character[self.colorSet[self.color]].getBox(), self.xy[0])    
                
        self.button_blue.draw(screen)
        self.button_red.draw(screen)
        self.button_yellow.draw(screen)
        self.button_move.draw(screen)
        self.button_attack.draw(screen)
        
        
class Stage_1(Stage):
    def __init__(self):
        super().__init__(1, "Blue")
    
    def show_stage(self, screen):
        self.table.setTile(4, 2,"Blue")
        self.character[0].setLocation(4, 2)
        self.table.setTile(2, 4, "Red")
        self.character[1].setLocation(2, 4)
        self.table.setTile(2, 0, "Yellow")
        self.character[2].setLocation(2, 0)
        super().show_stage(screen)
        
        