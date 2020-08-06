#[함수]
# 함수의 종류
# 1) 내장 함수(built-in) : len(), print(), append(), ...
# 2) 사용자 정의 함수

# 함수의 구조
# 1) def        : 키워드
# 2) test()     : 함수명
# 3) 들여쓰기   : 함수영역
# 4) return     : 함수가 끝났다(종료)

# 함수의 사용
#  함수명()

# 함수의 특징
# 1) 파일을 분할해서 원활하게 프로그래밍 할 수 있다.
# 2) 반복되는 코드를 함수를 통해 재활용 할 수 있다.

# [1]
def say_hello():
    print("안녕하세요")
    return
#---------------------------
say_hello()
say_hello()


# [2]
def say():
    return "hello"
#---------------------------
print(say())
result = say()
print(result)

# [3]
def tot(x, y):
    rs = x + y
    print("두 수의 합은 %d입니다." % rs)
#---------------------------
tot(10, 20)

# [4]
def tot(x, y):
    rs = x + y
    return rs
#---------------------------
a = 10
b = 20
c = tot(a, b)
print("두 수의 합은 %d입니다." % c)

#[전역변수 지역변수]

# 함수 안에서 선언된 변수는
# 함수 안에서만 사용할 수 있다.

# [1]

def test(a):
    a = a + 1
    
test(10)
# print(a)                         # 에러발생

#---------------------------------------------------

# [2-1]
x = 10

def change_num(x):
    x = 100

print("함수 호출 전 =", x)       # 10
change_num(x)
print("함수 호출 후 =", x)       # 10

#---------------------------------------------------

# [2-2]
x = 10

def change_num(x):
    x = 100
    return x

print("함수 호출 전 =", x)       # 10
x = change_num(x)
print("함수 호출 후 =", x)       # 100

# 함수 안에서의 또다른 함수의 호출

def tot(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def calc(x, y):
    print("%d + %d = %d" % (x, y, tot(x, y)))
    print("%d - %d = %d" % (x, y, sub(x, y)))
    print("%d * %d = %d" % (x, y, mul(x, y)))
    if y != 0:
        print("%d / %d = %.1f" % (x, y, div(x, y)))
    else:
        print("0으로 나눌 수 없습니다.")

# 호출
calc(10, 3)

#[클래스]
# 학생성적관리 프로그램 : 1단계(1차원 리스트)
hakbuns = ["1001", "1002", "1003"]
scores = [87, 11, 42]
 
# 학생성적관리 프로그램 : 2단계(2차원 리스트)
info = [
        ["1001", 87],
        ["1002", 11],
        ["1003", 42]   ]
 
# 학생성적관리 프로그램 : 3단계(클래스)
class Student:
    name = ""
    hakbun = 0
    score = 0
 
# 생성
hgd = Student()
hgd.name = "홍길동"
hgd.hakbun = "1001"
hgd.score = 87