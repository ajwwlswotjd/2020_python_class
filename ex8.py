
# 구구단 게임[2단계]
# 1. 구구단 문제를 출제하기 위해, 숫자 2개를 랜덤하게 저장한다.
# 2. 저장된 숫자를 토대로 구구단 문제를 출력한다.
# 예)	3 x 7 = ?
# 3. 문제에 해당하는 정답을 입력받는다.
# 4. 정답을 비교 "정답" 또는 "땡"을 출력한다.

import random as rnd
num1 = rnd.randint(1,9)
num2 = rnd.randint(1,9)

if int(input("%d x %d = ? : " % (num1,num2))) == num1 * num2 :
    print("정답")
else : 
    print("땡")