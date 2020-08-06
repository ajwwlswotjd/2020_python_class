# 369게임[1단계]
# 1. 1~50 사이의 랜덤 숫자를 저장한다.
# 2. 위 수에 369의 개수가
#   1) 2개이면, 짝짝을 출력
#   2) 1개이면, 짝을 출력
#   3) 0개이면, 해당 숫자를 출력
#   예)
# 		33	 : 짝짝
# 		16	 : 짝
# 		 7	 : 7

import random as rnd

num = str(rnd.randint(1,50))
cnt = 0
for i in num :
    if i in ("3" or "6" or "9") :
        cnt = cnt + 1    
        
if cnt != 0 :
    print(cnt*"짝")
else : 
    print(num)
    