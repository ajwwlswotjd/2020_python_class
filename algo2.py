# 숫자이동[2단계]
# 1. 숫자2는 캐릭터이다.
# 2. 숫자1을 입력하면, 캐릭터가 왼쪽으로
# 	 숫자2를 입력하면, 캐릭터가 오른쪽으로 이동한다.
# 3. 단, 좌우 끝에 도달했을 때, 예외처리를 해야한다.
# 4. 숫자 1은 벽이다. 벽을 만나면 이동할 수 없다.
# 5. 단, 숫자3을 입력하면, 벽을 격파할 수 있다.

game = [0, 0, 1, 0, 2, 0, 0, 1, 0]
idx = game.index(2)
while True :
    break
    print(game)
    print("==== 숫자 이동 ====")
    print("1. 캐릭터 왼쪽 이동")
    print("2. 캐릭터 오른쪽 이동")
    print("3. 벽 격파")
    choose = int(input("번호 입력 : "))
    if choose == 1 :
        idxTemp = idx - 1
        if idxTemp <= -1 :
            idxTemp = len(game)-1
        
        if game[idxTemp] == 1 :
            print("벽이 있습니다.")
            continue
        else :
            game[idx] = 0
            idx = idxTemp
            game[idx] = 2
    elif choose == 2 :
        idxTemp = idx + 1
        if idxTemp >= len(game) :
            idxTemp = 0
        
        if game[idxTemp] == 1 :
            print("벽이 있습니다.")
            continue
        else :
            game[idx] = 0
            idx = idxTemp
            game[idx] = 2
    elif choose == 3 :
        if idx <= 0 :
            game[idx+1] = 0
        elif idx >= len(game)-1 :
            game[idx-1] = 0
        else : 
            game[idx-1] = 0
            game[idx+1] = 0
        print("벽을 부쉈습니다.")
    else :
        print("잘못된 입력 입니다.")

#===============================

# 중복숫자 금지[2단계]
# 1. arr배열에 1~10 사이의 랜덤 숫자 5개를 저장한다.
# 2. 단 중복되는 숫자가 없어야 한다.
import random
nums = [0 for i in range(5)]
tenArr = list(range(1,11))
random.shuffle(tenArr)
nums = tenArr[0:5]
#for i in nums :
    #print(i)
    

#=================================

# 숫자 야구 게임
# 1. me에 1~9 사이의 숫자 3개를 저장
#    (단, 중복되는 숫자는 저장 불가)
# 2. com과 me를 비교해 정답을 맞출 때까지 반복
# 3. 숫자와 자리가 같으면 		strike += 1
#    숫자만 같고 자리가 틀리면 	ball += 1
# 예)
# 정답 : 1 7 3
# 3 1 5		: 2b
# 1 5 6		: 1s
# ...

arr = list(range(1,10))
random.shuffle(arr)
arr = arr[0:3]
strike = 0
ball = 0
print(arr)
user = list(map(int,input("숫자 입력 (예 : 1 2 3) : ").split()))

for i in range(len(user)) :
    try:
        idx = arr.index(user[i])
        if idx == i :
            strike = strike + 1
        else : 
            ball = ball + 1
        pass
    except :
        pass

print("%d볼 %d스트라이크" % (ball,strike))