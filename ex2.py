# 변수(variable)
# 1. 변수는 단, 한개의 값을 저장할 수 있다.
# 2. 변수명은 숫자로 시작할 수 없다.
# 3. 특수문자 _을 허용한다.
# 4. 알파벳의 대소문자를 구분한다.
# 5. 예약어(keyword)는 변수명으로 사용할 수 없다.
#    ex) def, int, class, ...

num = 17
num = 8
print(num)

_1top = 100

a = 7
A = 3
print(a)
print(A)

# 예) 현금이 1000원있다. 200원짜리 과자 구입 후, 잔돈 출력 
현금 = 1000
과자 = 200
잔돈 = 현금 - 과자
print(잔돈)

# 문제 1) 월급이 100원이다. 연봉은? (조건 : 세금 10% 제외)
salary = 100
print( salary * 12 * 0.9 )

# 문제 2) 시험점수를 30, 50, 4점 을 받았다. 평균은?

arr = [30,50,4]
print( sum(arr) / len(arr) )

# 문제 3) 가로가 3이고 세로가 6인 삼각형 넓이 출력

print( 3 * 6 / 2 )

# 문제 4) 100초를 1분 40초로 출력
sec = 100
print( "%d분 %d초" % ( sec/60 , sec%60 ) )

# 문제 5) 800원에서 500원짜리 개수 ,100원짜리 개수
# 정답 5) 500원(1개), 100원(3개)  

money = 800

print( "500원(%d개) 100원(%d개)" % ( money/500 , money%500/100 ) )