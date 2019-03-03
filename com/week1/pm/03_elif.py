# if 조건문
# if ~ else
# 조건문 = 조건, 비교연산자, and or not
'''
select = "zero cola"

if select == "cola" :
    print("콜라가 나온다")
elif select == "cider" :
    print("사이다가 나온다")
elif select == "water":
    print("물이 나온다")
else:
    print("선택한 음료수가 없습니다")
'''

'''
score에 따라 학점 등급을 출력해주는 코드를 작성하시오.
등급은 90점 이상은 'A' , 80점 이상은 'B', 70점 이상은 'C', 나머지는 'D'
예)
socre = 90
실행 결과
A
'''
score = 77
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")
