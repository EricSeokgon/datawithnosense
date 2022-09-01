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
