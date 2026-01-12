import numpy as np

np.random.seed(42)  #seed값을 고정

a = np.array([10, 20, 30])
print("a:", a)
print("a.shape:", a.shape) 

# arange / reshape
b = np.arange(1, 13).reshape(3, 4)      #arange 값을 추출 -> 3행 4열
print("b:\n", b)

# 기본 통계
print("b.sum():", b.sum())
print("b.mean():", b.mean())
print("b.max():", b.max())
print("b.min():", b.min())

# 난수
r1 = np.random.rand(3)          # 0~1
r2 = np.random.randint(1, 11, size=5)  # 1~10
print("rand(3):", r1)
print("randint(1~10, 5개):", r2)