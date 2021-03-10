# 일반 유닛
class Unit:
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self,location):
        print("[지상 유닛 이동")
        print("{0} : {1}방향으로 이동 합니다.[속도 {2}]"\
            .format(self.name, location, self.speed))
     
        
# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage 

    def attack(self, location):
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력 {2}"\
            .format(self.name, location, self.damage))
    
    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp == 0 :
            print("{0} : 파괴되었습니다.".format(self.name))

#드랍쉽 : 공중 유닛, 수송기. 마린/파이어벳/탱크등을 수송. 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아 갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):  # mothod overriding
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 아무것도 작성 하지 않아도 오류 없이 프로그램 진행

# 서플라이 디폿 : 건물, 1개 검ㄹ = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작 합니다.")

def game_over():
    pass

game_start()
game_over()
  