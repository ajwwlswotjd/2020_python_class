import random

 
comleft = random.randint(0,2)
comright = random.randint(0,2)


meleft = int(input("meleft ==> 0) 가위 , 1) 바위 , 2) 보 : "))
meright = int(input("meright ==> 0) 가위 , 1) 바위 , 2) 보 : "))

# 문제가 뭔지 모른다.

# 나의 승률 계산이라고 가정

com = [comleft,comright][random.randint(0,1)]
me = [meleft,meright][random.randint(0,1)]

if com == me : 
    print("무승부")
elif (com < me and not (com == 0 and me == 2)) or com == 2 and me == 0 :
    print("승리")
else :
    print("패배")    