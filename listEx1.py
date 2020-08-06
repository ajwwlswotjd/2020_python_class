#[리스트 기본이론]
# 리스트
# - 변수들의 집합
# 1) 선언
#    a = [ ]        # 빈 리스트의 주소를 a가 저장하고 있다.
#    a = [10, 20, 30, 40]

# 2) 사용
#    리스트 변수들은 0번부터 1씩 증가하면서 번호가 생성된다.(index)
#    a[0]  => 10
#    a[1]  => 20
#    a[2]  => 30
#    a[3]  => 40
  
# 3) 특징
#    . 크기의 제한이 없다.
#    . 여러 종류의 값을 저장할 수 있다.
#    . 0부터 시작되는 방번호(index)가 순차적으로 생성된다.


#[디셔너리 기본이론]
# 딕셔너리
# 1. 인덱스를 내가 직접 설정할 수 있다.
# 2. 중괄호{}로 표현한다.
# 3. 콜론(:)을 중심으로 {인덱스 : 값}

# 딕셔너리 사용법
info = {"홍길동" : 100}
#print(info["홍길동"])      # 100

# 딕셔너리 추가하기
info["김유신"] = 87
#print(info)                # {'홍길동': 100, '김유신': 87}

# 딕셔너리 삭제하기
del info["홍길동"]
#print(info)                # {'김유신': 87}

info["박명수"] = 23
info["노홍철"] = 56
info["민들레"] = 24

# {'김유신': 87, '박명수': 23, '노홍철': 56, '민들레': 24}
#print(info)

#[딕셔너리 항목추가]

studentList = []
info = {"이름":"김철수", "수학":100, "국어":32}
studentList.append(info)

info = {"이름":"이만수", "수학":11, "국어":84}
studentList.append(info)

info = {"이름":"박영희", "수학":95, "국어":58}
studentList.append(info)

# 총점 항목 추가하기

studentList[0]["총점"] = studentList[0]["수학"] + studentList[0]["국어"]
# print(studentList)

for i in range(len(studentList)):
    studentList[i]["총점"] = studentList[i]["수학"] + studentList[i]["국어"]
# print(studentList)

# 문제1
# 수학이 꼴등인 학생의 이름 출력
# 정답 : 이만수

print( sorted( studentList , key = ( lambda x: x["수학"] ) )[0]["이름"] )

# 문제2
# 총점이 높은 순서대로 학생의 이름 출력

for i in sorted( studentList , key = ( lambda x: x["총점"] ) , reverse=True ) :
    print(i["이름"])

# 문제3
# 2등 삭제 후, 전체 출력

sortedArr = sorted( studentList , key = ( lambda x: x["총점"] ) , reverse=True )
del sortedArr[1:2]
print(sortedArr)

#