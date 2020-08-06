# 가운데 숫자 맞추기 게임
# 1. 150~250 사이의 랜덤 숫자 저장
# 2. 랜덤 숫자의 가운데 숫자를 맞추는 게임이다.
# 예)
# 		249		: 4

import random as rnd

num = str(rnd.randint(150,250))[1]
while True :
    if input("가운데 숫자 맞추기 : ") == num :
        break