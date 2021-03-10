'''
Quiz)하늘에서 떨어지는 똥 피하기 게임을 만드시오

[게임의 조건]
1. 캐릭터는 화면 가장아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐. x좌표는 매번 랜덤으로 설정
3. 캐릭터가 떵을 피하면 다음 떵이 다시 떨어짐
캐릭터가 똥과 충돌하면 게임 종료
FPS는 30으로 고정

[게임 이미지]
1. 배경 : 640 * 480 (세로/가로) -background.png
2. 캐릭터 : 70 * 70 - character.png
3. 똥 : 70*70 - enemy.png

'''
import sys
import pygame
import random
################################################################
# 기본 초기화반드시 해야 하는 것들

pygame.init()#초기화(반드시 필요)

#화면 크기 설정
screen_width = 480
screen_height = 640 
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 설정
pygame.display.set_caption("똥피하기") #게임 이름

#FPS
clock = pygame.time.Clock()
########################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

#배경이미지 불러오기
background = pygame.image.load("D:/Python/PyExcise/pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기

character = pygame.image.load("D:/Python/PyExcise/pygame_basic/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height


#이동할 좌표
to_x = 0
character_speed = 0.6

# 똥(enemy)
enemy = pygame.image.load("D:/Python/PyExcise/pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width)
enemy_y_pos = 0

#폰트 정의
 
game_font = pygame.font.Font(None, 40)# 폰트 객체 생성(폰트, 크기)

#총 시간
total_time = 30

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()# 시작 tick을 받아옴

#이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정

# 2.이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running == False 
            sys.exit()

        # 좌우로 만 이동
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
         
        if event.type == pygame.KEYUP:
            if  event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                to_x = 0

        
# 3. 게임 캐릭터 위치 정의

    character_x_pos += to_x * dt
    enemy_y_pos += 5

    # 가로 경계값 처리
    if character_x_pos <0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if enemy_y_pos > screen_height: ### 적이 밑으로 떨어지면 다시 위에서 떨어진다.
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    


# 4. 충돌 처리

    # 충돌 처리를 위한 rect정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos  # 움직인 캐릭터 위치를 확인
    character_rect.top = character_y_pos    

    enemy_rect = enemy.get_rect()  # 적의 위치
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False


# 5. 화면에 그리기
    screen.blit(background, (0,0)) #배경 그리기
    screen.blit(character,(character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) # 적 그리기

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks)/1000 # 현재 tick을 받아옴 
                                    # 경과 시간(ms)을 1000으로 나누어 초(s)단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)),True,(255,255,255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10,10))

    #막약 시간이 0 이하면 게임 종료
    if total_time-elapsed_time <= 0 :
        print("타임 아웃")
        running = False
    
    pygame.display.update() # 화면 다시 그리기

# 종료 직전 잠시 대기 (2초)
pygame.time.delay(1000)
# pygame 종료
pygame.quit()
