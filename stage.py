import pygame
from system import Button, ScreenChange
from character import *
from keys import Game_system

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
    def __init__(self, stageNumber):
        self.background = pygame.image.load("img/back/tree_1.png")
        self.base = pygame.image.load("img/tile/base.png")
        
        self.stageNumber = stageNumber # 몇 번째 스테이지 인지 확인
      
        self.blue = Blue()
        self.red = Red()
        self.yellow = Yellow()
        
        self.table = Table()
        self.gameSystem = Game_system()

    def show_stage(self, screen):
        
        screen.blit(self.background, (0,0))
        screen.blit(self.base, (85, 32))
        
        # 타일깔기
        for i in range(5):
            for j in range(5):
                screen.blit(self.table.getTile(i, j), (103+94*i, 50+94*j)) # 첫번째 칸의 위치 + 두번째 칸과의 간격 * i
        
        # 애니메이션을 구현 할려 했던......
        # while self.animaCheck:
        #     screen.blit(self.anima[frame], (107 + 94 * self.location_x, 32 + 94 * self.location_y)) 
        #     frame = (frame + 1) % len(self.anima)  # 프레임 업데이트
        #     pygame.display.update()  # 화면 업데이트
        #     pygame.time.wait(150)  # 150ms 대기
        
        screen.blit(self.blue.getAnima(), (107 + 94 * self.blue.getLocationX(), 32 + 94 * self.blue.getLocationY()))
        screen.blit(self.red.getAnima(), (107 + 94 * self.red.getLocationX(), 32 + 94 * self.red.getLocationY()))
        screen.blit(self.yellow.getAnima(), (107 + 94 * self.yellow.getLocationX(), 32 + 94 * self.yellow.getLocationY()))
        
        self.gameSystem.show(screen)
                
        
        
class Stage_1(Stage):
    def __init__(self):
        super().__init__(1)
    
    def show_stage(self, screen):
        self.table.setTile(4, 2,"Blue")
        self.blue.setLocation(4, 2)
        self.table.setTile(2, 4, "Red")
        self.red.setLocation(2, 4)
        self.table.setTile(2, 0, "Yellow")
        self.yellow.setLocation(2, 0)
        super().show_stage(screen)
        
        