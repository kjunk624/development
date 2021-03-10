import pygame


pygame.init()#초기화(반드시 필요)

#화면 크기 설정
screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 설정
pygame.display.set_caption("My Game") #게임 이름

#FPS
clock = pygame.time.Clock()

#배경이미지 불러오기
background = pygame.image.load("D:/Python/PyExcise/pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:/Python/PyExcise/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width/2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로의 크기가장 아래에 해당하는 곳에 위치

#이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

#이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정

    # print("fps : " + str(clock.get_fps()))
    # 캐릭터가 1초 동안에 100만큼 이동해야함
    # 10fps : 1초동안에 10번 동작 -> 1번에 10만큼 이동 : 10 * 10 =100
    # 20fps : 1초동안에 20번 동작 -> 1번에 5만큼 이동 ! : 20 * 5 = 100
    # 그러므로 프레임과 관계 없이 움직일 수 있도록 변화량을 변수로 바꿈(character_speed)

    for event in pygame.event.get():#이벤트가 발생 하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running == False # 게임 진행중이 아님
            sys.exit()

        if event.type == pygame.KEYDOWN: # 키가 눌려졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed # to_x = to_x - character_speed 
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로 
                to_x += character_speed  
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0 # 변화량이 0이므로 그자리에 멈춤
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0


    character_x_pos += to_x * dt # 키를 눌러서 변한 좌표만큼 변화를 기록
    character_y_pos += to_y * dt # dt로 프레임과 상관 없이 이돌 속도는 비슷하도록 보정

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width 

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height 


    screen.blit(background, (0,0)) #배경 그리기

    screen.blit(character,(character_x_pos, character_y_pos)) # 캐릭터 그리기
    
    pygame.display.update()#화면 다시 그리기

# pygame 종료
pygame.quit()
