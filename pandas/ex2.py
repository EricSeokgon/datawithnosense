# numpy 패키지 불러오기 및 np라는 약어로 지칭하기
import numpy as np

# 스칼라
a0 = np.array(1)
print(a0)

# 벡터
a1 = np.array([1, 2])
print(a1)

# 행렬
a2 = np.array([[1, 2], [3, 4]])
print(a2)

# 텐서
a3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 4, 8]]])
print(a3)

# ndim 속성을 이용해 배열의 차원 확인
print(a0.ndim, a1.ndim, a2.ndim, a3.ndim)

# shape 속성을 애용해 배열의 크기 확인
print(a0.shape, a1.shape, a2.shape, a3.shape)

# 3차원 배열에서 1번쨰 행렬 필터링
print(a3[0])

# 3차원 배열에서 1번째 행렬의 2번째 행 필터링
print(a3[0,1])

# 3차원 배열에서 1번째 행렬의 2번째 행의 4번째 열 필터링
print(a3[0,1,2])



