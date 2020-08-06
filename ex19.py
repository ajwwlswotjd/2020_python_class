# 랜덤학생
# 1. 10회 반복을 한다.
# 2. 1~100 사이의 랜덤 숫자를 저장한다.(학생의 성적)
# 3. 성적이 60점 이상이면 합격생이다.
# ---------------------------------------
# . 전교생(10명)의 총점과 평균을 출력한다.
# . 합격자 수를 출력한다.
# . 1등 학생의 번호와 성적을 출력한다.
import random
arr = []
for i in range(0, 10) :
    arr.append(random.randint(1, 100))

total = sum(arr)
avg = total / len(arr)
cnt = len(list(filter(lambda x: x >= 60,arr)))
idx = arr.index(max(arr))
print(arr)
print("총점 : %d점, 평균 : %.1f점" % (total,avg))
print("합격자 수 : %d명" % cnt)
print("1등 학생 : %d번, 성적 : %d점" % (idx+1,arr[idx]))
