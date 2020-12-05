import sympy
from sympy import I, pi, oo
sympy.init_printing()


#### 행렬 ####
# sympy.Matrix(list)
# sympy.Matrix(size, lambda)


#### 행렬 메소드 목록 ####
# 전부 self.@@로 호출한다.
##>>>연관 행렬<<<##
# transpose, T      ## 전치행렬
# adjoint, H        ## 수반행렬
# inv               ## 역행렬
##>>>행렬의 속성<<<##
# trace             ## 트레이스
# det               ## 행렬식
# norm              ## 노름
# nullspace         ## 영공간
# rank              ## 랭크
# singular_values   ## 특이값
##>>>연립방정식 해답 구하기<<<##
# solve             ## Mx=b 의 해x
# LUdecomposition   ## LU분해
# LUsolve           ## LU를 이용한 해
# QRdecomposition   ## QR분해
# QRsolve           ## QR을 이용한 해
# diagonalize       ## bMP 대각화

a, b, c, d= sympy.symbols("a, b, c, d")


#### 행렬 ####
print(">>> 행렬 생성1 <<<")
print(sympy.Matrix([1, 2]))
"""
⎡1⎤
⎢ ⎥
⎣2⎦
"""
print(sympy.Matrix([[1, 2]]))
"""
[1  2]
"""
row1=[1,2]
row2=[3,4]
vector=[row1, row2]
print(sympy.Matrix(vector))
"""
⎡1  2⎤
⎢    ⎥
⎣3  4⎦
"""

print("\n"+">>> 행렬 생성2 <<<")
print(sympy.Matrix(3,4, lambda m,n : 10*m+n))
M = sympy.Matrix([[a,b],[c,d]])
print(M)
print(M*M)
x = sympy.Matrix(sympy.symbols("x_1, x_2"))
print(M*x)
