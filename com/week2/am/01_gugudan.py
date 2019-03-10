# 구구단2단 출력하는 함수를 만들어 보세요
# gugudan
def gugudan(dan) :
    for j in range(1,10):
        print(dan,'x', j, '=', dan*j)

for dan in range(2, 20+1):
    gugudan(dan)

# 이거 하는데 1시간 걸림
