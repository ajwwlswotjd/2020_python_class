# 랜덤

# random.py 파일의 내용을 사용하겠다.
import random

r_num = random.randint(0, 2)    # 0, 1, 2 중에서 랜덤 숫자
print(r_num)



# 홀짝 게임
# 1. 1~100사이의 랜덤 숫자를 저장한다.
# 2. 저장된 랜덤 숫자를 보여주고,
# 3. 해당 숫자가 홀수인지 짝수인지 맞추는 게임이다.

import random as rnd
num = rnd.randint(1,100)
print(num)
print("1.홀수")
print("2.짝수")
choice = int(input("번호를 선택하세요 : "))
if ( num % 2 == 0 and choice == 2 ) or ( num % 2 == 1 and choice == 1 ) :
    print("정답")
else :
    print("떙")    
