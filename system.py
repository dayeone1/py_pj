import pygame

# 색 선언
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Button:
    def __init__(self, text, img_in, img_act,x , y, button_width, button_height, action=None):
        self.text = text
        self.img_in = img_in  # 기본 이미지
        self.img_act = img_act  # 클릭된 이미지
        self.rect = pygame.Rect(x, y, button_width, button_height)
        self.action = action
        self.font = pygame.font.SysFont("font/h8514sys.fon", 30)
        self.sound = pygame.mixer.Sound("img/rock.wav")

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()  # 현재 마우스 위치 얻기
        click = pygame.mouse.get_pressed()  # 클릭 유무 얻기

        # 마우스 위치가 버튼 영역에 들어오면 클릭된 표시
        if self.rect.collidepoint(mouse):
            screen.blit(self.img_act, (self.rect.x, self.rect.y))  # 마우스가 버튼 위일 때 이미지 변경
            button_text = self.font.render(self.text, True, WHITE)
            if click[0] and self.action is not None:
                self.action()  # 클릭 시 함수 실행
                self.sound.play() # 효과음
                pygame.time.delay(100)
        else:
            screen.blit(self.img_in, (self.rect.x, self.rect.y))  # 기본 이미지 표시
            button_text = self.font.render(self.text, True, BLACK)

        # 버튼 텍스트 그리기
        text_rect = button_text.get_rect(center=self.rect.center)
        screen.blit(button_text, text_rect)
    
    
# 현재 화면 상태 확인
class ScreenChange:
    
    currentScreen = 0  # 0: 시작 화면, 1: 스토리 화면, 2: 스테이지 화면, 3 + n: 본 게임 화면
        
    def getScreen(self):
        return ScreenChange.currentScreen
    
    def setScreen(self, changeNumber):
        ScreenChange.currentScreen = changeNumber
        print(ScreenChange.currentScreen)
        
class Music:
    pygame.init()
    bgm = pygame.mixer.Sound("img/bgm.wav")
    def music_play(self):
        Music.bgm.play(-1)
    
    def music_stop(self):
        Music.bgm.stop()

    