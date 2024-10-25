import pygame
from menu import Menu  # 메뉴 클래스를 불러옴

class Dialogue:
    def __init__(self):
        self.dialogues = [
            "안녕하세요! 이것은 스토리의 시작입니다.",
            "이곳은 환상적인 세계입니다.",
            "모험이 시작됩니다! 준비가 되었나요?",
            "이제 새로운 친구를 만나러 갑니다.",
            "모험은 언제나 기대를 안겨줍니다!"
        ]
        self.current_index = 0  # 현재 대사 인덱스

    def next_dialogue(self):
        if self.current_index < len(self.dialogues):
            self.current_index += 1

    def reset(self):
        self.current_index = 0

    def get_current_dialogue(self):
        if self.current_index < len(self.dialogues):
            return self.dialogues[self.current_index]
        return "대사가 끝났습니다."

def show_story(screen, menu, dialogue):
    screen.fill((0, 255, 0))  # 초록색 배경

    # 대사 표시 위치 조정 (하단)
    font = pygame.font.SysFont("malgungothic", 24)
    text = font.render(dialogue.get_current_dialogue(), True, (0, 0, 0))
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 100))  # 하단 중앙
    screen.blit(text, text_rect)

    menu.draw(screen)  # 메뉴 그리기
