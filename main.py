import pygame
import sys
from story import show_story, Dialogue  # 스토리 화면과 대사 클래스를 불러옴
from menu import Menu, Button  # 메뉴 클래스를 불러옴

# Pygame 초기화
pygame.init()

# 창 크기 설정
WIDTH, HEIGHT = 1200, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('스토리')

# 버튼 크기 설정
button_width = 250
button_height = 70

# 색상 정의
WHITE = (255, 255, 255)

# 현재 화면 상태
current_screen = 0  # 0: 시작 화면, 1: 스토리 화면

# 버튼 인스턴스 생성 (시작 화면 버튼)
story_button = Button("스토리", (width - button_width) / 2, height / 2 - 100, button_width, button_height)
stage_button = Button("스테이지", (width - button_width) / 2, height / 2, button_width, button_height)
exit_button = Button("게임 종료", (width - button_width) / 2, height / 2 + 100, button_width, button_height)

# 메뉴 및 대사 인스턴스 생성
menu = Menu()
dialogue = Dialogue()

# 화면 변경 함수
def show_start_screen():
    screen.fill(WHITE)
    text = pygame.font.SysFont("malgungothic", 24).render("시작 화면입니다.", True, (0, 0, 0))
    screen.blit(text, (100, 100))

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # 시작 화면 버튼 클릭 확인
            if current_screen == 0:
                if story_button.is_clicked(mouse_pos):
                    current_screen = 1  # 스토리 화면으로 설정
                    dialogue.reset()  # 대사 초기화
                elif stage_button.is_clicked(mouse_pos):
                    print("스테이지 화면으로 이동")  # 스테이지 화면으로 이동하는 로직 추가
                elif exit_button.is_clicked(mouse_pos):
                    running = False  # 게임 종료

            # 스토리 화면에서는 메뉴 버튼 클릭 확인
            if current_screen == 1:
                if menu.handle_click(mouse_pos):
                    current_screen = 0  # 시작 화면으로 돌아가기
                    dialogue.reset()  # 대사 초기화

                # 대사 클릭 시 다음 대사로 넘어가기
                dialogue.next_dialogue()

    # 현재 화면 표시
    if current_screen == 0:
        show_start_screen()
        # 시작 화면 버튼 그리기
        story_button.draw(screen)
        stage_button.draw(screen)
        exit_button.draw(screen)
    elif current_screen == 1:
        show_story(screen, menu, dialogue)  # 스토리 화면 표시

    # 화면 업데이트
    pygame.display.flip()

# Pygame 종료
pygame.quit()
sys.exit()
