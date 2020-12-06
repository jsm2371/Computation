from scipy import linalg as la
import sympy
sympy.init_printing()
import numpy as np
import matplotlib.pyplot as plt


#### 조건수 ####
## pp.224-233

### 메소드 ###
# self.condition_number().simplify()
#    simplify()까지 선언해야 수치로 표현해줌.
"""
조건수 : "특이값의 최대값"÷"특이값의 최소값"
   사실 정의를 보면 역행렬노름*행렬노름 이라 되어있는데
   아마도 특이행렬은 이 방법으로 구할수 없어서 그런것 같다.
"""
def con_num(A):
    sv = A.singular_values()
    return max(sv)/min(sv)

"""
프로베니우스 노름 : "각 요소의 제곱들의 합의 제곱근"
   노름의 종류는 여러가지인데 이 중 가장 대표적인 노름.
   일반적인 유클리드 노름의 행렬버전이라 생각하면 됨.
"""
def fro_norm(A):
    result = 0
    for p in A:
        result += p**2
    return sympy.sqrt(result)


## sympy 패키지의 경우
print(">>> sympy 행렬 <<<")
A = sympy.Matrix([[2, 3], [5, 4]])
b = sympy.Matrix([4, 3])
print(A,b)
print("rank =", A.rank())
cn = A.condition_number() #위에서 정의한 con_num(A)와 동일
nm = A.norm()   #프로베니우스 노름 계산함
print("cond =", sympy.N(cn), '=', cn)
print("norm =", sympy.N(nm), '=', nm)
L, U, _ = A.LUdecomposition()
print("L =",L)
print("U =",U)
print("L*U =", L * U)
print("x:Ax=b is", A.solve(b))  #A.LUsolve(b)와 동일


## numpy 패키지의 경우
print("\n>>> numpy 행렬 <<<")
A = np.array([[2, 3], [5, 4]])
b = np.array([4, 3])
print(A,b)
print("rank =", np.linalg.matrix_rank(A))
print("cond =", np.linalg.cond(A))
print("norm =", np.linalg.norm(A))
P, L, U = la.lu(A)
print("L =\n", L)
print("U =\n", U)
print("L*U =\n", P.dot(L.dot(U)))
print("x:Ax=b is", la.solve(A, b))




#### 수치해 ####
# 행렬 그 자체가 갖고있는 특성이다.
# 미세한 오차가 아주 커다란 차이를 만들어낸다는 걸 수치적으로 나타내어준다.
# 조건수가 세자릿수가 넘어가기 시작하면 수치해의 오차가 크게 발생하기 시작함.
# 예시로는 [[1, sqrt(p)], [1, 1/sqrt(p)]] 라는 행렬을 갖고 설명하기 좋다.
# 위의 행렬의 경우 p가 1에 가까워질수록 오차가 급격히 커진다.
# 그래프의 결과를 살펴보면 약 조건수 150 이상이 되니 오차변동폭이 커지는듯.

p = sympy.symbols("p", positive=True)
A = sympy.Matrix([[1, sympy.sqrt(p)], [1, 1/sympy.sqrt(p)]])
b = sympy.Matrix([1,2])

x_sym_sol = A.solve(b)
Acond = A.condition_number().simplify()

## 조건수가 커지면 수치해도 큰 변동이 발생한다는 것을 보여주는 그래프
# 이걸 lambda를 써서 sympy처럼 함수역할을 하게 만든거임
AA = lambda p: np.array([[1, np.sqrt(p)], [1, 1/np.sqrt(p)]])
bb = np.array([1, 2])
x_num_sol = lambda p: np.linalg.solve(AA(p), bb)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

p_vec = np.linspace(0.9, 1.1, 200)
for n in range(2):
    x_sym = np.array([x_sym_sol[n].subs(p, pp).evalf() for pp in p_vec])
    x_num = np.array([x_num_sol(pp)[n] for pp in p_vec])
    if n==0:
        axes[0].plot(p_vec, (x_num - x_sym)/x_sym, 'k')
    elif n==1:
        axes[0].plot(p_vec, (x_num - x_sym)/x_sym, 'r')

axes[1].plot(p_vec, [Acond.subs(p, pp).evalf() for pp in p_vec])

plt.show()





