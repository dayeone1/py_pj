import pygame

# 색상 정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = BLUE
        self.font = pygame.font.SysFont("malgungothic", 18)

    def draw(self, screen):
        # 버튼 그리기
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
