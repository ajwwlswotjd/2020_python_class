# 369게임[2단계]
# 1. 1~50까지 반복을 한다.
# 2. 그 안에서 해당 숫자의 369게임의 결과를 출력한다.
# 예) 1 2 짝 4 5 짝 7 8 짝 10 11 12 짝 ...

for i in range(1,51) :
    string = str(i)
    if "3" in string or "6" in string or "9" in string :
        print("짝", end=" ")
    else : 
        print(string, end=" ")