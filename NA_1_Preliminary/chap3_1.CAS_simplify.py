import sympy
from sympy import I, pi, oo
sympy.init_printing()


#### 수식 단순화 ####
# sympy.simplify(expr) #단순화 -휴리스틱 접근법에 의존하고 있음.
#   self.simplify()
# sympy.trigsimp(expr) #삼각함수 특화
# sympy.powsimp(expr)  #멱함수 특화

# sympy.compsimp(expr)  #조합 특화
# sympy.ratsimp(expr)  #공통분모 특화


#### 수식 단순화 ####
print(">>> 수식 단순화 <<<")
x, y= sympy.symbols("x, y")
expr = 2 * (x**2 - x) - x * (x+1)
print(expr)
print(sympy.simplify(expr))
print(expr.simplify())
print(expr)

print("\n"+">>> 수식 단순화2 <<<")
expr = 2 * sympy.cos(x) * sympy.sin(x)
print(expr)
print(sympy.simplify(expr))
print(sympy.trigsimp(expr))

print("\n"+">>> 수식 단순화3 <<<")
expr = sympy.exp(x) * sympy.exp(y)
print(expr)
print(sympy.simplify(expr))
print(sympy.powsimp(expr))



