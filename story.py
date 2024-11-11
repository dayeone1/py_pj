import pygame, pymysql
from system import Button, ScreenChange

class Dialogue:
    
    def __init__(self):
        
        self.text_bar = pygame.image.load("img/interface/text_bar.png")
        self.name_bar = pygame.image.load("img/interface/name_bar.png")
        self.background = pygame.image.load("img/back/tree_1.png")
        self.next_botton = pygame.image.load("img/interface/next_botton.png")

        self.dialogues = []  # 대사 리스트 초기화
        self.names = []  # 이름 리스트 초기화
        self.load_dialogues()  # 대사/이름 로드

        self.current_index = 0  # 현재 대사 인덱스
        self.next = Button("", self.next_botton, self.next_botton, 1090, 600, 40, 40, self.next_dialogue) # 대사 전환 버튼
        
        
    def load_dialogues(self):
        # MySQL 데이터베이스에 연결
        db = pymysql.connect(
            host="localhost",
            user="root",
            password="1234",
            database="game_dialogue"
        )
        
        cursor = db.cursor()
        cursor.execute("SELECT character_name, dialogue FROM dialogues")
        result = cursor.fetchall()
        
        # 대사와 이름 리스트에 추가
        for row in result:
            self.names.append(row[0])      # 이름 추가
            self.dialogues.append(row[1])  # 대사 추가
        
        cursor.close()
        db.close()

    def next_dialogue(self):
        if self.current_index < len(self.dialogues) - 1:  # 마지막 대사 다음으로 넘어가지 않도록 수정
            self.current_index += 1
            pygame.event.wait(300) # 대사 전환 후 0.3초 대기
        else:
            self.current_index = 0 # 대사 초기화
            self.screenChange = ScreenChange()
            self.screenChange.setScreen(0)
            

    # 대사, 이름 가져옴
    def get_current_dialogue(self):
        if self.current_index < len(self.dialogues):
            return self.dialogues[self.current_index]
        return "대사 끝"

    def get_current_name(self):
        if self.current_index < len(self.names):
            return self.names[self.current_index]
        return "이름 출력 끝"

    def show_story(self, screen):
        screen.fill((0, 0, 0))  # 배경 표시
        screen.blit(self.text_bar, (50, 460))
        
        # 대사 표시 위치 조정 (하단)
        font = pygame.font.SysFont("malgungothic", 24)
        text = font.render(self.get_current_dialogue(), True, (0, 0, 0))  # 대사 텍스트 색상 검정으로 변경
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() - 150))  # 하단 중앙
        screen.blit(text, text_rect)  # 대사 표시
        
        screen.blit(self.name_bar, (917, 423))  # 이름창 표시
        self.next.draw(screen)
        
        # 이름 표시
        name_text = font.render(self.get_current_name(), True, (0, 0, 0))  # 이름 텍스트 색상 검정으로 변경
        name_rect = name_text.get_rect(x = 980, y = 435)  # 이름 표시 위치 조정
        screen.blit(name_text, name_rect)  # 이름 표시
        
        
