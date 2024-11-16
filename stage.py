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
        self.tile = []
        self.tile_color = [] 
        self.character_L = []
        for i in range(0, 5):
            self.tile.append([])
            self.tile_color.append([])
            self.character_L.append([])
            for j in range(0, 5):
                self.tile[i].append(self.tile_images["White"])
                self.tile_color[i].append("White")
                self.character_L[i].append(0)
        
        self.TILE_GAP = 94
                
    def getTileColor(self, i, j):
        return self.tile_color[j][i]
    
    def getTile(self, i, j):
        return self.tile[j][i]
    
    def setTile(self, i, j, color):
        self.tile[i][j] = self.tile_images[color]
        self.tile_color[i][j] = color
        
    def getTileGap(self):
        return self.TILE_GAP
    
    def getCharL(self, i, j):
        return self.character_L[j][i]
    
    def setCharL(self, i, j, color):
        self.character_L[i][j] = color
        
    def removeCharL(self, i, j):
        self.character_L[j][i] = 0

class Stage:
    def __init__(self, stageNumber, stamina):
        pygame.init()
        self.table = Table()

        
        self.background = pygame.image.load("img/back/tree_1.png")
        self.base = pygame.image.load("img/tile/base.png")
        
        self.stamina_box = pygame.image.load("img/interface/stamina_box.png")
        
        self.attack_on = pygame.image.load("img/interface/attack_button.png")
        self.attack_click = pygame.image.load("img/interface/attack_button_click.png")
        self.spot = pygame.image.load("img/tile/spot.png")
        
        self.left = pygame.image.load("img/interface/left.png")
        self.left_click = pygame.image.load("img/interface/left_click.png")
        self.right = pygame.image.load("img/interface/right.png")
        self.right_click = pygame.image.load("img/interface/right_click.png")
        self.go = pygame.image.load("img/interface/go.png")
        self.go_click = pygame.image.load("img/interface/go_click.png")
        
        self.event = 0
        self.color = "Blue" # 현재 선택된 컬러
        self.colorSheet = {
            "Blue" : 0,
            "Red" : 1,
            "Yellow" : 2
        }
        
        self.character = [Blue(), Red(), Yellow()]
        self.rabbit = Rabbit()
        
        self.xy = [(720, 470), (489, 7)] # 캐릭터, uiBox 좌표값
        self.attack_arear = []
        
        # 색 변경하는 인덱스들
        self.button_blue = Button("", self.character[0].getIndex(), self.character[0].getIndexClick(), 823, 395, 120, 75, lambda: self.setColor("Blue"))
        self.button_red = Button("", self.character[1].getIndex(), self.character[1].getIndexClick(), 1062 , 395, 120, 75, lambda: self.setColor("Red"))
        self.button_yellow = Button("", self.character[2].getIndex(), self.character[2].getIndexClick(), 942, 395, 120, 75, lambda: self.setColor("Yellow"))
        
        
        # 공격, 이동
        self.button_attack = Button("attack", self.attack_on, self.attack_click, 755, 503, 410, 70, lambda: self.setEvent(1))
        self.button_move = Button("move", self.attack_on, self.attack_click, 755, 596, 410, 70, lambda: self.setEvent(2))
        
        self.attack_button_left = Button("", self.left, self.left_click, 775, 520, 73, 132, lambda: self.setPaint(self.paint-1))
        self.attack_button_right = Button("", self.right, self.right_click, 897, 520, 73, 132, lambda: self.setPaint(self.paint+1))
        self.attack_button_go = Button("", self.go, self.go_click, 1056, 520, 96, 132, lambda: self.painting())
        
        self.move_button_left = Button("", self.left, self.left_click, 775, 520, 73, 132, lambda: self.setTel(self.tel-1))
        self.move_button_right = Button("", self.right, self.right_click, 897, 520, 73, 132, lambda: self.setTel(self.tel+1))
        self.move_button_go = Button("", self.go, self.go_click, 1056, 520, 96, 132, lambda: self.moving())
        
        self.stageNumber = stageNumber # 몇 번째 스테이지 인지 확인
        self.stamina = stamina # 턴 수
        self.max_stamina = stamina # max 턴 수
        self.paint = 0 # 공격 지점
        self.tel = 0 # 이동 지점
        
    def show_stage(self, screen):
        
        screen.blit(self.background, (0,0))
        screen.blit(self.base, (85, 32))
    
        # 타일깔기
        for i in range(5):
            for j in range(5):
                screen.blit(self.table.getTile(i, j), (103+self.table.getTileGap()*i, 50 + self.table.getTileGap()*j)) # 첫번째 칸의 위치 + 두번째 칸과의 간격 * i
        
        # 애니메이션을 구현 할려 했던......
        # while self.animaCheck:
        #     screen.blit(self.anima[frame], (107 + 94 * self.location_x, 32 + 94 * self.location_y)) 
        #     frame = (frame + 1) % len(self.anima)  # 프레임 업데이트
        #     pygame.display.update()  # 화면 업데이트
        #     pygame.time.wait(150)  # 150ms 대기
        
        # 타일 위 캐릭터 그리기
        screen.blit(self.character[0].getAnima(), (107 +  self.table.getTileGap() * self.character[0].getLocationX(),
                                        32 + self.table.getTileGap() * self.character[0].getLocationY()))
        screen.blit(self.character[1].getAnima(), (107 + self.table.getTileGap() * self.character[1].getLocationX(), 
                                        32 + self.table.getTileGap() * self.character[1].getLocationY()))
        screen.blit(self.character[2].getAnima(), (107 + self.table.getTileGap() * self.character[2].getLocationX(), 
                                        32 + self.table.getTileGap() * self.character[2].getLocationY()))
        
        screen.blit(self.rabbit.getMainImg(),(107 + self.table.getTileGap() * self.rabbit.getLocationX(), 
                                        32 + self.table.getTileGap() * self.rabbit.getLocationY()))
        
        # 남은 스테미나 표시
        self.button_stamina_box = Button(str(self.stamina), self.stamina_box, self.stamina_box, 85, 564, 105, 105, None)
        self.button_stamina_box.draw(screen)
        
        # 선택된 컬러의 함수 저장용
        self.select_color = self.character[self.colorSheet[self.color]]
        
        screen.blit(self.select_color.getMainImg(), self.xy[1])
        screen.blit(self.select_color.getBox(), self.xy[0])
        
        # 현재 상태
        if self.rabbit.getColor() == "Black":
            screenChange = ScreenChange()
            screenChange.setScreen(0)
        if self.stamina <= 0:
            self.defense(screen)
        elif self.event == 0:
            self.default(screen) 
        elif self.event == 1:
            self.attack(screen)
        elif self.event == 2:
            self.move(screen)
            
    # event 0
    def default(self, screen):
         
        self.button_blue.draw(screen)
        self.button_red.draw(screen)
        self.button_yellow.draw(screen)
        
        self.button_attack.draw(screen)
        self.button_move.draw(screen)
        
    # 공격 가능한 범위 구하기
    def attackArea(self): 
        count = 0
        
        # 어디서부터 오류인진 모르나 일단 x y 가 뒤바뀐 관계로 뒤집어서,,..
        xy = [self.select_color.getLocationY(), self.select_color.getLocationX()]
        
        self.attackAreaX = []
        self.attackAreaY = []
        arrayArea = [[-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]]
        for i in range(8):
            for j in range(2):
                if xy[j] + arrayArea[j][i] < 0 or xy[j] + arrayArea[j][i] > 4 :
                    break
                count += 1
            if count == 2:
                self.attackAreaY.append(xy[0]+arrayArea[0][i])
                self.attackAreaX.append(xy[1]+arrayArea[1][i])
            count = 0
        
    # event 1
    def attack(self, screen):
        self.attackArea()

        # 공격 지점 이동
        if self.paint >= len(self.attackAreaX):
            self.setPaint(0)
        elif self.paint < 0:
            self.setPaint(len(self.attackAreaX)-1)
        screen.blit(self.spot,(self.table.getTileGap() * self.attackAreaX[self.paint] + 103, 
                               self.table.getTileGap() * self.attackAreaY[self.paint] + 50))
        
        self.attack_button_left.draw(screen)
        self.attack_button_right.draw(screen)
        self.attack_button_go.draw(screen)

    def setPaint(self, num):
        self.paint = num
        
    # 시간부족으로 if문 노가...다
    def painting(self):
        y = self.attackAreaX[self.paint]
        x = self.attackAreaY[self.paint]
        tile_color = self.table.getTileColor(y, x)
        
        if tile_color == "White":
            self.table.setTile(x, y, self.color)
        elif tile_color != self.color and tile_color != "Black":
            if (tile_color == "Yellow" and self.color == "Blue") or (tile_color == "Blue" and self.color == "Yellow"):
                self.table.setTile(x, y,"Green")
            elif (tile_color == "Yellow" and self.color == "Red") or (tile_color == "Red" and self.color == "Yellow"):
                self.table.setTile(x, y,"Orange")
            elif (tile_color == "Blue" and self.color == "Red") or (tile_color == "Red" and self.color == "Blue"):
                self.table.setTile(x, y,"Purple")
            else:
                self.table.setTile(x, y,"Black")
                
        if self.rabbit.getLocationX() == y and self.rabbit.getLocationY() == x:
            tile_color = self.rabbit.getColor()
            
            if tile_color == "White":
                self.rabbit.setColor(self.color)
            elif tile_color != self.color and tile_color != "Black":
                if (tile_color == "Yellow" and self.color == "Blue") or (tile_color == "Blue" and self.color == "Yellow"):
                    self.rabbit.setColor("Green")
                elif (tile_color == "Yellow" and self.color == "Red") or (tile_color == "Red" and self.color == "Yellow"):
                    self.rabbit.setColor("Orange")
                elif (tile_color == "Blue" and self.color == "Red") or (tile_color == "Red" and self.color == "Blue"):
                    self.rabbit.setColor("Purple")
                else:
                    self.rabbit.setColor("Black")
                
        self.stamina -= 1
        self.setEvent(0)
        
    def setColor(self, color):
        self.color = color 
        
    def getColor(self, color):
        return color
        
    def getEvent(self):
        return self.event
    
    def setEvent(self, number):
        self.event = number        
   
    # 이동 가능 구역 탐색
    def moveArea(self):
        
        self.moveX =[]
        self.moveY =[]

        for i in range(5):
            for j in range(5):
                if (self.table.getCharL(i, j) != 0) and (self.table.getCharL(i, j) != self.color):
                    continue
                elif (self.table.getTileColor(i, j) == "Black") or self.table.getTileColor(i, j) == "White":
                    continue
                elif self.table.getTileColor(i,j) != self.color:
                    if self.color == "Blue":
                        if (self.table.getTileColor(i, j) != "Green" and self.table.getTileColor(i, j) != "Purple"):
                            continue
                    elif self.color == "Yellow":
                        if (self.table.getTileColor(i, j) != "Green" and self.table.getTileColor(i, j) != "Orange"):
                            continue
                    elif self.color == "Red":
                        if (self.table.getTileColor(i, j) != "Purple" and self.table.getTileColor(i, j) != "Orange"):
                            continue

                self.moveX.append(i)
                self.moveY.append(j)
                
    # event 2
    def move(self, screen):
        self.move_button_left.draw(screen)
        self.move_button_right.draw(screen)
        self.move_button_go.draw(screen)
        
        self.moveArea()
        
        # 이동 지점 선택
        if self.tel >= len(self.moveX):
            self.setTel(0)
        elif self.tel < 0:
            self.setTel(len(self.moveX)-1)
        screen.blit(self.spot,(self.table.getTileGap() * self.moveX[self.tel] + 103
                               , self.table.getTileGap() * self.moveY[self.tel] + 50))
    
    def setTel(self, num):
        self.tel = num
    
    def moving(self):
        y = self.moveX[self.tel]
        x = self.moveY[self.tel]
        self.table.setCharL(x, y, self.color)
        self.table.removeCharL(x, y)
        self.select_color.setLocation(x, y)
        
        self.stamina -= 1
        self.setEvent(0)
    
    # event 3
    def defense(self, screen):
        pygame.event.wait(1000)
        
        self.event = 0
        self.stamina = self.max_stamina
        
class Stage_1(Stage):
    def __init__(self):
        super().__init__(1, 4)
        
        self.table.setTile(4, 2,"Blue")
        self.table.setCharL(4, 2,"Blue")
        self.character[0].setLocation(4, 2)
        
        self.table.setTile(2, 4, "Red")
        self.table.setCharL(2, 4,"Red")
        self.character[1].setLocation(2, 4)
        
        self.table.setTile(2, 0, "Yellow")
        self.table.setCharL(2, 0,"Yellow")
        self.character[2].setLocation(2, 0)
        
        self.table.setCharL(0, 2, "mop")
        self.rabbit.setLocation(0, 2)
    
    def show_stage(self, screen):
        super().show_stage(screen)
        
        