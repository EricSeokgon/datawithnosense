import pandas as pd
from sklearn.datasets import load_iris

# iris 변수에 iris 데이터 셋 입력
iris = load_iris()

# iris 데이터 셋의 독립변수 이름 및 데이터 출력
print(iris.feature_names)
print(iris.data)

# iris 데이터 셋의 종속변수 이름 및 데이터 출력
print(iris.target_names)
print(iris.target)

# 데이터 셋 타입 확인
print(type(iris.data))

# ndaray 타입의 iris.data를 pandas 패키지를 이용해 데이터 프레임으로 변경
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
print(df.head(5))

# df데이터 셋에 species열을 추가하고 iris.target을 추가
df['species'] = iris.target
# head()함수를 이용해 df 데이터 셋의 상위 5개 데이터만 출력
print(df.head(5))

# df 데이터 셋의 컬럼명 확인
print(df.columns)

# 컬럼명 변경
df.columns = ['sl', 'sw', 'pl', 'pw', 'sp']
print(df.head(5))

# 5번쨰 컬럼명만 sp에서 s로 변경
df.rename(columns={'sp': 's'}, inplace=True)
print(df.head(5))

# df 데이터 프레임의 데이터 확인
print(df.values)

# df 데이터 프레임의 열 인덱스 확인
print(df.columns)

# df 데이터 프레임의 행 인덱스 확인
print(df.index)

# df 데이터 프레임에서 0~3번째 행의 데이터만 불러오기
print(df[0:4])

# df 데이터 프레임에서 3번째 행의 데이터만 불러오기
print(df[3:4])

# df 데이터 프레임에서 sl열의 데이터만 불러오기
print(df['sl'])

# df 데이터 프레임에서 sl,pl,s열의 데이터만 불러오기
print(df[['sl', 'pl', 's']])

# 3번째 행까지 sl, s열의 데이터만 불러오기
print(df[0:4][['sl', 's']])

# 3번째 행까지 sl, s열의 데이터만 불러오기
print(df.loc[0:3, ('sl', 's')])

# 3번째 행까지 sl, s열의 데이터만 불러오기
print(df.iloc[0:4, [0, 4]])

# df 데이터 셋에서 컬럼 s가 1인 대상만 추출해 df_1에 넣음
df_1 = df[df.s == 1]

# 데이터 프레임의 경우 info()함수를 이용해 데이터 셋 정보 확인 가능
df_1.info()

# tail()함수를 이용하면 끝에서부터 위로 원하는 행만큼 조회 가능
df.tail(5)

# df데이터 셋에서 sl이 6보다 크고, s가 1인 대상만 추출해 df_2에 넣음
df_2 = df[(df.sl > 6) & (df.s == 1)]
print(df_2)

# df데이터 세싱서 s가 0인 대상의 sl, sw, s열만 추출해 df_3에 넣음
df_3 = df.loc[df.s == 0, ['sl', 'sw', 's']]
print(df_3)

# df데이터 셋에서 s열만 제외하고 추출해 df_4에 넣음
df_4 = df[df.columns.difference(['s'])]
print(df_4.head(5))
