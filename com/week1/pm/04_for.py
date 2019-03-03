# 반복문
# Hello World 10번 출력하세요
'''
for num in range(10) :
    print("Hello World")
    print("bye")
'''
# for 변수 in 리스트,튜플,문자열 :
#   실행할 코드
'''
          #0       1         2       3
build = ["박보검","아이유","원빈","장동건"]
print(build[0])

for room in build :
    print(room, "와 밥을 먹었습니다")

# 0이상 9미만
# list = [1,2,3,4,5,6,7,8,9]

for num in range(1,10):
    print('Hello, world!',num)


sum = 0
for i in range(1, 11):
    sum = sum + i
print(sum)
# list = [1,2,3,4,5,6,7,8,9,10]

# list = [1,3,5,7,9]

for i in range(1, 10, 2):
    print('Hello, world!', i)

# list = [10,9,8,7,6,5,4,3,2,1]

for i in range(10, 0, -1):    # 10에서 1까지 1씩 감소
    print('Hello, world!', i)
'''
# 구구단 출력
def gugudan(dan) :
    for num in range(1, 10):
        print(dan, "x", num, "=", dan * num)

gugudan(2)
gugudan(3)
