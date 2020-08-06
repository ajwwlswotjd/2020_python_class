# 2. 대입 연산자 : =
# 변수는 오직 대입 연산자를 통해서만이
# 값의 변경이 가능하다.

num = 10
print(num + 1)     # 11
print(num)         # 10

num = num + 1
print(num)         # 11

# 4. 논리 연산자
# 1) and : 양쪽 모두 참이어야, 참
# 2) or : 어느 한쪽이라도 참이면, 참

print(10 == 10 and 3 == 3)
print(10 != 10 and 3 == 3)
print(10 == 10 and 3 != 3)
print(10 != 10 and 3 != 3)

print()

print(10 == 10 or 3 == 3)
print(10 != 10 or 3 == 3)
print(10 == 10 or 3 != 3)
print(10 != 10 or 3 != 3)

# 입력받기

print("당신의 나이를 입력하세요.")
age = input()
print(age)

# type() 함수 : 데이터의 종류 확인
print(type(age))    # <class 'str'>

# int() 함수 : 문자 -> 숫자
age = int(age)
print(type(age))    # <class 'int'>


# 방법 1)
print("당신의 나이를 입력하세요.")
age = input()
age = int(age)

# 방법 2)
age = input("당신의 나이를 입력하세요 : ")
age = int(age)

# 방법 3)
age = int(input("당신의 나이를 입력하세요 : "))
print(age)
