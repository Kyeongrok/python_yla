def getPlus(val1, val2):
    result = val1 + val2
    return result

result = getPlus(20, 30)
print(result)

def getMinus(val1, val2):
    result = val1 - val2
    return result

# 다른점
# 1. return이 있다.
# 2. print가 함수 밖에 있다.
# 3. result라는 변수를 정의해서 값을 넣었다.
# 4. print -> get으로 바뀜

resultMinus = getMinus(20, 30)
print(resultMinus)

# multiple, divide
def getMultiple(val1, val2):
    return val1 * val2

def getDivide(val1, val2):
    return val1 / val2

print(getMultiple(20, 30))
print(getDivide(20, 30))

# (10 + 20) / (30 - 40)
# result: <결과>

result = getDivide(getPlus(10, 20), getMinus(30, 40))
print("result:", result)