from scipy import linalg as la
import sympy
sympy.init_printing()
import numpy as np
import matplotlib.pyplot as plt

#### 선형회귀법 ####
## pp.233-237 ##

### 메소드 ###
# la.lstsq(matrix, data)

# 시드 고정
np.random.seed(1512)

# 매개변수
x = np.linspace(-1, 1, 100)
a, b, c = 1, 2, 3
y_exact = a + b*x + c*x**4  # 결정함수

# 노이즈를 포함한 2차원 데이터(X,Y) 100개 묶음
m = 100
X = 1 - 2*np.random.rand(m)   #정보 수집 시간에도 노이즈가 발생한 상태
                              #이것도 시간 -1~1의 100개 데이터를 수집한거임
Y = a + b*X + c*X**4 + np.random.randn(m)   # 결정함수+노이즈
"""
rand  : 0~1 균일분포 표준정규분포 난수배열
randn : 평균0 표준편차1 가우시안 표준정규분포 난수배열
"""

# 선형회귀를 통해 데이터에 적합한 모델 생성
# 1차 회귀의 경우
A = np.vstack([X**n for n in range(2)])
sol, r, rank, sv = la.lstsq(A.T, Y)
"""
input : la.lstsq(matrix, data)
output: sol : 회귀값의 결과
        r : 제곱오차합
        rank : 입력 행렬의 랭크
        sv : 입력 행렬의 특이값
"""
y_fit1 = sum([s*x**n for n, s in enumerate(sol)])
"""
input : enumerate(sol)   return(index, value)
output: (0, x_0)
        (1, x_1)
        ...
        (n, x_n)
"""
print("error of  1st ls =", r)

# 2차 회귀의 경우
A = np.vstack([X**n for n in range(3)])
sol, r, rank, sv = la.lstsq(A.T, Y)
y_fit2 = sol[0] +sol[1]*x + sol[2]*x**2
print("error of  2nd ls =", r)

# 15차 회귀의 경우
A = np.vstack([X**n for n in range(15)])
sol, r, rank, sv = la.lstsq(A.T, Y)
y_fit15 = sum([s*x**n for n, s in enumerate(sol)])
print("error of 15th ls =", r)

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(X, Y, 'go', alpha=0.5)
ax.plot(x, y_exact, 'k--', lw=1)
ax.plot(x,y_fit1, 'r', lw=2)
ax.plot(x,y_fit2, 'b', lw=2)
ax.plot(x,y_fit15, 'm', lw=2)
fig.show()
