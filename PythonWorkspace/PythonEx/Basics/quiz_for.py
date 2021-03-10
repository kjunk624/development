from random import *

'''customers = list(range(1,51))
while (i <= 50):
    drive_time = [{i:randint(5,51)} for i in customers]
    if print("[o] {}째 손님 (소요시간 : 15분)")'''

cnt = 0 # 총 탑승 승객 수
for i in range(1,51): # 1~50이라는 수(승객)
    time = randrange(5,51) # 5~50분 소요시간
    if 5<= time <=15: # 5~15분 이내의 손님(매칭 성공), 탐승 승객 증가 처리
        print("[o] {0}째 손님 (소요시간 : {1}분)".format(i,time))
        cnt +=1
    else : # 매칭 실패한 경우
        print("[ ] {0}째 손님 (소요시간 : {1}분)".format(i,time))

print("총 탑승 승객 : {0}분".format(cnt))


