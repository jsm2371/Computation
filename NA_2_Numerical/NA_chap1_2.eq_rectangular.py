import sympy
sympy.init_printing()
import numpy as np



#### 비정방 선형방정식의 정확한 해 얻는 방법 ####
## pp.233-234

### 메소드 ###
# sympy.solve(func, (vars))

"""
연립방정식의 해
 x + 2y + 3z = 7
4x + 5y + 6z = 8
"""
x_vars = sympy.symbols("x_1, x_2, x_3")
A = sympy.Matrix([[1,2,3], [4,5,6]])
x = sympy.Matrix(x_vars)
b = sympy.Matrix([7,8])
sol = sympy.solve(A*x - b, x_vars)
print(sol)


