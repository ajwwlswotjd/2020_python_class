# Up & Down 게임[2단계]
# 1. 정답을 맞추면 게임은 종료된다.
# 2. 100점부터 시작해 오답을 입력할 때마다 5점씩 차감된다.
# 3. 게임 종료 후, 점수를 출력한다.
import random
score = 100
num = random.randint(1,100)
print(num)
while True :
    answer = int(input("숫자 입력 (1 ~ 100) : "))
    if num == answer : 
        break
    elif num < answer :
        print("DOWN")
    else : 
        print("UP")
    score = score - 5
print("점수 : %d" % score)