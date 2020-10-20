import sympy
import numpy as np
from sympy import I, pi, oo
sympy.init_printing()


#### 해석적 계산 ####
# sympy.solve(expr, symbol)

x, y, z= sympy.symbols("x, y, z")
a, b, c= sympy.symbols("a, b, c")


#### 해석적 계산 ####
print(">>> 해석적 계산 <<<")
expr = x**2 + 2*x - 3
print(expr)
print(sympy.solve(expr))

expr = a * x**2 + 2*b * x + c
print(expr)
print(sympy.solve(expr, x))

expr = sympy.sin(x) - sympy.cos(x)
print(expr)
print(sympy.solve(expr, x))


print("\n"+">>> 특수 계산의 해답 <<<")
expr = x**5 - x**2 +1
print(expr)
print(sympy.solve(expr, x))  ## 해석적으로 답을 구할수 없는 경우

expr = sympy.exp(x) + 2*x
print(expr)
print(sympy.solve(expr, x))  ## 해로써 특수함수를 취급하는 경우


print("\n"+">>> 연립 방정식의 해답1 <<<")
eq1 = x+ 2*y -1
eq2 = x -y +1
print(eq1, eq2)
print(sympy.solve([eq1, eq2], [x, y]))
print(sympy.solve([eq1, eq2], [x, y], dict=True))

print("\n"+">>> 연립 방정식의 해답2 <<<")
eq1 = x**2 -y
eq2 = y**2 -x
print(eq1, eq2)
print(sympy.solve([eq1, eq2], [x, y]))     ##연립해가 여러개일때 차이 발생
print(sympy.solve([eq1, eq2], [x, y], dict=True))

print("\n"+">>> 연립 방정식 해답 검정 <<<")
# 해들을 dict 처리해서 받아두면 아래와 같이 다중 확인시 유용하게 사용가능함
sols = sympy.solve([eq1, eq2], [x, y], dict=True)
judge = [eq1.subs(sol).simplify() == 0 and eq2.subs(sol).simplify() == 0
         for sol in sols]
print(judge)


