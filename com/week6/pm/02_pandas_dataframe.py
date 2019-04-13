import pandas as pd

from pandas import DataFrame

data = {'city': ['Seoul', 'Busan', 'Daejeon', 'Daegu', 'Gwangju'],
       'weather': [9, 11, 11, 10, 10],
       'day':[4, 4, 4, 4, 4]}
frame = DataFrame(data)
print(frame)

# 행에 색인 추가하기
frame1 = DataFrame(data, columns=['day', 'city', 'weather'])
print(frame1)

print(frame1.columns)

print(frame1['day'])

print(frame1['city'])

print(frame1['weather'])


# 행과 열에 색인 추가하기
frame2 = DataFrame(data,
                   columns=['day', 'city', 'weather'],
                   index=['one', 'two', 'three', 'four', 'five']
                  )
print(frame2)

print(frame2['day'])

print(frame2.city)

print(frame2.loc['three']) # ioc gets rows from the index

print(frame2.iloc[4])

frame2 = frame2.append(pd.Series([4, 'Ulsan', 8], index=frame2.columns), ignore_index=True)

print(frame2)

frame2['rainfall amount'] = 0

frame2.at[0, 'rainfall amount'] = 1

print(frame2)

# 행 삭제하기
frame2 = frame2.drop([5], axis=0)

print(frame2)

# 행 삭제하기
frame2 = frame2.drop('rainfall amount', axis=1)

print(frame2)