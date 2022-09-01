import pandas as pd
from sklearn.datasets import load_iris

#iris 변수에 iris 데이터 셋 입력
iris = load_iris()

#iris 데이터 셋의 독립변수 이름 및 데이터 출력
print(iris.feature_names)
print(iris.data)

#iris 데이터 셋의 종속변수 이름 및 데이터 출력
print(iris.target_names)
print(iris.target)

#데이터 셋 타입 확인
print(type(iris.data))

#ndaray 타입의 iris.data를 pandas 패키지를 이용해 데이터 프레임으로 변경
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
print(df.head(5))

# df데이터 셋에 species열을 추가하고 iris.target을 추가
df['species'] = iris.target
#head()함수를 이용해 df 데이터 셋의 상위 5개 데이터만 출력
print(df.head(5))

# df 데이터 셋의 컬럼명 확인
print(df.columns)

#컬럼명 변경
df.columns=['sl','sw','pl','pw','sp']
print(df.head(5))

# 5번쨰 컬럼명만 sp에서 s로 변경
df.rename(columns={'sp':'s'}, inplace=True)
print(df.head(5))

# df 데이터 프레임의 데이터 확인
print(df.values)

# df 데이터 프레임의 열 인덱스 확인
print(df.columns)

# df 데이터 프레임의 행 인덱스 확인
print(df.index)