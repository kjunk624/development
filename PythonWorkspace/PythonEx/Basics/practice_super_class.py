class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

class FlyableUnit(Flyable, Unit): # 마지막에 호출된 생성자만 실행됨
    def __init__(self):
        super().__init__()

class FlyableUnit(Flyable, Unit): # 다중 상속일 경우에는 명시적으로 두 생상자를 모두 호출 해준ㄴ 것이 좋다
    def __init__(self):
        #super().__init__()
        Flyable.__init__(self)
        Unit.__init__(self)


# 드랍십
dropship = FlyableUnit()