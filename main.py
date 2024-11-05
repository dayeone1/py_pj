import pygame
import sys
import time
from system import Button  # system.py에서 Button 클래스를 불러옴

# 사용할 이미지 초기화
background = pygame.image.load("img/back/tree.png")
start_button_on = pygame.image.load("img/interface/start_botton.png")
start_button_act = pygame.image.load("img/interface/start_botton_click.png")

# Pygame 초기화
pygame.init()

# 창 크기 설정
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TriColor_King')

# 현재 화면 상태
current_screen = 0  # 0: 시작 화면, 1: 스토리 화면, 2: 스테이지 화면, 3: 본게임 화면

# 버튼 인스턴스 생성 (시작 화면 버튼)
stage_button = Button("STAGE", start_button_on, start_button_act, 420, 395, lambda: print("STAGE 버튼 클릭됨"))
story_button = Button("STORY", start_button_on, start_button_act, 420, 485, lambda: print("STORY 버튼 클릭됨"))
exit_button = Button("EXIT", start_button_on, start_button_act, 420, 575, pygame.quit)

clock = pygame.time.Clock()

# 메인 루프
start = True
while start:
    # 30fps
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False

    # 현재 화면 표시
    if current_screen == 0:
        # 배경 그리기
        screen.blit(background, (0, 0))  # 배경을 화면에 그립니다.
        
        # 버튼 그리기
        stage_button.draw(screen)
        story_button.draw(screen)
        exit_button.draw(screen)

    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
