# 최대값 구하기[1단계]
# 1. 숫자 3개를 입력받는다.
# 2. 입력받은 3개의 수를 비교하여,
# 3. 가장 큰 수(MAX)를 출력한다.

arr = []

for i in range(0,3) :
    arr.append(int(input("숫자 입력 : ")))
print(max(arr))