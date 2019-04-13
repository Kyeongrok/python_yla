import numpy as np
import pandas as pd

#https://www.coupang.com/np/search?component=&q=에어컨&channel=user

f = open("./에어컨.json", "r")

df = pd.read_json("./에어컨.json")

# 전체 데이터 보기
print(df)

# 함수 만들어보기
# 입력: 파일 이름
# 출력: dataframe
def create_dataframe(filename):
    df = pd.read_json(filename)
    return df

# head
#print(df.head())

# 보기
#df.info()

# print(df.describe())

# print(df['price'])

# Google
df['price'] = df['price'].str.replace(',', '')

# print(df['price'])

df['price'] = df['price'].astype(np.int)

# 데이터 갯수
print(df['price'].count())

# 가격의 최고 값
print(df['price'].max())

# 가격의 최소 값
print(df['price'].min())

# 가격의 평균 값
print(df['price'].mean())

# 가격이 7000원 이하의 상품 보기
print(df[df['price'] < 7000])


print(df[df['price'] < 7000]['name'])

# 삼성에어컨 찾기
# print(df[df['name'].str.contains("삼성")])
df_samsung = df[df['name'].str.contains("삼성")]

# 삼성 에어컨에서 가격이 제일 높은 에어컨 찾기
print(df_samsung['price'].max())
print(df_samsung[df_samsung['price'] == 4000000])


# LG 에어컨 찾기
df_lg = df[df['name'].str.contains("LG")]
# print(df_lg)

# LG 에어컨에서 가격이 제일 낮은 에어컨 찾기
print(df_lg['price'].min())
print(df_lg[df_lg['price'] == 7330])
print(df_lg[df_lg['price'] == 7330]['name'])
# 가격이 제일 낮은 에어컨의 이름 찾기
print(df_lg[df_lg['price'] == 7330]['name'].values[0])

# 브랜드
# 삼성전자, 캐리어, LG전자, 제너스, 대유위니아, 한솔일렉트로닉스, 대우전자, 보쉬,
# 청호나이스, 에코벨, 아낙, 도비러비, 에이지, 신일, 미디어, 대우컴즈, 21센추리
print("LG")
print(df[df['name'].str.contains("LG")].count().values[0])

# 브랜드별로 찾아보기

# 가격별 정렬
print(df.sort_values(by=['price']))
