from scipy import linalg as la
import sympy
sympy.init_printing()
import numpy as np

#### 고윳값 ####
## pp.237-239 ##

### 메소드 ###
# self.eigenvals()      # 행렬의 해석적 고윳값
# self.eigenvects()     # 행렬의 해석적 고유벡터
# la.eigvals(matrix)    # 행렬의 수치적 고윳값
# la.eig(matrix)        # 행렬의 수치적 고윳값/고유벡터
# la.eigvalsh(matrix)   # 행렬의 수치적 실고윳값
# la.eigh(matrix)       # 행렬의 수치적 실고윳값/고유벡터

eps, delta = sympy.symbols("epsilon, Delta")
H = sympy.Matrix([[eps, delta], [delta, -eps]])
print(H)
## 해석적 방법으로 고윳값을 구한 결과
print(">>> 해석적 고윳값 <<<")
print(H.eigenvals())
print(H.eigenvects())

(eval1, _, evec1), (eval2, _, evec2) = H.eigenvects()
inner_raw = evec1[0].T*evec2[0]
inner = sympy.simplify(inner_raw)
print(inner_raw)
print(inner)

## 수치적 방법으로 고윳값을 구한 결과
print("\n>>> 수치적 고윳값 <<<")
A = np.array([[1,3,5], [3,5,3], [5,3,9]])
evals, evecs = la.eig(A)
print("수치 고윳값 =",evals)
print("수치 고유벡터 =\n",evecs)
# 복소 수치적 접근
print("수치 고윳값 =",la.eigvals(A))
print("수치 고윳값/고유벡터 =\n",la.eig(A))
# 실수만을 대상으로 하는 수치적 접근
# 실대칭/에르미트 행렬은 전부 실수 고윳값을 가지므로 이걸 사용하면 더 좋음
print("수치 실고윳값 =",la.eigvalsh(A))
print("수치 실고윳값/고유벡터 =\n",la.eigh(A))


