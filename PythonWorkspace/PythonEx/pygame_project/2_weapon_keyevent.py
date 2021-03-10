import os
import pygame
################################################################
# 기본 초기화반드시 해야 하는 것들

pygame.init()#초기화(반드시 필요)

#화면 크기 설정
screen_width = 640 #가로
screen_height = 480 #세로
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 설정
pygame.display.set_caption("Nado Pang") #게임 이름

#FPS
clock = pygame.time.Clock()
########################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환

# 배경이미지 불러오기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지 높이 위에 캐릭터를 두기 위해 사용

#캐릭터(스프라이트) 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height - stage_height

# 캐릭터 이동 반향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기는 한번에 여러발 발사 가능
weapons =[]

# 무기 속도
weapon_speed = 10

#적 enemy 캐릭터


#이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정

    
# 2.이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():#이벤트가 발생 하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running == False # 게임 진행중이 아님
            os.sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -=character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # 무기 발사
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0


# 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    # 예를 들어 발사 위치가 100,200 일 때 y값은 계속 줄어들며 변함
    #  -> 180,160,120....
    # 이변 환 값들을 리스트로 묶어 처리

    weapons = [[w[0],w[1] - weapon_speed] for w in weapons] #무기 위치를 위로 올림

    # 천정에 닿은 무기 없애기
    weapons = [[w[0],w[1]] for  w in weapons if w[1] > 0]# 천정에 닿지 않은 무기만 배열에 저장

# 4. 충돌 처리



# 5. 화면에 그리기
    screen.blit(background,(0,0)) #배경 그리기
    for weapon_x_pos, weapon_y_pos in weapons: # 발사된 무기 그려주기
        screen.blit(weapon, (weapon_x_pos,weapon_y_pos))
    screen.blit(stage,(0, screen_height-stage_height)) # 스테이지 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    
    
    pygame.display.update()

# pygame 종료
pygame.quit()

