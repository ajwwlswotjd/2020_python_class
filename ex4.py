# 제어문(control statement)
# 1) 조건문 : if
# 2) 반복문 : while, for
# 3) 보조 제어문 : break, continue

# 들여쓰기(indentation)에 주의!
# 조건문 if의 구조
'''
    if 조건식:
        조건식이 참(True)일 때, 실행할 문장
'''

if True:
    print("실행 O")

if False:
    print("실행 X")

# 예) 홀짝
num = 8
print(num % 2 == 0)
print(num % 2 == 1)

if num % 2 == 0:
    print("짝수")
if num % 2 == 1:
    print("홀수")

# 문제 1) 양수, 0, 음수 출력
num = -18
if num < 0 :
    print("음수")
elif num > 0 :
    print("양수")    
else :
    print("0")

# 문제 2) 4의 배수 출력
num = 12
if num % 4 == 0 :
    print("4의 배수 입니다")
else : 
    print("4의 배수가 아닙니당")    

# 문제 3) 합격, 불합격 출력
score = 87
# 합격이 80점 이상이라고 가정
if score >= 80 :
    print("합격")
else :
    print("불합격")
