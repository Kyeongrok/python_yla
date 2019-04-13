# numpy, pandas
import numpy as np
from pandas import Series

obj = Series([4, 7, -5, 3])

print(obj)
# 값 출력
print(obj.values)
# 인덱스 출력
print(obj.index)

# 인덱스를 직접 설정해 줄 수 있음
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

print(obj2)
# 값 출력
print(obj2.values)
# 인덱스 출
print(obj2.index)


print(obj2['a'])

obj2['d'] = 6
print(obj2)

# 새롭게 인덱스를 할 수 있음
obj2 = obj2[['c', 'a', 'd', 'b']]
print(obj2)

# 사칙 연산 지원
print(obj2[obj2 > 0])

print(obj2 * 2)

print(np.exp(obj2))

# in 연산자
# dict, list 에서 했었던...
list = [1, 2, 3, 4, 5]
print(list)
print(1 in list)
print(10 in list)

dict = {'a': 1, 'b': 2, 'c':3}
print(dict)
print('a' in dict)
print('b' in dict)
print('d' in dict)

obj2 = Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
print(obj2)
print('a' in obj2)
print('b' in obj2)

sdata = {'Seoul':9, 'Incheon': 10, 'Busan':10, 'Daejeon':10}
obj3 = Series(sdata)
print(obj3)

cities = ['Busan', 'Daejeon', 'Incheon', 'Seoul']
obj4 = Series(sdata, index=cities)
print(obj4)

obj4.name = 'weather'
obj4.index.name = 'city'
print(obj4)

obj4.index = ['Daegu', 'Gwangju', 'Sejeong', 'Jeju']
print(obj4)
