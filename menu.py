import pygame

class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.SysFont("malgungothic", 24)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

class Menu:
    def __init__(self):
        self.button = Button("메뉴", 1450, 50, 90, 50)
        self.start_menu_button = Button("시작화면", 1250, 100, 250, 70)
        self.open = False

    def draw(self, screen):
        self.button.draw(screen)
        if self.open:
            self.start_menu_button.draw(screen)

    def handle_click(self, mouse_pos):
        if self.button.is_clicked(mouse_pos):
            self.open = not self.open  # 메뉴 열기/닫기

        if self.open and self.start_menu_button.is_clicked(mouse_pos):
            self.open = False  # 메뉴 닫기
            return True  # 시작 화면으로 돌아가기
        return False  # 시작 화면으로 돌아가지 않음
