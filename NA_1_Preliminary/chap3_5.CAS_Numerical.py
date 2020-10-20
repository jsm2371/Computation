import sympy
import numpy as np
from sympy import I, pi, oo
sympy.init_printing()


#### 수치 계산 ####
# sympy.N(num, float=int)   #소숫점 float자리까지 수치 계산결과 반환
# expr.evalf(float=int)    ##위와 동일 역할 수행 
# sympy.lambdify(x, expr, package) #위와 동일한데 다른 패키지의 연산속도 호출

x, y, z= sympy.symbols("x, y, z")

#### 수치 계산 ####
print(">>> 수치 계산 <<<")
expr = 1+pi
print(expr)
print(sympy.N(expr, 30))
print(expr.evalf(30))

expr = x + 1/pi
print(expr)
print(sympy.N(expr, 30))
print(expr.evalf(30))


print("\n"+">>> 반복 계산 1 <<<")
expr = sympy.sin(pi*x*sympy.exp(x))
print(expr)
print(sympy.N(expr.subs(x,1), 8))
nums = [expr.subs(x,xx).evalf(8) for xx in range(0,10)]
print(nums)
#*위의 방법으로 대량의 계산을 수행하는 것은 느리므로 다른 방안이 제시됨

print("\n"+">>> 반복 계산 2 <<<")
expr_func = sympy.lambdify(x, expr)
print(expr_func(1))
# 심지어 이 기법은 다른 패키지의 연산속도를 빌려올수 있다
expr_func = sympy.lambdify(x, expr, 'numpy')
xvals = np.arange(0, 10)
print(expr_func(xvals))


