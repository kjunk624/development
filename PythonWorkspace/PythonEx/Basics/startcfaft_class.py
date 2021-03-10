class Unit:
    def __init__(self,name,hp,damage):
        super().__init__()
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 =  Unit("마린", 40, 5)
marine2 =  Unit("마린", 40, 5)
tank =  Unit("탱크", 150, 35)

# 레이스 : 공중 유닛,비행기,클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

#마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것(빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith1.clocking == True: #확장된 메소드는 확장한 객체에만 적용되고 다른 객체에게는 적용되진 않는다.
    print("{0}은 현재 클로킹 상태입니다.".format(wraith2.name))

