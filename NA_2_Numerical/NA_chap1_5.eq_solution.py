import sympy
sympy.init_printing()
import numpy as np


#### 해석적 방정식 해 구하기 ####
## pp.240-241 ##

### 메소드 ###
# sympy.solve(func, var)  # 솔루션이 있는 경우 해석적 답을 반환

x, a, b, c = sympy.symbols("x, a, b, c")
sol = sympy.solve(a + b*x + c*x**2, x)
print(sol)

sol = sympy.solve(a*sympy.cos(x) - b*sympy.sin(x), x)
print(sol)

#sol = sympy.solve(sympy.sin(x)-x, x)
#print(sol)
#>> Error : "해석적 알고리즘이 없음"


