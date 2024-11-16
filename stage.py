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
        
        self.TILE_GAP = 94
                
    def getTile(self, i, j):
        return self.tile[j][i]
    
    def setTile(self, i, j, color):
        self.tile[i][j] = self.tile_images[color]
        self.tile_color[i][j] = color
        
    def getTileGap(self):
        return self.TILE_GAP

class Stage:
    def __init__(self, stageNumber):
        pygame.init()
        self.table = Table()

        
        self.background = pygame.image.load("img/back/tree_1.png")
        self.base = pygame.image.load("img/tile/base.png")
        
        self.attack_on = pygame.image.load("img/interface/attack_button.png")
        self.attack_click = pygame.image.load("img/interface/attack_button_click.png")
        self.spot = pygame.image.load("img/tile/spot.png")
        
        self.event = 0
        self.color = "Blue" # 현재 선택된 컬러
        self.colorSheet = {
            "Blue" : 0,
            "Red" : 1,
            "Yellow" : 2
        }
        
        self.character = [Blue(), Red(), Yellow()]
        
        self.xy = [(720, 470), (489, 7)] # 캐릭터, uiBox 좌표값
        self.attack_arear = []
        
        # 색 변경하는 인덱스들
        self.button_blue = Button("", self.character[0].getIndex(), self.character[0].getIndexClick(), 823, 395, 120, 75, lambda: self.setColor("Blue"))
        self.button_red = Button("", self.character[1].getIndex(), self.character[1].getIndexClick(), 1062 , 395, 120, 75, lambda: self.setColor("Red"))
        self.button_yellow = Button("", self.character[2].getIndex(), self.character[2].getIndexClick(), 942, 395, 120, 75, lambda: self.setColor("Yellow"))
        
        # 공격, 이동
        self.button_attack = Button("attack", self.attack_on, self.attack_click, 755, 503, 410, 70, lambda: self.setEvent(1))
        self.button_move = Button("move", self.attack_on, self.attack_click, 755, 596, 410, 70, lambda: self.setEvent(2))
        
        self.stageNumber = stageNumber # 몇 번째 스테이지 인지 확인
        
        
    def show_stage(self, screen):
        
        screen.blit(self.background, (0,0))
        screen.blit(self.base, (85, 32))
    
        # 타일깔기
        for i in range(5):
            for j in range(5):
                screen.blit(self.table.getTile(i, j), (103+self.table.getTileGap()*i, 50+self.table.getTileGap()*j)) # 첫번째 칸의 위치 + 두번째 칸과의 간격 * i
        
        # 애니메이션을 구현 할려 했던......
        # while self.animaCheck:
        #     screen.blit(self.anima[frame], (107 + 94 * self.location_x, 32 + 94 * self.location_y)) 
        #     frame = (frame + 1) % len(self.anima)  # 프레임 업데이트
        #     pygame.display.update()  # 화면 업데이트
        #     pygame.time.wait(150)  # 150ms 대기
        
        screen.blit(self.character[0].getAnima(), (107 +  self.table.getTileGap() * self.character[0].getLocationX(),
                                        32 + self.table.getTileGap() * self.character[0].getLocationY()))
        screen.blit(self.character[1].getAnima(), (107 + self.table.getTileGap() * self.character[1].getLocationX(), 
                                        32 + self.table.getTileGap() * self.character[1].getLocationY()))
        screen.blit(self.character[2].getAnima(), (107 + self.table.getTileGap() * self.character[2].getLocationX(), 
                                        32 + self.table.getTileGap() * self.character[2].getLocationY()))
        
        # 선택된 컬러의 함수 저장용
        self.select_color = self.character[self.colorSheet[self.color]]
        
        screen.blit(self.select_color.getMainImg(), self.xy[1])
        screen.blit(self.select_color.getBox(), self.xy[0])
        
        if self.event == 0:
            self.default(screen)
        elif self.event == 1:
            self.attack(screen)
        elif self.event == 2:
            self.move(screen)
        
    def attackArea(self): 
        count = 0
        
        # 어디서부터 오류인진 모르나 일단 x y 가 뒤바뀐 관계로 뒤집어서,,..
        xy = [self.select_color.getLocationY(), self.select_color.getLocationX()]
        
        self.attackAreaX = []
        self.attackAreaY = []
        arrayArea = [[-1, 1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]]
        for i in range(8):
            for j in range(2):
                if xy[j] + arrayArea[j][i] < 0 and xy[j] + arrayArea[j][i] > 4 :
                    break
                count += 1
            if count == 2:
                self.attackAreaY.append(xy[0]+arrayArea[0][i])
                self.attackAreaX.append(xy[1]+arrayArea[1][i])
            count = 0
        
        print(self.attackAreaX[0], self.attackAreaY[0])
        print(xy)
        
    def attack(self, screen):
        self.attackArea()
        self.paint = 0
        
        screen.blit(self.spot,(self.table.getTileGap() * self.attackAreaX[0] + 103, self.table.getTileGap() * self.attackAreaY[0] + 50))

    def setPaint(self, num):
        self.paint = num
    
    def setColor(self, color):
        self.color = color 
        
    def getColor(self, color):
        return color
        
    def getEvent(self):
        return self.event
    
    def setEvent(self, number):
        self.event = number
        
    def default(self, screen):
        self.button_blue.draw(screen)
        self.button_red.draw(screen)
        self.button_yellow.draw(screen)
        
        self.button_attack.draw(screen)
        self.button_move.draw(screen)
        
    def move(self, screen):
        return None
        
class Stage_1(Stage):
    def __init__(self):
        super().__init__(1)
    
    def show_stage(self, screen):
        self.table.setTile(4, 2,"Blue")
        self.character[0].setLocation(4, 2)
        self.table.setTile(2, 4, "Red")
        self.character[1].setLocation(2, 4)
        self.table.setTile(2, 0, "Yellow")
        self.character[2].setLocation(2, 0)
        super().show_stage(screen)
        
        