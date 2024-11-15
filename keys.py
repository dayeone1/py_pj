import pygame
from system import Button
from character import *
from system import *

class Game_system:
    def __init__(self):
        pygame.init()
        self.event = 0
        
        self.attack_on = pygame.image.load("img/interface/attack_button.png")
        self.attack_click = pygame.image.load("img/interface/attack_button_click.png")
        
        self.color = "Blue" # 현재 선택된 컬러
        self.colorSet = {
            "Blue" : 0,
            "Red" : 1,
            "Yellow" : 2
        }
        
        self.character = [Blue(), Red(), Yellow()]
        
        self.xy = [(720, 470), (489, 7)] # 캐릭터, uiBox 좌표값
        
        self.button_blue = Button("", self.character[0].getIndex(), self.character[0].getIndexClick(), 823, 395, 120, 75, lambda: self.setColor("Blue"))
        self.button_red = Button("", self.character[1].getIndex(), self.character[1].getIndexClick(), 1062 , 395, 120, 75, lambda: self.setColor("Red"))
        self.button_yellow = Button("", self.character[2].getIndex(), self.character[2].getIndexClick(), 942, 395, 120, 75, lambda: self.setColor("Yellow"))
      
    def show(self, screen):
        screen.blit(self.character[self.colorSet[self.color]].getMainImg(), self.xy[1])
        screen.blit(self.character[self.colorSet[self.color]].getBox(), self.xy[0])
        
        self.button_blue.draw(screen)
        self.button_red.draw(screen)
        self.button_yellow.draw(screen)
        
    def setColor(self, color):
        self.color = color 
        
    def getEvent(self):
        return self.event
    
    def setEvent(self, number):
        self.event = number
        
    def default(self):
        return None
    
    def attack(self):
        return None
    
    def move(self):
        return None