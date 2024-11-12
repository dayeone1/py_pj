import pygame, sys
from pygame.locals import QUIT,MOUSEBUTTONDOWN # 창 닫기에 사용
from story import Dialogue
from system import Button, ScreenChange
from stages import StageCheck
from stage import *

# Pygame 초기화
pygame.init()
clock = pygame.time.Clock()
dialogue = Dialogue()
screenChange = ScreenChange()
stageCheck = StageCheck()
stage1 = Stage_1()


# 사용할 이미지 초기화
background = pygame.image.load("img/back/tree.png")
start_button_on = pygame.image.load("img/interface/start_button.png")
start_button_act = pygame.image.load("img/interface/start_button_click.png")

bgm = pygame.mixer.Sound("img/bgm.wav")

# 창 크기 설정
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TriColor_King')

# 버튼 생성
button_width = 360
button_height = 60

stage_button = Button("STAGE", start_button_on, start_button_act, 420, 395, button_width, button_height, lambda: screenChange.setScreen(2))
story_button = Button("STORY", start_button_on, start_button_act, 420, 485, button_width, button_height, lambda: screenChange.setScreen(1))
exit_button = Button("EXIT", start_button_on, start_button_act, 420, 575, button_width, button_height, pygame.quit)

# 메인 루프
start = True
bgm.play(-1)
while start:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

    # 현재 화면 표시
    if screenChange.getScreen() == 0:
        screen.blit(background, (0, 0))  # 배경 표시
        
        # 버튼 그리기
        stage_button.draw(screen)
        story_button.draw(screen)
        exit_button.draw(screen)
        
    elif screenChange.getScreen() == 1:
        dialogue.show_story(screen)  # 대사 표시
        
    elif screenChange.getScreen() == 2:
        stageCheck.show_stages(screen)
        
    elif screenChange.getScreen() == 3:
        stage1.show_stage(screen)
        
        
    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
