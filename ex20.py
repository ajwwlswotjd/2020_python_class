# 카카오 택시
# 1. 손님을 태워 목적지까지 이동하는 게임이다.
# 2. -10~10 사이의 랜덤 숫자 2개를 저장해 목적지로 설정한다.
# 3. 메뉴는 아래와 같다.
# 		1) 속도설정 : 1~3까지만 가능
# 		2) 방향설정 : 동(1)서(2)남(3)북(4)
# 		3) 이동하기 : 설정된 방향으로 설정된 속도만큼 이동
# 4. 거리 2칸 당 50원씩 추가되어 요금도 출력한다.
# 예) 1(50) 2(50) 3(100) 4(100) ...

# 목적지(destination)

import random as rnd
import math

des_x = 0
des_y = 0

des_x = rnd.randint(-10,10)
des_y = rnd.randint(-10,10)

# 현재 위치
x = 0
y = 0

# 방향(direction)
direc = 0

# 속도
speed = 0

# 요금
fee = 0

run = True
while run:
    print("=== 카카오 택시 ===")
    print("목적지 :", des_x, des_y)
    print("현위치 :", x, y)
    print("방  향 :", direc)
    print("속  도 :", speed)

    print("1.방향설정")
    print("2.속도설정")
    print("3.이동하기")

    choice = int(input("메뉴 선택 : "))
    if choice == 1: # 방향 설정
        print("1. 동쪽 방향")
        print("2. 서쪽 방향")
        print("3. 남쪽 방향")
        print("4. 북쪽 방향")
        direcTemp = int(input("방향 입력 : "))
        if direcTemp in range(1,5) : 
            direc = direcTemp
        else : 
            print("잘못된 값을 입력하였습니다.")
        pass
    elif choice == 2: # 속도 설정
        speedTemp = int(input("속도 입력 (1~3) : "))
        if speedTemp in range(1,4) :
            speed = speedTemp
        else : 
            print("잘못된 값을 입력하였습니다.")
        pass
    elif choice == 3: # 이동하기
        fee = fee + speed
        if direc == 1 : # 동쪽으로 이동
            x = x + speed
        elif direc == 2 : # 서쪽으로 이동
            x = x - speed
        elif direc == 3 : # 남쪽으로 이동
            y = y - speed
        elif direc == 4 : # 남쪽으로 이동
            y = y + speed
        else :
            print("오류 발생")
    
        if des_x == x and des_y == y :
            break
        pass

money = math.ceil(fee/2)*2*50
print("요금 : %d원" % money)