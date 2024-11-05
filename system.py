import pygame

# 버튼 크기 설정
button_width = 360
button_height = 60

# 색 선언
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Button:
    def __init__(self, text, img_in, img_act, x, y, action=None):
        self.text = text
        self.img_in = img_in  # 기본 이미지
        self.img_act = img_act  # 클릭된 이미지
        self.rect = pygame.Rect(x, y, button_width, button_height)
        self.action = action
        self.font = pygame.font.SysFont("font/h8514sys.fon", 30)

    def draw(self, surface):
        mouse = pygame.mouse.get_pos()  # 현재 마우스 위치 얻기
        click = pygame.mouse.get_pressed()  # 클릭 유무 얻기

        # 마우스 위치가 버튼 영역에 들어오면 클릭된 이미지 표시
        if self.rect.collidepoint(mouse):
            surface.blit(self.img_act, (self.rect.x, self.rect.y))  # 마우스가 버튼 위일 때 이미지 변경
            button_text = self.font.render(self.text, True, WHITE)
            if click[0] and self.action is not None:
                self.action()  # 클릭 시 액션 실행
        else:
            surface.blit(self.img_in, (self.rect.x, self.rect.y))  # 기본 이미지 표시
            button_text = self.font.render(self.text, True, BLACK)

        # 버튼 텍스트 그리기
        text_rect = button_text.get_rect(center=self.rect.center)
        surface.blit(button_text, text_rect)
